import serial
from time import sleep
from kodijson import Kodi

kodi = Kodi("http://192.168.29.113:8080/jsonrpc") #Kodi API endpoint

port_names = ['/dev/ttyACM0', '/dev/ttyACM4', '/dev/ttyACM5', '/dev/ttyACM1']
port_name_str = ','.join(port_names)
arduino_actions = {
    "6F9FA05": "up",
    "6F92AD5": "down",
    "6F91AE5": "right",
    "6F99A65": "left",
    "6F906F9": "select",
    "6F9708F": "back",
    "6F958A7": "volumeup",
    "6F97887": "volumedown",
    "6F908F7": "mute",
    "6F948B7": "shutdown",
    "6F9B04F": "fullscreen",
    "6F94AB5": "info",
    "6F9C837": "stop",
    "6F9A857": "playpause",
    "6F9E817": "forward",
    "6F9C639": "backward"
}
def connectToArduino():
    arduino = None
    arduino_found = False
    sleep(1)
    while not arduino_found:
        for i, port_name in enumerate(port_names):
            try:
                arduino = serial.Serial(port=port_name, baudrate=115200, timeout=.1)
                arduino_found = True
                print("Arduino found and Connected!")
                break
            except serial.SerialException:
                pass

        if not arduino_found:
            print(addon.getAddonInfo('name') + ': Arduino not found, retrying in 5 seconds')
            sleep(5)

        sleep(2)

    return arduino

def remoteListener():
    arduino = connectToArduino()
    prev_command = ""
    prev_value = ""
    count = 0

    while True:
        try:
            value = arduino.readline().decode('utf-8').strip()
            if value:
                print(value)
                if value == "FFFFFFFF":
                    if prev_value == "FFFFFFFF":
                        count += 1
                        if count > 5 and prev_command:
                            action = prev_command
                            kodi.Input.ExecuteAction({'action': action})
                        else:
                            continue
                    else:
                        count = 1
                else:
                    try:
                        action = arduino_actions[value]
                        if action == "shutdown":
                            kodi.System.Shutdown()
                        else:
                            kodi.Input.ExecuteAction({'action': action})
                        prev_command = action
                        count = 0
                    except KeyError:
                        pass
                prev_value = value
        except serial.SerialException as e:
           print(addon.getAddonInfo('name') + ': Error with Serial: ' + str(e))
           break
        except KodiException as e:
           print(addon.getAddonInfo('name') + ': KodiException: ' + str(e))
           break

        sleep(0.01)

remoteListener()
