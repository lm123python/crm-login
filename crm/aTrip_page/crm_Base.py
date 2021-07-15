# 时间 2021/7/14 10:03
import selenium
from selenium import  webdriver
from selenium.webdriver.support.select import Select

class Base(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver.get('http://47.98.155.64:8080/crm')
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(5)
     #定位
    def find(self,by1,value):
        try:
            element = self.driver.find_element(by1, value)
            return element
        except:
            print('定位失败')
    #点击
    def click(self,by1,value):
        return self.find(by1,value).click()
    #清空
    def clear(self,by1,value):
        return self.find(by1,value).click()
    #输入内容
    def send(self,by1,value):
        return  self.find(by1,value).send_keys()
    #关闭
    def quit(self):
        return  self.driver.quit()
        # self.driver.close()
    def close(self):
        return  self.driver.close()
    def crm_assert(self):
        tanchu = self.driver.switch_to.alert
        return tanchu
    #提取文本
    def text1(self):

        return self.crm_assert().text



    #切换frame
    def frame(self,fid):
        return self.driver.switch_to.frame(fid)
    #切换回原来的页面
    def frame_out(self):
        return self.driver.switch_to.default_content()
    #下拉框
    def dorp_down(self,by1,value,dex):
        element=self.find(by1,value)
        down=Select(element)
        down.select_by_index(dex)
    def accept(self):
        return self.driver.switch_to.alert.accept()

