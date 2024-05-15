import cv2
import subprocess
import time

cap = cv2.VideoCapture(0)

filename_start = 'exposure-ms-50-features'
counter = 0
start = time.time()
for i in range(500):
    ret, frame = cap.read()
    cv2.imwrite(f'data/{filename_start}_{counter}.png', frame)
    counter += 1
end = time.time()
print('avg fps: ',end='')
print(50/(end-start))
