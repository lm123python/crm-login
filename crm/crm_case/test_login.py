import unittest
from aTrip_sear.crm_searche import Search
import time


class MyTestCase(unittest.TestCase,Search):
    def setUp(self) -> None:
        self.a = Search()
        print('setup')
    def tearDown(self) -> None:
        time.sleep(2)
        print('teardown')
        self.a.close()
    def test_login1Search(self):
        self.a.search4('admin', '123456')
        # self.assertEqual(True, False)
    # @unittest.skip('暂时不测')
    def test_login2(self):
        self.a.search4('admins', '123456')
        b=self.a.text1()
        print(b)
        self.assertEqual(b,'用户或密码错误！请重新输入！')
        time.sleep(3)
        self.a.accept()


if __name__ == '__main__':
    unittest.main()
