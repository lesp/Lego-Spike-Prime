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

# Command to send text to the LED matrix
def display(text):
    command = 'hub.display.show('text')\r'
    ser.write(b(command))