# 时间 2021/7/14 15:10
import unittest
from crm.crm_case.test_login import *
test1='./'
dis=unittest.defaultTestLoader.discover(test1,pattern='test*.py')
if __name__=='__main__':
    run1=unittest.TextTestRunner()
    run1.run(dis)