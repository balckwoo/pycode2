import os
import yagmail
import logging
import time
import pymysql
from config.secret import (
    sql_db,
    sql_host,
    sql_port,
    sql_pwd,
    sql_user,
    select_sql,
)
# 发送邮件
def send_email(user, pwd, port, body, subject, report, to_user, host='smtp.163.com', ):
    '''
    :param user:
    :param pwd:
    :param port:
    :param body:
    :param subject:
    :param report:
    :param to_user: 接受者账号，默认是字符串，如果传多个请用列表的方式传递
    :param host:
    :return:
    '''
    # 生成发送对象
    send = yagmail.SMTP(user=user, password=pwd, host=host, port=port)
    if type(to_user) is list:
        # 发送邮件
        send.send(to=to_user, subject=subject, contents=[body, report])
        flag = '发送给批量用户成功'
    elif type(to_user) is str:
        # 发送邮件
        send.send(to=to_user, subject=subject, contents=[body, report])
        flag = '发送给单个用户成功'
    else:
        flag = '发送数据错误'
    return flag

# 数据库的操作
def read_mysql_data(sql,host=sql_host,port=sql_port,user=sql_user,pwd=sql_pwd,db=sql_db):
    """
    :param host:
    :param port:
    :param user:
    :param pwd:
    :param db:
    :param sql:
    :return:
    """
    try:
        # 建立sql连接对象
        conn = pymysql.connect(host=host, port=port, user=user, password=pwd, db=db)
        # 生成游标对象
        cur = conn.cursor()
        # 执行sql语句
        cur.execute(sql)
        # 关闭游标
        cur.close()
        # 关闭数据库
        conn.close()
        # 查询sql结果
        data = cur.fetchone()
        return data
    except BaseException as msg:
        print(msg,'数据库读写错误')

FD = "./reports"

def GetNewReport(FileDir=FD):
    # 打印目录所在所有文件名（列表对象）
    l = os.listdir(FileDir)
    # 按时间排序
    l.sort(key=lambda fn: os.path.getmtime(FileDir + "\\" + fn))
    # 获取最新的文件保存到file_new
    f = os.path.join(FileDir, l[-1])
    return f

# 当前文件路径
cur_path = os.path.dirname(os.path.realpath(__file__))
# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# 类名称：InsertLog
# 类的目的：写日志
# 假设：无
# 影响：无
# 输入：无
# 返回值：无
# 创建者：你爸爸
# 创建时间：2019/05/18
# 修改者：
# 修改原因：
# 修改时间:
# -------------------------------------------------------------------------------

# log_path是存放日志的路径
log_path = os.path.join(os.path.dirname(cur_path), 'log')
# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path):
    os.mkdir(log_path)


class InsertLog():
    def __init__(self):
        # 文件的命名
        self.logname = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter(
            '[%(asctime)s - %(funcName)s line: %(lineno)3d] - %(levelname)s: %(message)s')

    def __console(self, level, message,*args):
        # 创建一个FileHandler，用于写到本地
        # fh = logging.FileHandler(self.logname, 'a')  # 追加模式  这个是python2的
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')  # 这个是python3的
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message,*args):
        self.__console('debug', message,args)

    def info(self, message,*args):
        self.__console('info', message,args)

    def warning(self, message,*args):
        self.__console('warning', message,args)

    def error(self, message,*args):
        self.__console('error', message,args)

if __name__ == '__main__':
    read_mysql_data(1)