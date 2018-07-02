


import time
import unittest
import HTMLTestRunnerNew
from class_0626.test_http_request import TestHttpRequest

suite=unittest.TestSuite()
loader=unittest.TestLoader()

suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

now=time.strftime('%Y-%m-%d_%H_%M_%S')  #引入时间戳，获取当前时间
file_path='home_work'+now+'.html'
with open(file_path,'wb')as file_path:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file_path, verbosity=2, title='故事', description='test_06_12',
                                              tester='duolala')
    runner.run(suite)
