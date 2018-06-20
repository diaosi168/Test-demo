

#全部继承，部分继承，多继承，超继承

import class_0605.练习_0605  #具体到模块名
from class_0605.练习_0605 import cars   #具体到类名

class SuperCars(cars):    #全部继承，只有一个爸爸
    pass

'''car=SuperCars('blue',90000000,'奥迪') #创建实例，全部继承父类函数方法
#car=cars('blue',90000000,'大众')
print(car.go_mountain()) 
print(car.go_sky())
print(car.go_sea())'''




class SuperCars(cars):    #部分继承--》重写父类
    #当父类与子类有重名的方法的时候 ，就叫重写
    #子类的实例调用函数的是自己子类的函数
    def go_mountain(self,hill_height):
        print(self.brand+'可以爬山'+hill_height+'米的高山')
    #新建几个父类没有的函数
    #父类不能调用子类的函数
    def go_outer_space(self):
        print('还可以去外太空')
car=SuperCars('blue',90000000,'奔驰')
print(car.go_mountain('5000'))
#print(car.go_sky())
#print(car.go_sea())
car.go_outer_space()



class BigSuperCars(SuperCars,cars):  #多继承
    pass

car=BigSuperCars('yellow','500','沃尔沃')
car.go_mountain('4000')






