class Add():
    def add(self,a,b):
        return a+b

#单元测试的目的是什么？见证自己的代码能不能够正常运行，对某个接口的功能测试
#什么是单元测试？ 对类或者对函数进行测试

#TestCase 测试用例
#1.一个testcase的实例就是一条测试用例；
#2.测试前准备环境的搭建（setUp），执行测试代码（run），以及测试后环境的还原（tearDown）
#TestSuite 测试套件 存储测试用例的容器
#TestLoader 加载测试用例  用来加载TestCase到TestSuite中的
#TextTestRunner 执行用例的，其中的run（test）会执行TestCase,TestSuite中的run(result)方法
#TextTestResult  保存TextTestRunner 执行的结果
#fixture   测试用例环境的搭建和销毁


import unittest     #package unittest写测试用例的框架

#去写测试用例 unittest 测试类

class TestAdd(unittest.TestCase):  #继承；
    def setUp(self):#在你执行用例之前会做的初始化操作
        print('开始执行用例')

    def test_add_two_positive(self):   #用例一定要以test_开头
        print('两个正数相加：')
        t=Add()
        result=t.add(9,2)
        print(result)
    #用例执行的先后顺序，根据用例方法名ascII编码去执行的
    def test_add_two_negative(self):   #在你执行每一条用例之后都会做的清除工作操作
        print('两个负数相加：')
        t=Add()
        result=t.add(-9,-2)
        print(result)

    def tearDown(self):                #在你执行用例之后会做的清除工作操作
        print('结束用例的执行！')

class TestPrint(unittest.TestCase):
    def setUp(self):
        print('这个是测试打印的测试用例')

    def test_print_1(self):
        print('打印第二条信息')

    def tearDown(self):
        print('我们已经结束这条测试的打印')

if __name__=='__main__':
    unittest.main()   #他会执行当前模块所有以test开头的用例



#.. 代表一条用例，并且通过
#E error代表用例执行遇到异常，你的传参有错，程序执行有问题
#F 代表用例执行失败，期望值 = 实际值。'''





'''class Http(unittest.TestCase):

    def setUp(self):
        print('开始执行测试用例')

    def __init__(self,url1,param):
        self.url=url1
        #print(url1)
        self.param=parampydev debugger: process 7973 is connecting

    try:
        def test_get_request(self):
            response=requests.get(self.url,self.param).json()
            return response
        #return response.json()
        def test_post_request(self):
             response = requests.post(self.url, self.param).json()
             return response
        #return response.json()
    except:
        print("错误")
    def tearDown(self):
        print('结束执行测试用例')

if __name__ == '__main__':
    url1 = ''
    param={}
    t=Http('url','param')
    #print(t)
   # print(t.test_post_request())

unittest.main'''
