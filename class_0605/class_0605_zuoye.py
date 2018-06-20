



#1：创建一个名为 Restaurant 的类，
# 其方法 init ()设置两个属性： restaurant_name 和 cooking_type。
# 创建一个名为 describe_restaurant()的方法和一个名为 open_restaurant()的方法，
# 其中前者打印前述两项信息，而后者打印一条消息， 指出餐馆正在营业。
# 根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。

'''class Restaurant():
    def __init__(self,restaurant_name,cooking_type):
        self.restaurant_name=restaurant_name
        self.cooking_name=cooking_type
    def describe_restaurant(self):
        print('川菜：',self.restaurant_name,'\n湘菜：',self.cooking_name)
    def open_restaurant(self):
        print('欢迎光临，餐厅正在营业!')
restaurant=Restaurant('麻辣','辣')
print(restaurant.restaurant_name,restaurant.cooking_name)
restaurant.describe_restaurant()
restaurant.open_restaurant()'''


#2:继承1 这个类，且添加函数：discount 打折扣用的 pay_money 支付餐费用 完成调用

'''class Restaurant():
    def __init__(self,restaurant_name,cooking_type):
        self.restaurant_name=restaurant_name
        self.cooking_name=cooking_type
    def describe_restaurant(self):
        print('川菜：',self.restaurant_name,'\n湘菜：',self.cooking_name)

    def open_restaurant(self):
        print('欢迎光临，餐厅正在营业!')

class Restaurant_1(Restaurant):
    def discount_1(self,pay_monney):
        self.pay_monney=pay_monney
        print('您的折后价为：',self.pay_monney)


t=Restaurant_1('麻辣','辣')
t.discount_1('888')'''




#3:超继承1这个类的open_restaurant方法，多加一个优惠信息宣传。

class Restaurant():
    def __init__(self,restaurant_name,cooking_type):
        self.restaurant_name=restaurant_name
        self.cooking_name=cooking_type
    def describe_restaurant(self):
        print('川菜：',self.restaurant_name,'\n湘菜：',self.cooking_name)
    def open_restaurant(self):
        print('欢迎光临，餐厅正在营业!')

class Restaurant_1(Restaurant):
    def open_restaurant_1(self):
        super(Restaurant_1,self).__init__(self.restaurant_name,self.cooking_name)
        print('夏季畅爽优惠活动，消费100元以上免费送西瓜汁一份')
t=Restaurant_1('麻辣','辣')
t.describe_restaurant()
t.open_restaurant()
t.open_restaurant_1()

