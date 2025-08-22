import cv2

import matplotlib.pyplot as plt
import numpy as np
img =cv2.imread("itachi1.png")
rows,cols=img.shape[:2]
(h,w)=img.shape[:2]
print(img.shape)

M=np.float32([[1,0,-500],[0,1,10]])
translate=cv2.warpAffine(img,M,(cols,rows))

RM=cv2.getRotationMatrix2D((w//2,h//2),45,1)
rotated=cv2.warpAffine(img,RM,(w,h))
cv2.rectangle(img,(800,700),(900,900),(255,0,0),2)

cv2.circle(img,(900,900),500,(0,220,444),6)

# plt.imshow(cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB))
# plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.imshow(cv2.cvtColor(translate,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()