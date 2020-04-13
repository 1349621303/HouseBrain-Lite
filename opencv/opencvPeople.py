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


            #对行人进行处理
            found_filtered = []
            count= count+1
            if count == 100000:
                count =0
            #每三涨图片找一张
            if count %3 ==0:
                found, w = self.hog.detectMultiScale(frame,
                                            winStride=(4, 4),
                                            padding=(8, 8),
                                            scale=1.25,
                                            useMeanshiftGrouping=False
                                            )
                for ri, r in enumerate(found):
                        for qi, q in enumerate(found):
                            if ri != qi and is_inside(r, q):#检测两张图片是否重叠
                                break
                            else:
                                found_filtered.append(r)
            
            faceRects=  found_filtered


            #对人脸进行处理
            if len(faceRects) > 0:  # 大于0则检测到人脸
                for faceRect in faceRects:  # 单独框出每一张人脸
                    x, y, w, h = faceRect

            
                    num += 1
                    if num > (catch_pic_num):  # 如果超过指定最大保存数量退出循环
                        break
                    print("the index of the picture " + str(num))

                    # 画出矩形框
                    if True:
                        cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)

                        # 显示当前捕捉到了多少人脸图片了，这样站在那里被拍摄时心里有个数，不用两眼一抹黑傻等着
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        cv2.putText(frame, 'num:%d' % (num), (x + 30, y + 30), font, 1, (255, 0, 255), 4)

                    # 超过指定最大保存数量结束程序
            if num > (catch_pic_num): 
                break

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