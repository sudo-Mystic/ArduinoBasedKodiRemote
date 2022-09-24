# ArduinoBasedKodiRemote
Kodi Remote based on arduino uno , which utilises pyserial to communicate with arduino connect 

TO INSTALL IT

1: Copy the repo to your computer, make sure to download all dependencies
2: Upload the IRTransmitter Sketch to the Arduino , (i am using Arduino UNO so i connected my ir module according to it [vcc -> 3.3v , gnd -> gnd , sig -> Pin 8] update if you're using different model)
3: this remote the KodiRemote.py script to be running in background to work , this python script recieves the hex codes of our ir remote then according to it sends commands to kodi

Update variable according to your setup
