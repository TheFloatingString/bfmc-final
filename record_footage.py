import cv2
cap = cv2.VideoCapture(0)

filename_start = 'slightly-slanted-angle'
counter = 0
while True:
    ret, frame = cap.read()
    cv2.imwrite(f'data/lane_{counter}.png', frame)
    counter += 1
