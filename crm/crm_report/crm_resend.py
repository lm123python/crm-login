# 时间 2021/7/14 14:14
from HTMLTestRunner import HTMLTestRunner
import unittest,os,time
from crm.crm_case.test_login import *
from crm.crm_case.test_search import *

suite=unittest.TestSuite()
# suite.addTest(MyTestCase('test_login1'))
# suite.addTest(MyTestCase('test_login1'))
# suite.addTest(MyTestCase('test_login2'))
suite.addTest(MyTestCase1('test_search'))



report='./c/crm_login'
now=time.strftime('%m_%d_%H%M')
filename=report+now+'result.html'

xr=open(filename,'wb')
runner=HTMLTestRunner(stream=xr,title='crm报告',description='crm登录')
runner.run(suite)

xr.close()
