import sys

import cv2
import os

print(os.getcwd())

class Get_face:

    def __init__(self):
        self.flag = True#用于判断摄像机的使用权在不在后台
        super()

    def CatchPICFromVideo(self ,path_name="the pic path", window_name="GET_FACE", camera_idx=0, catch_pic_num=100, classfile="/haarcascade_frontalface_default.xml"):
        cv2.namedWindow(window_name)

        # 视频来源，可以来自一段已存好的视频，也可以直接来自USB摄像头
        cap = cv2.VideoCapture(camera_idx)

        # 告诉OpenCV使用人脸识别分类器
        classfier = cv2.CascadeClassifier(os.getcwd() + classfile)

        # 识别出人脸后要画的边框的颜色，RGB格式

        color = (0, 255, 0)

        num = 1
        last = 1
        while cap.isOpened():
            ok, frame = cap.read()  # 读取一帧数据
            if not ok:
                break

            grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 将当前桢图像转换成灰度图像

            # 人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
            faceRects = classfier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
            if len(faceRects) > 0:  # 大于0则检测到人脸
                count =0
                for faceRect in faceRects:  # 单独框出每一张人脸
                    count = count+1
                    x, y, w, h = faceRect

                    # 将当前帧保存为图片
                    img_name = '%s/%d.jpg' % (path_name, num)#踩坑，对文件重命名时，最后一个空格也算作字符
                    image = frame[y - 10 : y + h + 10, x - 10 : x + w + 10]

                    #print(image.shape) #打印图片形状
                    
                    #存到本地
                    #cv2.imwrite(img_name, image)
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