

import unittest
import HTMLTestRunnerNew


from class_0609.class_0609_3 import http

class TestHttp(unittest.TestCase):
    def setUp(self):
        print("开始执行测试用例！")
        self.url='http://119.23.241.154:8080/futureloan/mvc/api/member/login'
        self.param={'mobilephone':'15678934551','pwd':'234555'}
    def test_get_requests(self):
        s=http(self.url,self.param)
        s.get_request()
    def test_post_requests(self):
        t=http(self.url,self.param)
        t.post_request()
    def tearDown(self):
        print('结束执行测试用例')


suite=unittest.TestSuite()
#第一种写法
#suite.addTest(TestHttp('test_get_requests'))
#suite.addTest(TestHttp('test_post_requests'))
#第二种写法
loader=unittest.TestLoader()
suite.addTests(loader.loadTestsFromTestCase(TestHttp))

with open('home_work.html','wb')as class_0609:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=class_0609, verbosity=2, title='故事', description='test_06_09',
                                              tester='duolala')
    runner.run(suite)