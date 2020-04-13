- api.py负责使用flask暴露web接口
- message.py有发送邮件的模块
- load_data.py有数据处理函数
- pic_pro.py有处理图片的函数，粗加工
- torchFun.py有深度学习模型加载预测函数
- plan.py有计时函数，每天固定时间执行发送邮件


项目运行时，需要运行
api.py
plan.py
上一级目录的gei——pic.py