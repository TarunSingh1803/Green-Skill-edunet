import cv2
# Read the image
img = cv2.imread("C:/Users/Tarun Singh/OneDrive/Desktop/Open CV/sample.jpg")  # Replace 'image.jpg' with your image path

# Check if image was loaded successfully
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Display the image
    cv2.imshow('Image', img)

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
