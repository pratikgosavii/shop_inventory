import cv2
import numpy as np
from PIL import Image

# Load your two images
image1 = cv2.imread('demo1.jpg')
image2 = cv2.imread('demo2.jpg')

# Convert the images to grayscale for comparison (optional but often useful)
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Calculate the absolute difference between the two images
difference = cv2.absdiff(gray1, gray2)

# Define a threshold to identify differences (adjust as needed)
threshold = 30

# Find regions where the difference exceeds the threshold
_, thresholded = cv2.threshold(difference, threshold, 255, cv2.THRESH_BINARY)

# Find contours in the thresholded image
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a copy of the original images to draw circles on
result_image1 = image1.copy()
result_image2 = image2.copy()

# Define the padding around the differences
padding = 5

# Loop through the detected contours and draw circles around them
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(result_image1, (x - padding, y - padding), (x + w + padding, y + h + padding), (0, 0, 255), 2)
    cv2.rectangle(result_image2, (x - padding, y - padding), (x + w + padding, y + h + padding), (0, 0, 255), 2)

# Save or display the resulting images
cv2.imwrite('demo11.jpg', result_image1)
cv2.imwrite('demo22.jpg', result_image2)

# Convert images to PIL format for easier display
result_image1_pil = Image.fromarray(cv2.cvtColor(result_image1, cv2.COLOR_BGR2RGB))
result_image2_pil = Image.fromarray(cv2.cvtColor(result_image2, cv2.COLOR_BGR2RGB))

# Display the images (optional)
result_image1_pil.show()
result_image2_pil.show()
