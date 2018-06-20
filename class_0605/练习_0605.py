
class cars():
    def __init__(self,coluer,money,brand):
        self.coluer=coluer
        self.money=money
        self.brand=brand

    def go_mountain(self):
        return (self.brand,self.money,'上山技能一百分')
    def go_sea(self):
        return ('可以做潜水挺')
    def go_sky(self):
        return ('666,上山下海能上天')
# 测试代码
if __name__ =='__main__':  # python程序的入口
    # 只有当你在当前模块执行的时候，才会执行if下面的代码
    car = cars('blue', 90000000, '大众')
    print(car.go_mountain())
    print(car.go_sky())


'''car=cars('blue',90000000,'大众')
print(car.go_mountain())
print(car.go_sky())'''







'''class User():
    def __init__(self,content,name='糖糖'):
        self.name=name
        self.content=content
    #第二种写法
    #def __init__(self):
    #    self.name='tangtang'
    #第三种写法
    #def __init__(self,name):
    #     self.name=name
    def describe_user(self):
        return('晚上好：',self.name)
    def greet_user(self):
        print('你好啊：',self.name,self.content)
t=User('小星星')
print(t.describe_user())
t=User('小可爱')
t.greet_user()'''


