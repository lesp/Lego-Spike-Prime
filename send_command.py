import serial
from serial.tools.list_ports import comports
from time import sleep
devices = comports()
print(" I have found the following devices connected to the computer")
for i in range(len(devices)):
    print('0: ',devices[i])
for dev in devices:
    print(dev.device)
ser = serial.Serial(dev.device)
ser.write(b'\x03') #Sends CTRL + C (End of text / break) to the REPL and enables us to write code.
ser.write(b'import hub\r')
print('I have imported the hub module for you')
while True:
    ser.write(b'hub.display.show("@biglesp")\r')
    sleep(0.2)
    ser.write(b'hub.display.clear()\r')
    sleep(0.2)