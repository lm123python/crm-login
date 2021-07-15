import unittest
from crm.aTrip_page.crm_Base import *
from crm.aTrip_sear.crm_searche import *
from ddt import ddt,data

class MyTestCase(unittest.TestCase,Search):
    def setUp(self) -> None:
        import time
        self.time=time

    def tearDown(self) -> None:
        pass
        # self.quit()

    def test_login1(self):
        a=Search()
        a.search4('admin', '123456')

        # self.assertEqual(True, False)
    def test_login2(self):
        a = Search()
        a.search4('admins', '123456')

        self.assertEqual(self.text(),'用户或密码错误！请重新输入！')


if __name__ == '__main__':
    unittest.main()
