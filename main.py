import cv2
import pytesseract
from imutils.video import WebcamVideoStream
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=100,
                help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=-1,
                help="Whether or not frames should be displayed")
args = vars(ap.parse_args())

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Sean\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
# img = cv2.imread('fourplusfive.png')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#problem = pytesseract.image_to_string(img)
# print(eval(problem))
#
# cv2.imshow('Image', img)
# cv2.waitKey(0)

vs = WebcamVideoStream(src=0).start()
while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=1080)
    problem = pytesseract.image_to_string(frame)
    cv2.imshow("Frame", frame)
    if args["display"] > 0:
        cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
