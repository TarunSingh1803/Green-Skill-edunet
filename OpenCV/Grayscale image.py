import cv2

img = cv2.imread("C:/Users/Tarun Singh/OneDrive/Desktop/sample.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()