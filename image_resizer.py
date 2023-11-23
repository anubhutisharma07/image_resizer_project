
import cv2


# Configurable Parameters
scale_percent = 50


image = cv2.imread("jujutsu-kaisen.jpg", cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", image)

cv2.waitKey(0)


# Percent by which the image is resized
scale_percent = 50

# Calculate the 50 percent of original dimensions
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)

# Dsize
dsize = (width, height)

# Resize image
output = cv2.resize(image, dsize)

cv2.imwrite("new_image.jpg", output)

