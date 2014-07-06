# Foscam specific definitions. 
# Andrea Masi 2014 eraclitux@gmail.com

import urllib
# TODO remove this requiremet (?), use only urllib
import requests
from ipcampy.common import IpCam, CamException

def map_position(pos):
    """Map natural position to machine code postion"""

    posiction_dict = dict(zip(range(1, 17), [i for i in range(30, 62) if i % 2]))
    return posiction_dict[pos]

class FosCam(IpCam):
    """Specific for Foscam ipcams.
    Known to work: FI8908W"""

    # FIXME urllib.urlretrieve prompt in case of wrong credentials
    # Find a way to return an error
    def snap(self, filename=None):
        """Get a snapshot and save it to disk."""
        if filename:
            f_path = filename
        elif self.name:
            f_path = self.name + ".jpg"
        else:
            # TODO add date 
            f_path = "{0}-{1}.jpg".format(self.cam_type, self.address)

        resp = urllib.urlretrieve(
            'http://{0}/snapshot.cgi?user={1}&pwd={2}'.format(
                                    self.address, 
                                    self.user, 
                                    self.pswd,
                                    ),
            f_path,
        )
        #print resp[1]['Content-disposition'].replace("filename=\"","")[:-1]

    def move(self, pos):
        """Move cam to given preset position.
        pos - must be within 1 to 16.
        Returns: CamException in case of errors, "ok" otherwise."""

        try:
            payload = {"address":self.address, "user": self.user, "pwd": self.pswd, "pos": map_position(pos)}
            resp = requests.get(
                    "http://{address}/decoder_control.cgi?command={pos}&user={user}&pwd={pwd}".format(**payload)
            )
        except KeyError:
            raise CamException("Position must be within 1 to 16.")
        if resp.status_code != 200:
            raise CamException("Unauthorized. Wrong user or password.")
        return "ok"

    def status(self):
        """Retrieve some configuration params.
        Note: info are returned even without password"""

        resp = requests.get("http://{0}/get_status.cgi".format(self.address))
        data = resp.text.replace(";", "")
        data = data.replace("var", "")
        data_s = data.split("\n")
        # Last is an empty line 
        data_s.pop()
        data_array = [s.split("=") for s in data_s]
        return dict(data_array)
