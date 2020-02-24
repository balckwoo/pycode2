import unittest

from po.Common_page import Page
from po.Login_page import LoginPage
from po.MemberCenter.TeacherListPage import TeacherListPage
from po.MemberCenter.TeacherList.AddTeacherPage import AddTeacherPage

class TestAddTeacherClass(unittest.TestCase):
    def setUp(self):
        # 浏览器实例
        self.p = Page()
        # 生成浏览器驱动
        # 返回一个驱动实例
        self.driver = self.p.createDriver()

        # 登录实例
        self.lp = LoginPage()

        # 会员中心实例
        self.tp = TeacherListPage()

        # 添加教师实例
        self.ap = AddTeacherPage()

    def tearDown(self):
        # 关闭浏览器
        self.p.closeBrowser(self.driver)

    # 测试添加教师成功

    def test_add_teacher_001(self):
        # 打开浏览器
        self.p.openUrl(self.driver)

        # 调用登录业务层代码
        self.lp.optionLogin(self.driver,'admin','admin')

        # 调用会员中心业务层代码
        self.tp.optionInTeacherList(self.driver)

        # 调用添加教师业务层代码
        self.ap.optionAddTeacher(self.driver,'13782222224','admin123',
                                 'a123456','aa@qq.com','13782222222','local','woshinibaba')

        # 调用业务校验文本代码
        data = self.ap.optionVerifyData(self.driver)
        self.assertEqual(data,'13782222224')

if __name__ == '__main__':
    unittest.main(verbosity=2)