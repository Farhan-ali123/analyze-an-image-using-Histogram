import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('C:\\Users\\user\\Desktop\\newp\\venv\\resources\\moon.jfif', cv2.IMREAD_GRAYSCALE)

# Calculate the histogram
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

# Plot the histogram
plt.plot(histogram, color='black')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('Image Histogram')
plt.show()
