import cv2
import requests
import base64
import requests

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
ret, buffer_ = cv2.imencode('.jpg', frame)
jpg_txt = base64.b64encode(buffer_).decode()
cap.release()
print(type(jpg_txt))
print(frame.shape)
print(len(jpg_txt))
headers={'Content-Type':'application/json'}
resp = requests.post('http://10.69.158.153:5000/api/frame', headers=headers, data={'img':jpg_txt})
print(jpg_txt)
print(resp)
