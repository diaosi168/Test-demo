

#专门完成http请求测试的测试类
import unittest
from class_0626.http_request import HttpRequests
from class_0626.do_excel import DoExcel
from ddt import ddt,data

test_data = DoExcel('tase_case.xlsx', 'test_data').read_data()

COOKIES=None   #定义一个全局变量初始值

@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        self.t=DoExcel('tase_case.xlsx', 'test_data')

        print('开始执行测试了')
        #self.url='http://119.23.241.154:8080/futureloan/mvc/api/member/register'
        #self.param={'mobilephone' : '18565752547', 'pwd' : '123456'}
    @data(*test_data)
    def test_http_request(self,a):
        print('测试数据是：',a)
        print('目前正在执行第%s条用例'%a[0])
        global COOKIES
        res=HttpRequests(a[4],eval(a[5])).http_request('get',cookies=COOKIES)
        if res.cookies!={}:  #判断长度或者判断是否为空{}
            COOKIES=res.cookies
        print(res.json())
        try:
            self.assertEqual(str(a[6]),res.json()['code'])
            result='PASS'

        except AssertionError as e:
            result='Fail'
            raise e     #raise e后面的代码不执行,已经中断代码了
        finally:
            self.t.write_data(a[0]+1,str(res.json()),result)

    def tearDown(self):
        print('测试结束了！')