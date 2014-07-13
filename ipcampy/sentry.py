# Andrea Masi 2014 eraclitux@gmail.com

import json
import time
from ipcampy.globals import cam_types

def __parse_args(cam_c):
    """Arrange class init params from conf file.
    Returns: a dict with values."""
    user = None
    pswd = None
    name = None
    address = "{address}:{port}".format(**cam_c)
    if "user" in cam_c:
        user = cam_c["user"]
        if "pswd" in cam_c:
            pswd = cam_c["pswd"]
    if "name" in cam_c:
        name = cam_c["name"]
    return {"user": user, "pswd": pswd, "name": name, "address": address}

def load_cams(conf_file):
    """Reads cams conf from file and intantiate appropiate classes.
    Returns: an array of IpCam classes."""
    with open(conf_file, "r") as c_file:
        lines = c_file.readlines()
    cams_conf = [json.loads(j) for j in lines]
    cams = []
    for cam_c in cams_conf:
        init_params = __parse_args(cam_c)
        cams.append(cam_types[cam_c["type"]](**init_params))
    return cams

def watch(cams, path=None, delay=10):
    """Get screenshots from all cams at defined intervall."""
    while True:
        for c in cams:
            c.snap(path)
        time.sleep(delay)
