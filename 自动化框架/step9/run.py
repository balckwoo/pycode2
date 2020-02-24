# 用with的方式打开报告
# 导入测试报告后的运行方式
import time
import unittest
from HTMLTestReportCN import HTMLTestRunner
from config.secret import (
    email_account,
    email_pwd,
    email_host,
    email_port,
    email_to_account,
)
from libs.public_tools import (
    GetNewReport,
    send_email,
)

# 测试脚本的路径
dirpath = './scripts'

# 加载器对象 加载需要测试的脚本
discover = unittest.defaultTestLoader.discover(dirpath,pattern='*_tc.py')

# 时间格式化
currenttime = time.strftime('%y%m%d%H%M%S')

# 生成测试报告的名字以及制定路径
filedir = './Reports/'+'report'+ currenttime + '.html'

# 以二进制的方式去写入测试报告

with open(filedir,'wb') as fp:
    # 套路 测试报告状态描述
    runner = HTMLTestRunner(stream=fp,
                            title='计算器自动化测试报告',
                            description='计算器自动化测试项目详细描述',
                            tester="测试大神")
    # 执行脚本
    runner.run(discover)

# 获取最新的测试报告
f = GetNewReport()
# 发邮件函数
# send_email(user=email_account,pwd=email_pwd,host=email_host,port=email_port,to_user=email_to_account,
#                subject='自动化测试报告',body='老板这是今天的自动化报告，麻烦看看',report=f)
# print('发送邮件成功')
