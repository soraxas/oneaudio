from enum import Enum

url = 'http://192.168.0.151'

# volume_down = 'cgi-bin/post_command.cgi?v=12000'
# volume_down1 = 'cgi-bin/post_command1.cgi?v=12000'
# volume_up = 'cgi-bin/post_command.cgi?v=12100'
# volume_up1 = 'cgi-bin/post_command1.cgi?v=12100'

POST_COMMAND = 'cgi-bin/post_command.cgi?v='
INFO_REQUEST = 'cgi-bin/get_home_display.cgi'
SPEAKER_INFO_REQUEST = 'cgi-bin/get_speaker_display.cgi'

class InputSource(Enum):
    """Input source."""

    standby = '11000'
    toslink = '11100'
    dlna = '11200'
    airplay = '11300'
    usbaudio20 = '11400'
    musicserver = '11500'
    internetradio = '11600'


class SystemControl(Enum):
    """System control."""

    poweroff_microbox = '11S00'
    poweroff_speaker = '10000'
    test_speaker = '20100'
    add_speaker = '20200'


class Volume(Enum):
    """Volume control."""

    decrease = '12000'
    increase = '12100'
    mute = '13000'


class VolumeSet:
    """Set volume for oneaudio micro box."""

    @staticmethod
    def volume(vol):
        """Conver the given in to required format

        :param volume within range of 0 to 60 inclusive
        """
        if vol < 0 or vol > 60:
            raise Exception('Must be within 0 to 60.')
        # required format is a two digit string represing the desire volume
        vol = str(int(vol))
        vol.rjust(2, '0')
        return '122{0}'.format(vol)


# a = requests.post('{}/{}'.format(url, MasterVolumeRange))




#
# document.getElementById("link_speaker").onclick = function() {
# 	if(flash_input==0xFF)
# 		location.href='speaker.html';
# }
