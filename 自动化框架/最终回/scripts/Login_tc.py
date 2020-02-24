# coding:utf-8
import sys
import unittest
from config.Secrect import (
    case_local,
    login_requirement,
    case_stuff,
)
from po.LoginPage import LoginPage
from libs.Tools import getTestData


class LoginTest(unittest.TestCase):
    '''测试登录功能'''

    def setUp(self):
        # 不需要共享登陆，因为校验的是登陆功能
        self.obj = LoginPage()
        self.obj.open_url()

    def tearDown(self):
        self.obj.close_broser()

    def test_login_success_001(self):
        '''登录成功验证'''
        # casename:获取类方法的名字，与xlsx测试用例一致
        # case_local:需要执行的测试用例的路径
        # login_requirement: 需要执行的需求
        casename = sys._getframe().f_code.co_name
        data = getTestData(case_local, login_requirement, casename)
        self.obj.login_operator(data[0], data[1])
        r = self.obj.get_success_msg()
        self.assertEqual(r, 'admin')

    def test_username_empty_login_002(self):
        '''验证账号为空'''
        self.obj.login_operator('', 'admin')
        r = self.obj.get_username_error_msg()
        self.assertEqual(r, '帐号或密码不能为空')

    # 决定用例是否执行
    @unittest.skipIf(case_stuff != 1,'')
    def test_error_login_003(self):
        '''验证正确账号错误密码'''
        self.obj.login_operator('admin', '123')
        r = self.obj.get_password_error_msg()
        self.assertEqual(r, '密码错误')


if __name__ == '__main__':
    unittest.main(verbosity=2)
