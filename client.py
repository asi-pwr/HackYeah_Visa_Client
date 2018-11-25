import json

import cv2
import requests
import random

cam = cv2.VideoCapture(0)

cv2.namedWindow("Visa task client")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("Visa task client", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k % 256 == 27:  # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:  # SPACE pressed
        img_name = "pic.png"
        cv2.imwrite(img_name, frame)

        url = "http://localhost:5000/uploader"
        fin = open('pic.png', 'rb')

        json_data = {'value': str(random.randint(1, 100))}
        files = [
            ('file', ('pic.png', open('pic.png', 'rb'), 'application/octet')),
            ('data', ('data', json.dumps(json_data), 'application/json')),
        ]

        try:
            response = requests.post(url, files=files)
            print(response.text)
        finally:
            fin.close()

cam.release()
cv2.destroyAllWindows()
