import unittest
# 业务类全部导入进来
from po.MemberCenter.StudentListPage import StudentListPage
from po.MemberCenter.StudentList.AddStudentPage import AddStudentPage
# 导入共享业务（此处是登录）
from libs.public_work import admin_login
from libs.public_tools import read_mysql_data

class TestAddTeacherClass(unittest.TestCase):

    def setUp(self):
        driver = admin_login()

        self.tp = StudentListPage(driver)
        # 实例化添加学生
        self.ap = AddStudentPage(driver)

    def tearDown(self):
        # 关闭浏览器
        self.tp.closeBrowser()

    def test_add_student_001(self):
        # 调用会员中心业务层代码
        self.tp.optionInStudentlist()

        # 调用学生业务层代码
        self.ap.optionAddStudent('13811112222', 'test007',
                              '123456', 1, '全部开放', '南通大学', 'xiaoxin@163.com','13811112222')

        ## 校验两层
        # 针对ui页面的校验（1）
        # self.assertEqual(data,'13811112222')
        # 使用数据库去进行校验（2）
        select_sql = 'select * from xsmart_users where username= test007'

        data = read_mysql_data(sql=select_sql)
        self.assertIn(data,'test007')

if __name__ == '__main__':
    unittest.main()

