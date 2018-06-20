

import unittest
import HTMLTestRunnerNew

'''class Add():
    def add(self,a,b):
        print(a+b)

#要求你们对这个add类里面的函数进行测试
#1 2/-1 -2/0 0/-1 2/不输入数据a/不输入数据b/两个数据都不输入
#小数

t=Add()
if t.add(1,2)==3:
    print('用例通过')
t.add(-1,-2)
t.add(0,0)
t.add(-1,2)
t.add(None,2)
t.add(1,None)
t.add(None,None)'''

#from class_0609 import class_0609_2
from  class_0609.class_0609_2 import TestPrint

suite=unittest.TestSuite()   #测试套件，存储测试用例的

#suite.addTest(TestAdd('test_add_two_positive'))
#addTest 是添加测试用例的，并且要求是一个实例，后面接接内名，并且执行类里面的方法
#下面是执行你存在suite里面的用例的

loader=unittest.TestLoader()  #加载测试用例
#suite.addTests(loader.loadTestsFromModule(class_0609_2))
suite.addTests(loader.loadTestsFromTestCase(TestPrint))
with open('report.html','wb') as class_0609:


#suite下面的是执行你存在suite里面的用例的
    #runner=unittest.TextTestRunner(stream=file,descriptions='这个是报告',verbosity=2)

    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=class_0609, verbosity=2,title='故事',description='test_06_09',tester='duolala')
    runner.run(suite)
