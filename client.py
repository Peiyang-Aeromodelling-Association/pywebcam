import cv2
import numpy as np
import requests

print("requesting video feed...")

url = r' http://192.168.43.4:5000/video_feed'

stream = requests.get(url, stream=True)

while True:
    video_bytes = bytes()
    for chunk in stream.iter_content(chunk_size=1024):
        video_bytes += chunk
        a = video_bytes.find(b'\xff\xd8')  # start code
        b = video_bytes.find(b'\xff\xd9')  # end code
        if a != -1 and b != -1:  # if both are found
            jpg = video_bytes[a:b + 2]  # actual image
            video_bytes = video_bytes[b + 2:]  # other information
            image = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
            cv2.imshow('image', image)
            if cv2.waitKey(1) == 27:  # if user hit esc
                exit(0)
