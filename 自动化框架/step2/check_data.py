from step2 import sciripts_test
import unittest
class TestTeacher(unittest.TestCase):
    # 第一条测试用例
    def test_success_001(self):
        driver = sciripts_test.openUrl()
        sciripts_test.login(driver)
        sciripts_test.memberCenter(driver)
        sciripts_test.optionTeacher(driver)
        sciripts_test.addTeacher(driver)
        v_data = sciripts_test.verifyData(driver)
        self.assertEqual(v_data,'18797763626')
if __name__ == '__main__':
    unittest.main()


