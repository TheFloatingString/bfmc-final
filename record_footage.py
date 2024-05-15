import cv2
import subprocess

cap = cv2.VideoCapture(0)

filename_start = 'exposure-40-'
counter = 0
while True:
    ret, frame = cap.read()
    cv2.imwrite(f'data/lane_{counter}.png', frame)
    counter += 1
