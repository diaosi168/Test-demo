
import unittest
import HTMLTestRunnerNew
import time   #引入时间

from class_0609.class_0609_3 import http

class TestHttp(unittest.TestCase):
    def setUp(self):    #做好初始化工作
        print('开始执行测试用例')
        #URL，param两个参数可以放在最外面，类里面的方法可以调用，
        self.url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/login'
        self.param = {'mobilephone': '15678934551', 'pwd': '234556'}

    def test_get_requests(self):
        s = http(self.url, self.param)
        s.get_request()

    def test_post_requests(self):
        t = http(self.url, self.param)
        response=t.post_request()    #查看返回值
        #断言
        #self.assertIsNone(response)      #判断响应结果是否为空

        #添加异常处理
        try:
            self.assertEqual('登录成功',response['msg'])
        except AssertionError as e:
            print('请求失败的结果是：%s'%e)
            raise e
        #r如果是类里面的属性或者是类里面的方法就要用self。属性名；self.方法名
        #如果要调用父类里面的方法或者函数，也要用self.父类方法名or 属性名
        #期望值和实际值的比对  Python里面叫断言，用asserEqual函数比对

    def tearDown(self):
        print('结束执行测试用例')


suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTests(loader.loadTestsFromTestCase(TestHttp))

now=time.strftime('%Y-%m-%d_%H_%M_%S')  #引入时间戳，获取当前时间
class_0612='home_work'+now+'.html'
with open(class_0612,'wb')as class_0612:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=class_0612, verbosity=2, title='故事', description='test_06_12',
                                              tester='duolala')
    runner.run(suite)
