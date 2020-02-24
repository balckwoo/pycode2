from po.Common_page import Page
from po.Login_page import LoginPage

# 共享业务登录
def admin_login():
    # 因为LoginPage继承了Page所以直接可以调用Page方法
    obj = LoginPage()
    obj.openUrl()
    obj.optionLogin('admin','admin')
    return obj.driver



if __name__ == '__main__':
    admin_login()
