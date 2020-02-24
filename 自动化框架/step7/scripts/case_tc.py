import unittest
# 业务类全部导入进来
from po.MemberCenter.TeacherListPage import TeacherListPage
from po.MemberCenter.TeacherList.AddTeacherPage import AddTeacherPage
# 导入共享业务（此处是登录）
from libs.Public_work import admin_login

class TestAddTeacherClass(unittest.TestCase):

    def setUp(self):
        driver = admin_login()
        # 实例化会员中心
        self.tp = TeacherListPage(driver)
        # 实例化添加教师
        self.ap = AddTeacherPage(driver)

    def tearDown(self):
        # 关闭浏览器
        self.tp.closeBrowser()

    def test_add001(self):

        # 调用会员中心业务层代码
        self.tp.optionInTeacherList()

        # 调用添加教师业务层代码
        self.ap.optionAddTeacher('13782222224', 'admin123',
                                 'a123456', 'aa@qq.com', '13782222222', 'local', 'woshinibaba')
        # 调用业务校验文本代码
        data = self.ap.optionVerifyData()
        self.assertEqual(data, '13782222224')

if __name__ == '__main__':
    unittest.main()

