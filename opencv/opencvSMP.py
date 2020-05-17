#只进行树每派的数据的推送。

import sys
import numpy as np

import cv2
import os

print(os.getcwd())

 
def is_inside(o, i):
	ox, oy, ow, oh = o
	ix, iy, iw, ih = i
	return ox > ix and oy > iy and ox + ow < ix + iw and oy + oh < iy + ih
 
 
def draw_person(image, person): #画框框
	x, y, w, h = person
	cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
 


class Get_face:

    def __init__(self):
        self.flag = True#用于判断摄像机的使用权在不在后台

        #行人检测器
        self.hog = cv2.HOGDescriptor()
        self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())#设置检测器
 
        super()

    def CatchPICFromVideo(self ,path_name="the pic path", window_name="GET_FACE", camera_idx=0, catch_pic_num=100, classfile="/haarcascade_frontalface_default.xml"):
        cv2.namedWindow(window_name)

        # 视频来源，可以来自一段已存好的视频，也可以直接来自USB摄像头
        cap = cv2.VideoCapture(camera_idx)

     
        # 识别出人脸后要画的边框的颜色，RGB格式
        color = (0, 255, 0)

        num = 1
        count =0;
        last = 1
        while cap.isOpened():
            ok, frame = cap.read()  # 读取一帧数据
            if not ok:
                break
            
            cv2.imwrite('/home/lwl/Study/code/Python/flask/软件工程/整合/HouseBrain-Lite-master/App/static/img/SMPtmp.jpg', frame)


            
            # 显示图像
            cv2.imshow(window_name, frame)
            c = cv2.waitKey(10)
            if c & 0xFF == ord('q'):
                break

                # 释放摄像头并销毁所有窗口
        cap.release()
        cv2.destroyAllWindows()

    def sendMessage(self, name="某人"):
        pritn('发送消息给用户有人来啦'+ name)    




if __name__ == '__main__':
    c = Get_face()
    c.CatchPICFromVideo()