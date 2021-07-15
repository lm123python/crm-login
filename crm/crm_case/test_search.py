import unittest
from crm.aTrip_page.crm_Base import *
from crm.aTrip_sear.crm_searche import *
from ddt import ddt,data

class MyTestCase1(unittest.TestCase,Search):
    def setUp(self) -> None:
        import time
        self.time=time

    def tearDown(self) -> None:
        pass
        # self.quit()

    def test_search(self):
        a=Search()
        a.search4('admin', '123456')
        #定位员工信息右侧
        self.frame('topFrame')#
        self.find(By.LINK_TEXT,'员工信息').click()
        self.frame_out()#切换可定位页面

        #切换主要页面
        self.frame("mainFrame")
        self.find(By.NAME,'userName').send_keys('张三')
        self.find(By.XPATH,'/html/body/form/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[2]/select').click()
        self.dorp_down(By.NAME,'queryType',0)#下拉框选中员工姓名
        self.find(By.XPATH,'/html/body/form/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[3]/input').click()#点击查询


        # self.assertEqual(True, False)
    # @unittest.skip('暂时不测')
    # def test_login2(self):
    #     a = Search()
    #     a.search4('admins', '123456')
    #
    #     self.assertEqual(self.text(),'用户或密码错误！请重新输入！')


if __name__ == '__main__':
    unittest.main()
