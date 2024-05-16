import serial
from threading import Thread
import cv2
import subprocess

def record_camera():
    counter = 0
    filename_start='full-course'
    cap = cv2.VideoCapture(0)
    subprocess.run("v4l2-ctl -c auto_exposure=1", shell=True)
    subprocess.run("v4l2-ctl -c exposure_time_absolute=100", shell=True)
    while True:
        ret, frame = cap.read()
        cv2.imwrite(f'data/a-{filename_start}_{counter}.png', frame)        
        counter += 1

def controller():
    while True:
        user_str = input('ctl: ')
        sp = serial.Serial('/dev/ttyACM0',baudrate=19200)
        sp.write(f'#1:0;;\r\n'.encode())
        if user_str=='stop':
            sp.write(f'#1:0;;\r\n'.encode())
        elif user_str[0]=='m':
            vel = float(user_str[1:])
            sp.write(f'#1:{vel};;\r\n'.encode())
        elif user_str[0]=='d':
            angle = float(user_str[1:])
            sp.write(f'#2:{angle};;\r\n'.encode())

t_cam = Thread(target=record_camera)
t_ctl = Thread(target=controller)
t_cam.start()
t_ctl.start()

