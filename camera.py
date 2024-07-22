from picamera2 import Picamera2 as picam
from time import sleep
import cv2

webcam = picam()
webcam.start()

frame = webcam.capture_array()

cv2.imshow('Teste', frame)
cv2.waitKey(10)
sleep(10)

cv2.destroyAllWindows()
