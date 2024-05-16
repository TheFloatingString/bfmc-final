import cv2
import subprocess
import time

cap = cv2.VideoCapture(0)

filename_start = 'exposure-ms-100-features-v5'
counter = 0
start = time.time()
N=1000
for i in range(N):
    ret, frame = cap.read()
    cv2.imwrite(f'data/{filename_start}_{counter}.png', frame)
    counter += 1
end = time.time()
print('avg fps: ',end='')
print(N/(end-start))
