#这是一个用来载入数据的程序

import torch as torch
import torch.nn as nn

import PIL.Image as Image
import os

import time
import json
import os

import cv2
import numpy as np

IMAGE_SIZE = 64

class CNN(nn.Module):
    def __init__(self, num_classes):
        super(CNN, self).__init__()
        self.conv1=nn.Sequential(
            nn.Conv2d(          #(3,64,64)
                in_channels=3,
                out_channels=16,
                kernel_size=5,
                stride=1,
                padding=2   #padding=(kernelsize-stride)/2
            ),#(16,64,64)
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)#(16,32,32)
 
        )
        
        self.normal = nn.BatchNorm2d(16) # 数据归一化,防止过拟合

        self.conv2=nn.Sequential(#(16,32,32)
            nn.Conv2d(16,32,5,1,2),#(32,32,32)
            nn.ReLU(),#(32,32,32)
            nn.MaxPool2d(2)#(32,16,16)
        )
        self.dropout = nn.Dropout(0.1)


        #分类器
        self.classifier = nn.Sequential(
            nn.Linear(32*16*16,1000),
            nn.ReLU(inplace=True),
            nn.Dropout(0.2),

            nn.Linear(1000,100),
            nn.ReLU(True),
            nn.Dropout(0.2),

            nn.Linear(100,num_classes)
        )

    #定义前向传播过程，过程名字不可更改，因为这是重写父类的方法
    def forward(self,x):
        x = self.conv1( x )
        x = self.conv2( x ) #(batch,32,16,16)
        x=x.view(x.size(0),-1) #(batch,32*7*7)
        output=self.classifier(x)
        return output


    def preImg(self, img):
            image = resize_image(img, IMAGE_SIZE, IMAGE_SIZE)
            image = np.array(image)
            image = image/256
            image= torch.tensor(image).view(-1, 3,64,64).float()
            ans = self.forward(image)
            index = ans.argmax()
            
            index = index.numpy()
            ans = ans.view(ans.size(1))
            pro = ans.detach().numpy()[index]
            #print(ans)

            return index, pro
    
    def preNum(self, img):
            device = torch.device('cpu')
            ans = self.forward(img)
            ans = ans.to(device)
            index = ans.argmax()
            
            index = index.numpy()
            ans = ans.view(ans.size(1))
            pro = ans.detach().numpy()[index]
            #print(ans)

            return index, pro


# 按照指定图像大小调整尺寸
def resize_image(image, height=IMAGE_SIZE, width=IMAGE_SIZE):
    top, bottom, left, right = (0, 0, 0, 0)

    # 获取图像尺寸
    h, w, _ = image.shape  # (237, 237, 3)

    # 对于长宽不相等的图片，找到最长的一边
    longest_edge = min(h, w)

    # 计算短边需要增加多上像素宽度使其与长边等长
    if h < longest_edge:
        dh = longest_edge - h
        top = dh // 2
        bottom = dh - top
    elif w < longest_edge:
        dw = longest_edge - w
        left = dw // 2
        right = dw - left
    else:
        pass

        # RGB颜色
    BLACK = [0, 0, 0]

    # 边缘填充 0 给图像增加边界，是图片长、宽等长，cv2.BORDER_CONSTANT指定边界颜色由value指定
    constant = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=BLACK)

    # 调整图像大小并返回
    return cv2.resize(constant, (height, width))





def read_path(path_name, images, labels):
    # global images
    # global labels
  
    for dir_item in os.listdir(path_name):

        # 从初始路径开始叠加，合并成可识别的操作路径
        full_path = os.path.abspath(os.path.join(path_name, dir_item))

        if os.path.isdir(full_path):  # 如果是文件夹，继续递归调用
            read_path(full_path, images, labels)
        else:  # 文件
            if dir_item.endswith('.png'):

                #进行数据增强
                im  = Image.open(full_path)

                #大小随机截取
                ims =[]

                for i in range(2):
                    new_img = transforms.RandomCrop(200)(im) # 随机裁剪出100x100的区域
                    for j in range(2):
                        #生成随机数作为int
                        a = np.random.randint(0,360)

                        new_img1 = transforms.RandomRotation(a)(new_img)  
                        new_img1= cv2.cvtColor(np.asarray(new_img1),cv2.COLOR_RGB2BGR)   #随机旋转45度
                        #ims.append(new_img1)
                        
                        image = new_img1
                        image = cv2.imread(full_path)
                        image = resize_image(image, IMAGE_SIZE, IMAGE_SIZE)

                        # 放开这个代码，可以看到resize_image()函数的实际调用效果
                        # cv2.imwrite('1.jpg', image)

                        images.append(image)
                        labels.append(path_name.split('\\')[-1])

    return images, labels


# 从指定路径读取训练数据
def load_dataset(path_name, images, labels):
    images, labels = read_path(path_name, images, labels)


    # 将输入的所有图片转成四维数组，尺寸为(图片数量*IMAGE_SIZE*IMAGE_SIZE*3)
    # 图片为64 * 64像素,一个像素3个颜色值(RGB)
    images = np.array(images)


    labels = np.array(labels)
    labels= change_lable(labels) #python串惨默认是引用    

    return images, labels


def change_lable(lable,max=2, me="me"):
    temp = np.zeros((len(lable), max), dtype=np.int)
    for index,item in enumerate(lable):
   
        if item.endswith('clean'):
            temp[index][0] = 1
        elif item.endswith('messy'):
            temp[index][1] = 1
    # print(temp)
    return temp
    print(lable.shape)



def pre(model, img):
        image = resize_image(img, IMAGE_SIZE, IMAGE_SIZE)
        image = np.array(image)
        image = image/256
        image= torch.tensor(image).view(-1, 3,64,64).float()
        ans = model(image)
        index = ans.argmax()
        
        index = index.numpy()
        ans = ans.view(ans.size(1))
        pro = ans.detach().numpy()[index]
        #print(ans)

        return index, pro

 
def is_inside(o, i):
	ox, oy, ow, oh = o
	ix, iy, iw, ih = i
	return ox > ix and oy > iy and ox + ow < ix + iw and oy + oh < iy + ih
 
def draw_person(image, person): #画框框
	x, y, w, h = person
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)
 


if __name__ == '__main__':
    # 读取训练数据
    images = []
    labels = []
    images, labels= load_dataset("/home/lwl/code/python/pytorch/mess_vs_clean/images/train", images, labels)
    images= images/256
    print(images.shape, labels.shape)


    t = torch.tensor(labels)
        
    print(t.size())

    