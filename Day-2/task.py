import cv2
import matplotlib.pyplot as plt

img=cv2.imread("images.jpg")
blur= cv2.blur(img,(15,15))
# gaussian=cv2.GaussianBlur(gaussian,(15,15),0)
# median=cv2.medianBlur(img,3)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()