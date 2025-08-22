import cv2
import numpy as np  
import matplotlib.pyplot as plt  
img =cv2.imread("rBen.webp")
print(img.shape)

cv2.rectangle(img,(30,70),(210,210),(255,0,0),2)

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()