import cv2

img1 = cv2.imread("C:/Users/Tarun Singh/OneDrive/Desktop/Open CV/sample.jpg")
img2 = cv2.imread("C:/Users/Tarun Singh/OneDrive/Desktop/Open CV/overlay.jpg")
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
blended = cv2.addWeighted(img1, 0.5, img2, 0.7, 0)
cv2.imshow('Blended Image', blended)
cv2.waitKey(0)
cv2.destroyAllWindows()
