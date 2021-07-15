# 时间 2021/7/14 10:34
import selenium
from aTrip_page.crm_Base import *
from selenium.webdriver.common.by import By

class Search(Base):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://47.98.155.64:8080/crm')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    #定位
    def search1(self):
        return self.find(By.NAME,'userNum')
    def search2(self):
        return self.find(By.NAME,'userPw')
    def search3(self):
        return self.find(By.ID,'in1')
    #点击输入
    def search4(self,admin,pwd):
        self.search1().send_keys(admin)
        self.search2().send_keys(pwd)
        self.search3().click()
# ss=Search()