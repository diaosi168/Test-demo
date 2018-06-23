


import unittest

from class_0614.class_0614_readexcel import DoExcel
from class_0614.class_httprequests import HttpRequest


class TestHttpRuqust(unittest.TestCase):
    def setUp(self):
        print('开始执行测试用例')
        self.t=DoExcel('test_case_0614.xlsx', 'test_data')

    def __init__(self,url,param,method,expected,case_id,methodName='runTest'):
        super(TestHttpRuqust,self).__init__(methodName)
        self.url=url
        self.param=eval(param)
        self.method=method
        self.expected=expected
        self.case_id=case_id

    def test_case(self):
        print('执行的是第',self.case_id,'条用例')
        response=HttpRequest(self.url,self.param).get_post_http_requests(self.method)
        #监控断言
        try:
            self.assertEqual(self.expected,response['reason'])
            print(self.expected)
            #print(response['reason'])
            result='pass'
        except AssertionError as e:
            print('报告错误的信息是%s'%e)
            raise e
            result='fail'

        #写入数据
        self.t.write_data(self.case_id+1,str(response['reason']),result)

    def tearDown(self):
        print('结束测试用例')

