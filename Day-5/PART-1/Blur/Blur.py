import cv2
import matplotlib.pyplot as plt

img=cv2.imread("blur1.jpg")
blur= cv2.blur(img,(15,15))

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()