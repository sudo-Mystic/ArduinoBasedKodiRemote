# Importing Libraries
import serial
from time import sleep
from kodijson import Kodi


arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=.1)
sleep(2)

kodi = Kodi("http://192.168.29.113:8080/jsonrpc")

while True:
 value = arduino.readline().decode('utf-8').strip()
 
 if(0 < len(value)):
  print(value.strip())
  if value == "6F9FA05":
   
   print("Up")
   kodi.Input.Up()
 
  elif value == "6F92AD5":
   
   print("Down")
   kodi.Input.Down()
  
  elif value == "6F91AE5":
  
   print("Right")
   kodi.Input.Right()
  
  elif value == "6F99A65":
  
   print("Left")
   kodi.Input.Left()
  
  elif value == "6F906F9":
  
   print("OK")
   kodi.Input.Select()
  
  elif value == "6F9708F":
 
   print("Back")
   kodi.Input.Back()

  elif value == "6F958A7":
  
   print("Vol Up")
   kodi.Input.ExecuteAction({'action': 'volumeup'})

  elif value == "6F97887":

   print("Vol Down")
   kodi.Input.ExecuteAction({'action': 'volumedown'})

  elif value == "6F908F7":
      
   print("Mute")
   kodi.Input.ExecuteAction({'action': 'mute'})
   
  elif value == "6F948B7":
      
   print("Shutdown")
   kodi.System.Shutdown()
   
  elif value == "6F9B04F":
      
   print("FullScreen")
   kodi.Input.ExecuteAction({'action': 'fullscreen'})
  
  elif value == "6F94AB5":
    
   print("Info")
   kodi.Input.ExecuteAction({'action': 'info'})
   
  elif value == "6F9C837":
    
   print("Stop")
   kodi.Input.ExecuteAction({'action': 'stop'})
  
  elif value == "6F9A857":
    
   print("PlayPause")
   kodi.Input.ExecuteAction({'action': 'playpause'})
   
  elif value == "6F9E817":
    
   print("Forward")
   kodi.Input.ExecuteAction({'action': 'fastforward'})

  elif value == "6F9C639":
    
   print("Backward")
   kodi.Input.ExecuteAction({'action': 'rewind'})
   
  sleep(0.1)
  

 sleep(0.01)
