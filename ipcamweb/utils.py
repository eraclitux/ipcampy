# Andrea Masi 2014 eraclitux@gmail.com

import os
import datetime

def ensure_secret():
    """Check if secret key to encryot sessions exists,
    generate it otherwise."""
    home_dir = os.environ['HOME']
    file_name = home_dir + "/.ipcamweb"
    if os.path.exists(file_name):
        with open(file_name, "r") as s_file:
            secret = s_file.readline()
    else:
        secret = os.urandom(24)
        with open(file_name, "w") as s_file:
            secret = s_file.write(secret+"\n")
    return secret

def list_snapshots_days(path, cam_id):
    """Returns a list of (date, dir) in which snapshopts are present"""
    screenshoots_path = path + "/" + str(cam_id)
    if os.path.exists(screenshoots_path):
        days = []
        for day_dir in os.listdir(screenshoots_path):
            date = datetime.datetime.strptime(day_dir, "%d%m%Y").strftime('%d/%m/%y')
            days.append((date, day_dir))
        return days
    else:
        return []
