import json
import subprocess
import os
import logging

import numpy as np
import pandas as pd
import requests
import time

logger = logging.getLogger(__name__)

_host = None #: PlotHost
DEFAULT_SERVER = 'http://localhost:2908'


def plotar(data, col=None, size=None, *, xyz=None, type='p', lines=None, label=None,
           axis_names=None, col_labels=None,
           name=None, description=None, speed=None, auto_scale=True,
           digits=5, host=None, return_data=False, push_data=True):
    # TODO assert compatibility checks
    n = data.shape[0]
    df = None
    if isinstance(data, pd.DataFrame):
        df = data
        if xyz is not None:
            assert len(xyz)==3
            data = df[xyz].values
            axis_names = axis_names or xyz
        else:
            data = df.iloc[:,0:3].values
            val = locals().get(i)
            axis_names = axis_names or df.columns[xyz].tolist()

    def _mk_val(df, val):
        if val is None:
            return None
        elif val is not None and isinstance(val, str) and val in df.columns:
            return df[val].values
        elif isinstance(val, float):
            return np.zeros((n,)) + val
        else:
            return np.array(val)

    col   = _mk_val(df, col)
    size  = _mk_val(df, size)
    lines = _mk_val(df, lines)
    label = _mk_val(df, label)

    for i in [col, size, lines, label]:
        assert i is None or i.shape == (n,), f"Parameters need to have same length: {i} has shape {i.shape} but would need {(n,)}"
    if auto_scale:
        # have all variables scaled to [-1,1]
        data = scale(data)
        if size is not None:
            # scale the sizes between 0.5 and 1.5:
            size = scale(size.reshape((-1, 1)))[:,0] + 1.5
    if col is not None and col.dtype == np.dtype('O'):
        x = pd.Series(col, dtype='category')
        col = x.cat.codes.values
        col_labels = x.cat.categories.values.tolist()
    if col is None:
        payload = data[:,:3]
    else:
        payload = np.hstack((data[:,:3],col.reshape((-1,1))))
    # todo: remove NAs, center and scale...
    body = {'data': payload.tolist(),'speed': 0, 'protocolVersion': '0.3.0'}

    if col is not None: body['col'] = col.tolist()
    if size is not None: body['size'] = size.tolist()
    if type is not None: body['type'] = type
    if label is not None: body['label'] = label.tolist()
    if speed is not None: body['speed'] = speed
    if axis_names is not None: body['axis_names'] = axis_names
    if col_labels is not None: body['col_labels'] = col_labels

    metadata = { 'n': n, 'created': time.ctime() }
    metadata['name'] = name or "Dataset"
    if description is not None: metadata['description'] = description
    body['metadata'] = metadata
    # data_json = json.dumps(, allow_nan=False)
    if push_data:
        plot_host = get_host(host)
        plot_host.post(json=body)
    if return_data:
        return body

def surfacevr(data, col=None, x=None, y=None,
           name=None, description=None, speed=None, auto_scale=True,
           digits=5, host=None, return_data=False, push_data=True):
    global _host
    _host = host
    # TODO assert compatibility checks
    n,m = data.shape
    for i in [col]:
        assert i is None or i.shape == data.shape, f"Parameters need to have same shape: {i} has shape {i.shape} but would need {data.shape}"
    if auto_scale:
        # have the data scaled to [-1,1]
        a,b = data.min(),data.max()
        if a <= 0 <= b:
            # keep the 0 at 0 and scale around that
            mx = max(-a,b)
            mx = mx or 1 # set to 1 if 0
            data = data / mx
        else:
            data = scale(data, axis=(0,1))
        x = scale(x)
        y = scale(y)
    # TODO: remove NAs
    body = {'surface': {'data':data.tolist(), 'col':col, 'shape': (n,m)},'speed': 0, 'protocolVersion': '0.3.0'}
    if x is not None:
        body['surface']['x'] = np.array(x).tolist()
    if y is not None:
        body['surface']['y'] = np.array(y).tolist()
    if speed is not None: body['speed'] = speed
    metadata = { 'n': n, 'm': m, 'created': time.ctime() }
    metadata['name'] = name or f"Dataset {n}x{m}"
    if description is not None: metadata['description'] = description
    body['metadata'] = metadata
    if push_data:
        plot_host = get_host(host)
        plot_host.post(json=body)
    if return_data:
        return body


def scale(data, axis=(0,)):
    if data is None:
        return None
    if min(data.shape) == 0:
        return data
    ranges = np.array(data.max(axis) - data.min(axis))
    ranges[ranges == 0] = 1
    data = (data - data.min(axis)) / ranges * 2 - 1
    return data


