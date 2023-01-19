import serial

from time import sleep

from kodijson import Kodi

# Create an instance of the Arduino serial port 

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=.1)

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

