import cv2
import requests

cam = cv2.VideoCapture(0)

cv2.namedWindow("Visa task client")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("Visa task client", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27: # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32: # SPACE pressed
        img_name = "pic.png"
        cv2.imwrite(img_name, frame)

        url = "http://localhost:8000/imageUpload"
        fin = open('pic.png', 'rb')
        files = {'file': fin}
        headers = {'Content-Disposition': 'attachment', 'filename': img_name}
        try:
            r = requests.put(url, files=files, headers=headers)
            print(r.text)
        finally:
        	fin.close()

cam.release()
cv2.destroyAllWindows()