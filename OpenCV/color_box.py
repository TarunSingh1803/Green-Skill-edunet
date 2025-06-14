import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv2.rectangle(img, (100, 100), (400, 400), (0, 255, 0), 3)
cv2.circle(img, (256, 256), 100, (0, 0, 255), -1)
cv2.putText(img, 'OpenCV!', (150, 480), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.imshow('Shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()