from po.Common_page import Page
from selenium.webdriver.common.by import By

class TeacherListPage(object):

    # 对象层
    btn_menbercenter_loc = (By.XPATH, '//*[@id="header"]/ul/li[3]/a')
    lnk_studentlist_loc = (By.LINK_TEXT, '教师列表')
    iframe_main_loc = (By.ID, 'mainframe')

    # 操作层
    # 点击会员中心
    def clickMemberCenterButton(self, dv):
        dv.find_element(*self.btn_menbercenter_loc).click()

    # 点击教师列表
    def clickTeacherListLink(self, dv):
        dv.find_element(*self.lnk_studentlist_loc).click()

    # 进入教师Iframe框
    def changeTeacherFrame(self, dv):
        # 点击教师列表
        dv.find_element_by_link_text('教师列表').click()
        # 切入Iframe框操作教师列表里面的内容
        ele = dv.find_element(*self.iframe_main_loc)
        dv.switch_to.frame(ele)

    # 回到上一层
    def change_main_frame(self, dv):
        dv.switch_to.default_content()

    # 业务层
    # 进入教师列表
    def optionInTeacherList(self, dv):
        self.clickMemberCenterButton(dv)
        self.clickTeacherListLink(dv)
        self.changeTeacherFrame(dv)

if __name__ == '__main__':
    pass
