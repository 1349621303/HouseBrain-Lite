from flaskApi import *
from load_data import *
import torch

def getMvsC():
    print(filePath)

    img = getPic()
       # cpu进行单个测试
    if True:
        device = torch.device('cpu')
        model = torch.load(filePath+'/mess_clean_model.h5', map_location=device)

        image = img

        print(model.preImg(image))

def getFaceRco():
    flag,imgs = getFace()
    if flag:
        device = torch.device('cpu')

        image = imgs[0]
        model = torch.load(filePath+'/model.h5', map_location=device)


        index, probability = pre(model, image)
        person = {"index":-1, "prob":0}
        person['index']=str(index)
        person["prob"] = str(probability)
        return person





if __name__== "__main__":
    temp = getMvsC()
    print(temp)
    ans  = getFaceRco()
    print(ans)

    