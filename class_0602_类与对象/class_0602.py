'''class car():
    coluer='red'
    money=10000000
    brand='大众'

    def go_mountain(self):
        return ('上山技能一百分')
    def go_sea(self):
        return ('可以做潜水挺')
    def go_sky(self):
        return ('666,上山下海能上天')
cars=car()
print(cars.go_mountain())
print(cars.go_sea())
print(cars.go_sky())'''


'''class boyFriend:
#属性
    #name='大大'
    age=27
    height=173
    weight=62
    sex='boy'
    money=100000000
    house=1
    car=1
#技能
    def get_name(self,name):
        return ('我男票的名字是：%s'%name)
    def get_age(self):   #类里面的函数调用类里面的属性,必须加self关键字+属性名
        return('我男票的年纪是：%s'%self.age)
    def earn_money(self,how_much,name):    #与普通函数的区别是，有一个关键字self
        #age=self.get_age()
        #print(age)
        print(self.get_name(name))
        return ('要会超级赚钱,每个月的月薪是：%s'%how_much)

    #def cooking(self):
        #print ('做饭可以堪比五星级大厨')
    #def driving(self):
        #print('秋名山车神')
    #def shopping(self):
        #return ('最喜欢的事情就是给我买买买！')
    #def code(self,language='python'):
        #return ('写代码6666,尤其是:%s写的特别好'%language)
#实例化
boy_freind=boyFriend()
print('你男票赚钱怎么样：',boy_freind.earn_money('5万','duoduo'))

#print(boy_freind.get_name('大大'))
#print(boy_freind.age)
#print(boy_freind.money)
#print(boy_freind.code())
#print(boy_freind.cooking())
#print(boy_freind.shopping())      '''


#1：写一个软件测试工程师类，具有的属性和技能，你们自己去定。
class TestEngineer():
    name='duolala'
    age='28'
    sex='女'
    testing='代码写的666'

    def gongnengtest(self):
        return ('功能测试',self.name)
    def huihetest(self,name):
        name=self.baihetest(name)
        print(name)
        return ('灰盒测试')
    def baihetest(self,testing):
        return ('白盒测试%s'%testing)

t=TestEngineer()
print(t.name)
print(t.age)
print(t.huihetest('dada'))
print(t.baihetest('内部逻辑'))
print(t.gongnengtest())


#2：创建一个名为 User 的类，其中包含属性 first_name 和 last_name,
# 还有用户简介通常会存储的其他几个属性。
# 在类 User 中定义一个名为 describe_user()的方法，它打印用户信息摘要；
# 再定义一个名为 greet_user()的方法，它向用户发出个性化的问候。
# 创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。


'''class User():
    def __init__(self,first_name,last_name,age,sex):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.sex=sex
    def describe_user(self):
        print('姓名：',self.first_name,self.last_name,'年纪：',self.age,'性别：',self.sex)
    def greet_user(self):
        print('你好！',self.first_name,self.last_name)

user_1=User('二','柱',24,'boy')
user_2=User('故','事',25,'girl')
user_3=User('一米','阳光',22,'girl')

user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user()'''



