
import schedule
import time

from message import *

#每天固定时间执行一次发送宿舍卫生状况
def job():
    print("I'm working...")
 

schedule.every().day.at("10:30").do(job)

 
while True:
    schedule.run_pending()
    time.sleep(1)
