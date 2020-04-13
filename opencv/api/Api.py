from flask import Flask, request
import base64
from flask_cors import CORS
import json
import os,base64 
import torch
from load_data import *
import cv2
from picPro import *

app = Flask(__name__)
CORS(app, resources=r'/*')

@app.route('/peo',methods=['POST', 'GET'])
def hello_world():
    if request.method == "GET":
        flag, img = getPeo()
        cv2.imwrite("../../App/static/img/peo.png", img)


  


                    


   
        

        return 'ok'
    else:
        return 'falile'



if __name__ == '__main__':
    app.run(host='127.0.0.1', port='3001')


