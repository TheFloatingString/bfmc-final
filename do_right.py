import serial
import time

sp = serial.Serial('/dev/ttyACM0', baudrate=19200)
sp.write(f'#1:0;;\r\n'.encode())
sp.write(f'#2:0;;\r\n'.encode())
time.sleep(3)
sp.write(f'#2:15;;\r\n'.encode())
sp.write(f'#1:15;;\r\n'.encode())
time.sleep(6)
sp.write(f'#1:0;;\r\n'.encode())
