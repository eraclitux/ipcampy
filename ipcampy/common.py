# Common definitions 
# Andrea Masi 2014 eraclitux@gmail.com

class CamException(Exception):
    """Custom exception raised in case of predictable errors."""
    pass

class IpCam:
    """Base ipcam class"""

    def __init__(self, address, name=None, user=None, pswd=None):
        self.cam_type = self.get_type()
        self.address = address
        self.name = name
        self.cam_id = self.address.replace(".", "").replace(":", "")
        # Human friendly name like 'Gate-1'
        if self.name:
            self.name = name.replace(" ","-")
        self.user = user
        self.pswd = pswd

    def get_type(self):
        """Return ipcam type (foscam, ect).
        Type is taken from package name."""
        return self.__class__.__module__.split(".")[1]
