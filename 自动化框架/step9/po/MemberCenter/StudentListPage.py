from po.Common_page import Page
from selenium.webdriver.common.by import By


class StudentListPage(Page):
    """学生列表页面"""

    # 对象层
    btn_menbercenter_loc = (By.XPATH, '//*[@id="header"]/ul/li[3]/a')
    lnk_studentlist_loc = (By.LINK_TEXT, '学生列表')
    iframe_main_loc = (By.ID, 'mainframe')
    btn_addstu_loc = (By.XPATH,'/html/body/div[2]/h3/a[2]/span')

    # 操作层
    # 点击会员中心
    def clickMemberCenterButton(self):
        self.driver.find_element(*self.btn_menbercenter_loc).click()

    # 点击学生列表
    def clickStudentListLink(self):
        self.driver.find_element(*self.lnk_studentlist_loc).click()

    # 进入学生Iframe框
    def changeStudentFrame(self):
        # 切入Iframe框操作学生列表里面的内容
        ele =  self.driver.find_element(*self.iframe_main_loc)
        self.driver.switch_to.frame(ele)

    def click_addstu(self):
        self.driver.find_element(*self.btn_addstu_loc).click()

    # 回到上一层
    def change_main_frame(self):
        self.driver.switch_to.default_content()

    # 业务层
    # 进入学生列表
    def optionInStudentlist(self):
        self.clickMemberCenterButton()
        self.clickStudentListLink()
        self.changeStudentFrame()
        self.click_addstu()





if __name__ == "__main__":
    pass
