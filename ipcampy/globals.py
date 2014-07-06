# Global dictionary holding specific cam classes that inherit IpCam
from ipcampy.foscam import FosCam

cam_types = {}
cam_types["foscam"] = FosCam
