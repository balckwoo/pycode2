
import unittest
from Po.CommonPage import CommonPageClass
from Po.LoginPage import LoginPageClass
from Po.menber_center.TeacherListPage import TeacherListClass
from Po.menber_center.teacher_list.AddTeacher import AddTeacherClass


class TestTeacherClass(unittest.TestCase):
    def setup(self):
        self.cp = CommonPageClass()
        self.lp = LoginPageClass()
        self.tc = TeacherListClass()
        self.at = AddTeacherClass()

    def tearDown(self):
        self.driver.quit()

    # 第一条测试用例
    def test_success_001(self):
        self.driver = self.cp.openUrl()
        self.lp.login(self.driver)
        self.tc.memberCenter(self.driver)
        self.at.optionTeacher(self.driver)
        self.at.sendTeacherData(self.driver)
        result = self.at.verifyData(self.driver)
        self.assertEqual(result,'18797766769')

if __name__ == '__main__':
    unittest.main()


#1.对业务进行了模块分层（会员中心父层，教师列表，学生列表子层）
#2.对原本是函数的业务模块，进行了类的区分
#3.在测试模块中，实例化全部业务类，拼接校验

