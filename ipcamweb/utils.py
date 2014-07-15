# Andrea Masi 2014 eraclitux@gmail.com

import os

def ensure_secret():
    """Check if secret key for coockies exists,
    generating it otherwise."""
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
