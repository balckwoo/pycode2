from libs.Tools import create__browser_driver
from config.Secrect import test_edu_url



class Page(object):
    def __init__(self, driver=''):

        b = driver
        if b == '':
            self.dv = create__browser_driver()
        else:
            self.dv = b
        self.dv.maximize_window()
        self.dv.implicitly_wait(10)

    def open_url(self, url=test_edu_url):
        self.dv.get(url)

    def close_broser(self):
        self.dv.quit()

