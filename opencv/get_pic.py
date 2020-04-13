import sys

import cv2
import os

import time
class Get_face:

    def __init__(self):
        self.flag = True#用于判断摄像机的使用权在不在后台
        super()

    def CatchPICFromVideo(self , window_name="GET_FACE", camera_idx=0, sleepT=2):
        cv2.namedWindow(window_name)

        # 视频来源，可以来自一段已存好的视频，也可以直接来自USB摄像头
        cap = cv2.VideoCapture(camera_idx)

      


        num = 1
        last = 1
        while cap.isOpened():
            ok, frame = cap.read()  # 读取一帧数据
            if not ok:
                break

            grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 将当前桢图像转换成灰度图像

          
                #存到本地
            cv2.imwrite("pic.png", frame)
            time.sleep(sleepT)

            num = num+1
            print("the index of the picture " + str(num))



        # 释放摄像头并销毁所有窗口
        cap.release()
        cv2.destroyAllWindows()

    def sendMessage(self, name="某人"):
        pritn('发送消息给用户有人来啦'+ name)    




if __name__ == '__main__':
    c = Get_face()
    c.CatchPICFromVideo(sleepT=1)