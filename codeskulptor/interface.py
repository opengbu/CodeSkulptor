import os
import zipfile

from . import DEFAULT_HOST, DEFAULT_PY2_PORT, DEFAULT_PY3_PORT, WWW_ROOT, WWW_ROOT_ZIP
from . import __version__


def run_grabber(verbose=False):
    from .grabber import Grabber

    print("Downloading fresh copy of CodeSkulptor from live site.")
    print("This requires an active internet connection")
    print("Please be patient while downloading as that might take few moments based on your internet connection")
    print("")

    www_dir = os.path.join(WWW_ROOT, "py2")
    print("Saving http://www.codeskulptor.org to %s..." % www_dir)
    Grabber("http://www.codeskulptor.org", verbose=verbose).grab(www_dir, clean=True)

    www_dir = os.path.join(WWW_ROOT, "py3")
    print("Saving http://py3.codeskulptor.org to %s..." % www_dir)
    Grabber("http://py3.codeskulptor.org", verbose=verbose).grab(www_dir, clean=True)

    print("\nAll Done!")


def run_server(address, version, open_browser=True):
    print("Unofficial CodeSkulptor Local Server (version %s)" % __version__)
    print("\nFor further details and issue reporting please visit https://github.com/uadnan/CodeSkulptor")

    this_www = os.path.join(WWW_ROOT, "py%s" % version)

    if not os.path.exists(this_www) and os.path.exists(WWW_ROOT_ZIP):
        with zipfile.ZipFile(WWW_ROOT_ZIP, "r") as f:
            f.extractall(WWW_ROOT)

    print("Starting CodeSkulptor server at http://%s:%s/" % address)
    print("Serving from %s" % this_www)
    print("Quit the server with CONTROL-C.")

    from .server import serve

    serve(address, this_www, open_browser=open_browser)


def run_py2(host=DEFAULT_HOST, port=DEFAULT_PY2_PORT):
    run_server((host, port), version=2)


def run_py3(host=DEFAULT_HOST, port=DEFAULT_PY3_PORT):
    run_server((host, port), version=3)
