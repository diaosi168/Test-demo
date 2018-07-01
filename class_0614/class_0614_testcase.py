

import time
import unittest
import HTMLTestRunnerNew
from class_0614.class_0614_readexcel import DoExcel
from class_0614.class_httprequests import HttpRequest
from ddt import ddt,data,unpack
from class_0614 import class_logning
#logger=class_logning.Mylog('http','INFO','http_logging.txt')
test_data=DoExcel('test_case_0614.xlsx', 'test_data').read_data()
@ddt
class TestHttpRuqust(unittest.TestCase):
    def setUp(self):
        self.t=DoExcel('test_case_0614.xlsx', 'test_data')
        print('开始执行测试用例')

    '''def __init__(self,url,param,method,expected,case_id,methodName='runTest'):
        super(TestHttpRuqust,self).__init__(methodName)
        self.url=url
        self.param=eval(param)
        self.method=method
        self.expected=expected
        self.case_id=case_id'''

    @data(*test_data)
    def test_case(self,data_1):
        print('执行的是第',data_1[0],'条用例')
        response=HttpRequest(data_1[3],eval(data_1[4])).get_post_http_requests(data_1[2])
        #监控断言
        try:
            self.assertEqual(data_1[5],response['reason'])
            #print(self.expected)
            #print(response['reason'])
            result='pass'
            actual=response['reason']
            self.t.write_data(data_1[0]+1,actual,str(response),result)
        #raise e如果加上raise那么抛出异常了，结果就不会写入Excel里面，但抛出异常，中断测试
        except AssertionError as e:
            print('报告错误的信息是%s')
            result='fail'
            raise e
        finally:
            #pass
            self.t.write_data(data_1[0]+1,actual,str(response),result)

        #写入数据
        #self.t.write_data(data_1[0]+1,str(response),result)

    def tearDown(self):
        print('结束测试用例')

suite = unittest.TestSuite()
#suite.addTest(TestHttpRuqust('test_case'))
#unittest.TextTestRunner().run(suite)


#第二种加载测试用例的方法,上下只需取一种
loader=unittest.TestLoader()
suite.addTests(loader.loadTestsFromTestCase(TestHttpRuqust))

now=time.strftime('%Y-%m-%d_%H_%M_%S')  #引入时间戳，获取当前时间
file_path='home_work'+now+'.html'

#执行用例
with open(file_path,'wb')as file_path:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file_path, verbosity=2, title='故事', description='test_06_14',
                                            tester='duolala')
    runner.run(suite)