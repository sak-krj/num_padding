# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = "./sample_data/image01_c1.png"

img = cv2.imread(image_path,0)
# edges = cv2.Canny(img,100,200)
# img.show()
# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
cv2.imshow("input", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# # im_list = np.asarray(img)
# fig, ax = plt.subplots(facecolor="w")
# ax.imshow(rgb)
# plt.show()
