# F55121006_Felisya Brigita Tania Wong_A

#import modul yang dibutuhkan
import cv2

# baca gambar mammogram
img = cv2.imread("mammogram.tif", 0)

# mengubah gambar jadi negatif
img_1 = 255 - img

cv2.imshow("Original Image", img)
cv2.imshow("Image Negative", img_1)

cv2.waitKey(0)
cv2.destroyALlWindows()




