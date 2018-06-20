'''class Add():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a+self.b)

class Add_2():             #多继承
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print('两数相加之和；%s'%(self.a+self.b))
class Add_3(Add,Add_2):   #继承多个类，如果有重名的函数方法，继承的顺序以谁在前为主,没有的重名的也以谁在前为主
    pass                   #多继承，可以继承多个爸爸
t=Add(6,7)
t.add()'''


#超继承
'''class Add():
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        print(self.a+self.b)

class Add_2(Add):
    def __init__(self,a,b,c):  #重写
    #超继承调用父类里面的函数，不用带self,只需要把父类里面的参数带过来就可以了 
        super(Add_2,self).__init__(a,b) #相当于调用父类里面的__init__函数
        self.c=c
    def add(self):
        print('两数相加之和；%s'%(self.a+self.b+self.c))
Add_2(3,4,5).add()'''


class PrintMsg():
    def print_msg(self,msg):
        print('父亲函数打印的参数是：',msg)
class SubPrintMsg(PrintMsg):   #重写，继承父类，在进行重写
    def print_msg(self,msg):    #超继承，父类函数俩面的代码可以继承过来，然后还可以加一些新特性
        super(SubPrintMsg,self).print_msg(msg)   #super需要根据你传进来子类，去找到他的父类，然后去继承调用它的方法
        print('哈哈哈'+msg)

t=SubPrintMsg()
t.print_msg('你这个小笨蛋')


#超继承
class Add_1():
    def add(self,a,b):
        print('两数之和是：',a+b)#计算两数之和
class Add_2(Add_1):
    def add(self,a,b,c):  #计算a,b两数之和并且打印出来，然后计算a,b,c三数之和 并且打印出来
        super(Add_2, self).add(a,b)  #这里是调用父类add的方法
        print('三数之和是：',a+b+c)

t=Add_2()
t.add(3,4,5)


'''#return的写法
class Add_1():
    def add(self,a,b):
        return('两数之和是：%s'%(a+b))#计算两数之和
class Add_2(Add_1):
    def sub(self,a,b,c):  #计算a,b两数之和并且打印出来，然后计算a,b,c三数之和 并且打印出来
        result=super(Add_2,self).add(a,b)  #这里是调用父类add的方法
#第二种写法 result=self.sub(a,b) 类里面函数方法如果不重名，可以直接用self.父类函数的方法
        print(result)
        print('三数之和是：',a+b+c)

t=Add_2()
t.sub(3,4,5)'''


