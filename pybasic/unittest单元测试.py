# import unittest
# # 测试用例
# unittest.TestCase
#
# # 测试集（套件）
# unittest.TestSuite
#
# # 运行方式的一种
# unittest.main()
#
# # 跳过测试用例
# unittest.skipUnless()
# unittest.skip()
# unittest.skipIf()
#
# # 生成一个runner执行对象（实例化）
# unittest.TextTestRunner()
#
# # 加载器对象（加载测试用例对象）
# unittest.defaultTestLoader()
#
# # 校验对象
# unittest.TestCase.assertEqual()
# unittest.TestCase.assertIn()

class CalcClass(object):
    # 加法
    def add(self, num1, num2):
        return num1 + num2

    # 乘法
    def mul(self, num1, num2):
        return num1 * num2

    # 除法
    def div(self, num1, num2):
        return num1 / num2

    # 减法
    def jianfa(self, num1, num2):
        return num1 - num2

# 了解unittest基本用法
# import unittest
# # unittest的使用
# # 继承的是Unittest模块中的TestCase类
# class TestClass(unittest.TestCase):
#     # unittest中的测试用例方法必须以test开头
#     def test_add(self):
#         calc = CalcClass()
#         result = calc.add(1,2)
#         # 校验方式
#         # result测试的结果
#         # 后面的3是预期结果
#         self.assertEqual(result,4)
# if __name__ == '__main__':
#     # unittest的运行方式
#     # 控制台输出三种结果
#     # .代表通过
#     # F代表测试失败
#     # E代表程序出错
#     unittest.main()

# 2.了解unittest执行顺序，verbosity参数的概念
# import unittest
# # Unitttest的使用
# # 继承的是Unittest模块中的TestCase类
# class TestClass(unittest.TestCase):
#     # unittest中的测试用例的方法必须以test开头
#     # 运行的顺序test后面的字段转成ascii编码
#     # 根据编码的大小来决定顺序
#     def test_add(self):
#         calc = CalcClass()
#         result = calc.add(1,3)
#         # 校验方式
#         # result测试的结果
#         # 后面的3是预期结果
#         self.assertEqual(result,4)
#
#     def test_jianfa(self):
#         calc = CalcClass()
#         result = calc.jianfa(4,1)
#         # 校验方式
#         #         # result测试的结果
#         #         # 后面的3是预期结果
#         self.assertEqual(result,34)
#
# if __name__ == '__main__':
# # # unittest的运行方式
# #     # 控制台输出三种结果
# #     # .代表通过
# #     # F 代表测试失败
# #     # E 代表程序出错
# #     # s 代表跳过测试用例
# #     # verbosity 参数
# #     0代表概述
# #     1代表简述
# #     2代表详细描述
# #     unittest.main(verbosity=0)
# #     unittest.main(verbosity=1)
#     unittest.main(verbosity=2)

# 3.了解Unittest setup teardown概念
# 了解测试集的运行方式
# import unittest
# # Unitttest的使用
# # Unitttest的使用
# # 继承的是Unittest模块中的TestCase类
# class TestAddclass(unittest.TestCase):
#     # 每条测试用例执行之前都会首先去运行
#     def setUp(self):
#         self.calc = CalcClass()
#     # unittest中的测试用例的方法必须以test开头
#     def test_add(self):
#         result = self.calc.add(1,2)
#         # 校验方式
#         #         # result测试的结果
#         #         # 后面的3是预期结果
#         self.assertEqual(result, 3)
#
#     def test_add2(self):
#         result = self.calc.add(-1,-2)
#         # result测试的结果
#         # 后面的3是预期结果
#         self.assertEqual(result, -3)
#
#     def test_add3(self):
#         result = self.calc.add(5,4)
# #       校验方式
# #         # result测试的结果
# #         # 后面的3是预期结果
#         self.assertEqual(result, 9)
#     # 每条测试用例执行之后都会首先去运行
#     def tearDown(self):
#         ...
# if __name__ == '__main__':
# # # unittest的运行方式
# #     # 控制台输出三种结果
# #     # .代表通过
# #     # F 代表测试失败
# #     # E 代表程序出错
# #
# #     ##执行方式
# #     # 执行方式一
# #     # main执行方式 执行全部测试用例
# #     unittest.main()
# # 执行方式二
# #     # 实例化测试集
# #     # 实例化一个测试集（测试套件）对象
#     suite = unittest.TestSuite()
#     # 添加测试用例到测试集（测试套件）对象
#     suite.addTest(TestAddclass('test_add'))
#     suite.addTest(TestAddclass('test_add2'))
#     # 生成一个runner对象运行测试集
#     runner = unittest.TextTestRunner()
#     # 运行测试集（测试套件）
#     runner.run(suite)

# 4.前置条件的种类有setup teardown setUpClass tearDownClass
# import unittest
# class TestAddclass(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         print('测试加法类首先执行这里')
#     @classmethod
#     def tearDownClass(cls):
#         print('测试加法类最后执行这里')
#
#     # 每条测试用例执行之前都会首先去运行
#     def setUp(self):
#         print('执行测试用例之前先知执行这里')
#     def test_a(self):
#         print('这是第一条测试用例')
#
#     def test_b(self):
#         print('这是第二条测试用例')
#
#     def tearDown(self):
#         print('执行测试用例之后只执行这里')
# if __name__ == '__main__':
#     unittest.main()

# 5.使用三种装饰器来不执行测试用例
import unittest
condition_var = True
# 定义一个配置变量
class TestAddclass(unittest.TestCase):
    # 每条用例执行之前都会首先去运行
    def setUp(self):
        self.calc = CalcClass()
    # unittest中的测试用例的方法必须以test开头
    # nothing就是传参的reason
    # condition(条件)不是true的时候会跳过执行
    @unittest.skipUnless(condition_var!=True,'nothing')
    def test_add(self):
        result = self.calc.add(1,2)
        # 校验方式
        # result测试的结果
        # 后面的3是预期结果
        self.assertEqual(result, 3)
        # unittest中的测试用例的方法必须以test开头
        #     # nothing 就是传参的reason
        #     # condition(条件)为true的时候会跳过执行
    @unittest.skipIf(condition_var==True,'nothing')
    def test_add2(self):
        result = self.calc.add(-1, -2)
        #         # 校验方式
        #         # result测试的结果
        #         # 后面的3是预期结果
        self.assertEqual(result, -3)

    @unittest.skip('nothing')
    def test_add3(self):
        result = self.calc.add(5,4)
#         # 校验方式
#         # result测试的结果
#         # 后面的3是预期结果
        self.assertEqual(result, 9)
    def test_add4(self):
        result = self.calc.add(8, 2)
#         # 校验方式
#         # result测试的结果
#         # 后面的3是预期结果
        self.assertEqual(result, 10)
#
    def test_add5(self):
        result = self.calc.add(8, 3)
#         # 校验方式
#         # result测试的结果
#         # 后面的3是预期结果
        self.assertEqual(result, 11)
#
if __name__ == '__main__':
    unittest.main(verbosity=2)

##################################
# 6.unittest运行的三种方式
##################################
# unittest.main()运行当前模块全部
# unittest.suite()运行加载到测试用例的测试集
# unittest discover 运行加载对象的全部（包文件）