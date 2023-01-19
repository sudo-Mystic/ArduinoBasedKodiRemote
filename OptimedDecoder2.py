import serial
from time import sleep
from kodijson import Kodi

# List of possible serial port names
port_names = ['/dev/ttyACM0', '/dev/ttyACM1', '/dev/ttyUSB0', '/dev/ttyUSB1']

# Infinite loop to continuously scan for the Arduino
while True:
    arduino_found = False
    # Iterate through the list of possible port names
    for port_name in port_names:
        try:
            # Try to open the serial port
            arduino = serial.Serial(port=port_name, baudrate=115200, timeout=.1)
            arduino_found = True
            break
        except serial.SerialException:
            pass

    # Check if the Arduino is found
    if arduino_found:
        print(f"Arduino found on port {port_name}")
        # Wait for 2 seconds for the serial connection to stabilize
        sleep(2)
        # Create an instance of the Kodi JSON-RPC API
        kodi = Kodi("http://192.168.29.113:8080/jsonrpc") 
        # Define a dictionary to map Arduino values to Kodi actions
        arduino_actions = {
            "6F9FA05": "up",
            "6F92AD5": "down",
            "6F91AE5": "right",
            "6F99A65": "left",
            "6F906F9": "ok",
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
        # Infinite loop to continuously read from Arduino
        while True:
            try:
                # Read data from the Arduino serial port
                value = arduino.readline().decode('utf-8').strip()
                # Check if there is any data received
                if len(value) > 0:
                    print(value.strip())
                    # Get the Kodi action corresponding to the Arduino value
                    action = arduino_actions.get(value)
                    # If the Arduino value maps to a Kodi action
                    if action:
                        # If the action is 'shutdown', call the Kodi System.Shutdown method
                        if action == "shutdown":
                            kodi.System.Shutdown()
                        else:
                            # For all other actions, call the Kodi Input.ExecuteAction method
                            kodi.Input.ExecuteAction({'action': action})
                    sleep(0.1)
                sleep(0.01)
            except serial.SerialException as e:
                print("Error communicating with Arduino:", e)
                arduino_found = False
                break
            except KodiException as e:
                print("Error communicating with Kodi:", e)
    else:
        print("Arduino not found, trying again in 5 seconds...")
        sleep(5)
