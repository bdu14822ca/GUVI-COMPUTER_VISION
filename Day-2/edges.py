import cv2

import matplotlib.pyplot as plt
img=cv2.imread("itachi.JPG")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# threshold,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
threshold,thresh=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
edges =cv2.Canny(gray,100,300)
plt.imshow(cv2.cvtColor(edges,cv2.COLOR_BGR2RGB))
hist=cv2.calcHist(gray,[0],None,[256],[0,256])
# plt.imshow(cv2.cvtColor(thresh,cv2.COLOR_BGR2RGB))
plt.plot(hist)
plt.show()