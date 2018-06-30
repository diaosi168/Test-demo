

import unittest
from ddt import ddt,data,unpack

#ddt    全名data driver test     数据驱动测试
#ddd    装饰器 装饰测试类
#data   装饰器 装饰测试用例
#unpack   装饰器，装饰测试用例，但是是用于数据的拆分

'''def print_msg(*args):   # * 一个*代表动态参数
    print(args)

print_msg(1,2,3,4)   #---元祖
print_msg(*[[1,2],[3,4]]) #---元祖
print_msg({'age':33,'name':'duolala'})   #---元祖

def print_info(**kwargs):   # **两个**代表关键字参数
    print_msg(kwargs)

print_info(x=1,y=3)
print_info(**{'age':33,'name':'duolala'})   # 元祖，获取的是key值'''


#ddt  的引用
@ddt
class TestAdd(unittest.TestCase):
    def setUp(self):
        print('start===========')
        #   @data(*[[1,2],[3,4]])

    '''def test_add(self,a):
        print(a)'''

    @data(*[{'age': 22, 'name': 'duolala'}, {'age': 32, 'name': 'tisou'}])
    @unpack
    def test_add1(self,age,name):
        print(age)
        print('=======')
        print('name')


    def tearDown(self):
        print('stop==============')