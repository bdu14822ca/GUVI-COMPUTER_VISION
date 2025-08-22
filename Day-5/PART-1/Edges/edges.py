import cv2
import matplotlib.pyplot as plt

img=cv2.imread("etree.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,100,300)
threshold,thread= cv2.threshold(gray,0,255,cv2.THRESH_BINARY)
plt.imshow(cv2.cvtColor(edges,cv2.COLOR_BGR2RGB))
plt.show()