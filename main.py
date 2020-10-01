import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Sean\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('fourplusfive.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
problem = pytesseract.image_to_string(img)
print(eval(problem))

cv2.imshow('Image', img)
cv2.waitKey(0)
