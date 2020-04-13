
import cv2
import numpy as np
 
 
def is_inside(o, i):
	ox, oy, ow, oh = o
	ix, iy, iw, ih = i
	return ox > ix and oy > iy and ox + ow < ix + iw and oy + oh < iy + ih
 
 
def draw_person(image, person): #画框框
	x, y, w, h = person
	cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
 
 
img = cv2.imread('test.jpg')

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())#设置检测器
 
found, w = hog.detectMultiScale(img)
 
found_filtered = []
 
for ri, r in enumerate(found):
	for qi, q in enumerate(found):
		if ri != qi and is_inside(r, q):#检测两张图片是否重叠
			break
		else:
			found_filtered.append(r)

print(len(found_filtered))
for person in found_filtered:
	print("asfsdfasdfaaf")
	print(person)
	draw_person(img, person) #依次画出框框
 
cv2.imshow('people detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