def controller(width="100%", height="200px"):
    url = get_host().external_url("keyboard.html")
    if is_in_jupyter():
        try:
            from IPython.display import IFrame
            return IFrame(url, width=width, height=height)
        except ImportError:
            return url
    else:
        return url

def viewer(width="100%", height="400px"):
    url = get_host().external_url("index.html")
    try:
        from IPython.display import IFrame
        return IFrame(url, width=width, height=height)
    except ImportError:
        return url


def get_host(host=None):
    global _host
    if host is not None:
        return PlotHost(host)
    if _host is None:
        # actual detection code
        jpy = my_jupyter_server()
        if jpy is not None:
            hub_prefix = os.getenv("JUPYTERHUB_SERVICE_PREFIX")
            if hub_prefix is None:
                ext = jpy['url'] + "plotar/"
            else:
                # on jupyter-/binderhub we don't know the external hostname,
                # so we use an absolute URL
                ext = hub_prefix+"plotar/"
            _host = PlotHost(jpy['url']+"plotar/", external_url=ext, params=jpy['params'], headers=jpy['headers'])
        else:
            _host = PlotHost(DEFAULT_SERVER)
    return _host


class PlotHost:
    def __init__(self, url: str, external_url: str = None, params='', headers={}):
        self.url = url
        if url is None or len(url) == 0 or not isinstance(url, str):
            raise ValueError("URL must be not None and a non-empty string.")
        if self.url[-1] != '/':
            self.url += '/'
        if external_url is None:
            external_url = self.url
        self._external_url = external_url
        self.params = "?"+params
        self.headers = headers
    def internal_url(self, path):
        '''Shows the URL that is '''
        return self.url + path #+ self.params
    def external_url(self, path):
        return self._external_url + path + self.params
    def post(self, json):
        response = requests.post(self.internal_url(""), json=json, headers=self.headers)
        response.raise_for_status()
    def __repr__(self):
        return f"PlotHost({self.url})"
    def _repr_html_(self):
        return f"PlotAR at <a href='{self.url}'>{self.url}</a>"

def my_jupyter_server(verbose=False, jupyter_parent_pid=None):
    servers = []
    imported_notebookapp = imported_serverapp = False
    try:
        from jupyter_server import serverapp
        servers += serverapp.list_running_servers()
        imported_serverapp = True
    except ImportError:
        pass
    try:
        from notebook import notebookapp
        imported_notebookapp = True
        servers += notebookapp.list_running_servers()
    except ImportError:
        pass
    if not len(servers):
        if verbose:
            import warnings
            warnings.warn(f"no running jupyter server found - imported jupyter_server: {imported_serverapp} notebook: {imported_notebookapp}")
        return None
    server_pid = os.getenv('JPY_PARENT_PID', jupyter_parent_pid)
    if server_pid is None:
        if len(servers) > 1:
            pass
        jpy = servers[0]
    else:
        for s in servers:
            if str(s['pid']) == server_pid:
                jpy = s
                break
        else:
            # no matching pid found...
            if verbose:
                print('no matching jupyter server found!')
            jpy = servers[0]
    if jpy is None:
        return None
    return dict(url=jpy['url'],
                params="token="+jpy['token'],
                headers={'Authorization': 'token ' + jpy['token']},
                )

def start_server_process(port: int = 2908, showServerURL=True):
    """Start Server in another process.

    Parameters
    ----------
    port
        The port on which to run the server (default is 2908).

    Returns
    -------
    Completed Process of `subprocess.run`.

    """
    import sys
    python = sys.executable
    # or os.__file__.split("lib/")[0],"bin","python") ?
    
    proc = subprocess.Popen([python, '-m', 'plotar.server', str(port)])

    if showServerURL:
        url = _host+'/index.html'
        try:
            response = requests.get(_host+"/qr.json")
            response.raise_for_status()
            url = response.json()['url']
        except Exception as ex:
            print("Problem getting external IP: ", ex)
            pass
        try:
            from IPython.display import display, SVG, HTML
            import pyqrcode
            from io import BytesIO
            io = BytesIO()
            pyqrcode.QRCode(url).svg(io, scale=4)
            img = io.getvalue().decode('utf-8')
            display(HTML(f'Visit: <a href="{url}">{url}</a>'))
            display(SVG(img))
        except ImportError:
            print(f"Visit: {url}")

    return proc

def is_in_jupyter() -> bool:
    # https://stackoverflow.com/a/39662359/6400719
    try:
        from IPython import get_ipython
        shell = get_ipython().__class__.__name__
        if shell == "ZMQInteractiveShell":
            return True  # Jupyter notebook or qtconsole
    except:
        return False  # Probably standard Python interpreter
    return False


