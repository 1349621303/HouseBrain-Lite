
import schedule
import time

from message import *
from torchFun import *

#每天固定时间执行一次发送宿舍卫生状况
def job():
    temp = getMvsC()
    
    print(temp)
    if temp['index'] == '0':
        sendMe()
 

schedule.every().day.at("17:30").do(job)

 
while True:
    schedule.run_pending()
    time.sleep(1)
