import os

# 测试用例地址
case_local = os.path.abspath(os.path.join(os.path.dirname(__file__), '../cases/EDU_V1.0测试用例.xlsx'))
# 测试需求
login_requirement = 'Login'
# 邮件账号密码
email_account = ''
email_pwd = ''
email_host = 'smtp.163.com'
email_port = '465'
email_to_account = ''
email_to_account2 = ''
email_to_account_list = [email_account, email_to_account2]
# 判断测试全局用例是否执行
# 1执行，2不执行
case_stuff = 2
# 测试地址
test_edu_url = 'http://localhost/admin.php?m=mgr/admin.login'
