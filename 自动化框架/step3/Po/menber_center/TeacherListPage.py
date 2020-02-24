
class TeacherListClass(object):
    def memberCenter(self,driver):
        # 点击会员中心
        driver.find_element_by_link_text('会员中心').click()
