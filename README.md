1. Download the ArduinoBasedKodiRemote repository to your computer, and make sure to install all necessary dependencies.

2 Open the IRTransmitter sketch in the Arduino IDE and upload it to the Arduino board, connecting the IR module to the appropriate pins (such as Vcc to 3.3v, GND to GND, and SIG to Pin 8 for an Arduino UNO. If you're using a different model, make sure to adjust the connections accordingly.

3. In order for the remote to function properly, run the KodiRemote.py script in the background. This script receives the hex codes from the IR remote and sends the corresponding commands to Kodi.

4. Make sure to update the IP address of your Kodi device and the hex codes according to your IR remote in the KodiRemote.py script for it to work properly with your setup.

Note:- Tried to optimise the code little bit , dont know if it work fine or not , you can check it by using OptimisedDecoder.py
