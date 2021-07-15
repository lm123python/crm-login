# 时间 2021/7/14 19:48

from crm.aTrip_page.crm_Base import *
from crm.aTrip_sear.crm_searche import *

import time


class MyTestCase(Search):


    def test_login1(self):
        a=Search()
        a.search4('admin', '123456')

        # self.assertEqual(True, False)
    # @unittest.skip('暂时不测')
    def test_login2(self):

        a = Search()
        a.search4('admins', '123456')
        b=self.text1()
        self.assertEqual(b,'用户或密码错误！请重新输入！')
        self.accept()
a=MyTestCase()
a.test_login2()