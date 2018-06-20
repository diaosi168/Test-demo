


import unittest
import HTMLTestRunnerNew
import time


from class_0612.class_0612_2 import Http


class TestHttp(unittest.TestCase):
    def setUp(self):
        print('开始执行测试用例')
        self.url='http://v.juhe.cn/laohuangli/d'
        self.param={'date':'2018-09-11','key':'a8f2732319cf0ad3cce8ec6ef7aa4f33'}

    def test_get_post_ruquests(self):
        t=Http(self.url,self.param)
        response=t.get_post_http_requests('post')
        self.assertEqual('错误的请求KEY!!',response['reason'])

    def tearDown(self):
        print('结束测试')

suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(TestHttp('test_get_post_ruquests'))

now=time.strftime('%Y-%m-%d_%H_%M_%S')  #引入时间戳，获取当前时间
class_0612='home_work'+now+'.html'
with open(class_0612,'wb')as class_0612:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=class_0612, verbosity=2, title='故事', description='test_06_12',
                                              tester='duolala')
    runner.run(suite)
