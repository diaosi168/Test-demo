
import time
import unittest
import HTMLTestRunnerNew
from class_0614.class_0614_testcase import DoExcel
from class_0614.class_0614_testcase import TestHttpRuqust


test_data=DoExcel('test_case_0614.xlsx', 'test_data').read_data()
suite=unittest.TestSuite()

for i in range(len(test_data)):
    url = test_data[i][3]
    param = test_data[i][4]
    method = test_data[i][2]
    expected = test_data[i][5]
    case_id = test_data[i][0]
    suite.addTest(TestHttpRuqust(url,param,method,expected,case_id,'test_case'))

#第二种加载测试用例的方法,上下只需取一种
#loader=unittest.TestLoader()
#suite.addTests(loader.loadTestsFromTestCase(TestHttpRuqust))

now=time.strftime('%Y-%m-%d_%H_%M_%S')  #引入时间戳，获取当前时间
file_path='home_work'+now+'.html'

#执行用例
with open(file_path,'wb')as file_path:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file_path, verbosity=2, title='故事', description='test_06_14',
                                              tester='duolala')
    runner.run(suite)


