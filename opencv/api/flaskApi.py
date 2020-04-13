import cv2
import numpy
import time
import flask
import os
filePath =  os.path.dirname(__file__)
print(filePath)

def getPic():
    image = cv2.imread(filePath+"/../pic.png")
    return image
    cv2.imshow('image',image)
    
    cv2.waitKey(0)
    

def getFace():
    img  = getPic()
    classfier = cv2.CascadeClassifier(filePath+ "/../haarcascade_frontalface_default.xml")
    images = []
    faceRects = classfier.detectMultiScale(img, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
    if len(faceRects) > 0:  # 大于0则检测到人脸
                count =0
                for faceRect in faceRects:  # 单独框出每一张人脸
                    x, y, w, h = faceRect

                    # 将当前帧保存为图片
                    image = img[y - 10 : y + h + 10, x - 10 : x + w + 10]
                    images.append(image)

                    #print(image.shape) #打印图片形状
                    
                    #存到本地
                    #cv2.imwrite(img_name, image)
    return len(images) != 0 , images # 返回结构和处理后的人脸数组
    

def getPeo():
    img = getPic()
    

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

    for person in found_filtered:
     
        draw_person(img, person) #依次画出框框


    return len(found_filtered) != 0 , img # 返回结构和处理后的图片




if __name__ =="__main__":
    flag, img = getFace()
    print(flag, len(img))

    

    


