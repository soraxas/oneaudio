import requests
from const import POST_COMMAND, INFO_REQUEST


    # except requests.exceptions.ConnectTimeout:
    #     a = 'TIMEOUT!!'
    # except requests.exceptions.ConnectionError:
    #     a = 'CONNECTION REFUSED...'
    # print('{} -> {}'.format(a, i))
    # i += 1



class MicroBox:
    """ONEaudio micro box instance for controlling each aspect"""

    def __init__(self, device_ip):
        self._device_ip = device_ip
        self._session = requests.Session()


    def get_info(self):
        info = self._session.get('http://{}/{}'.format(
            self.device_ip, INFO_REQUEST), timeout=2)
        return info


    def post_command(self, command):
        self._session.post('http://{}/{}{}'.format(
            self.device_ip, POST_COMMAND, command.value), timeout=2)

    @property
    def device_ip(self):
        return self._device_ip
