

#请给0607这节课写的HTTP请求类写一个测试类。要求如下：
#1：写好测试类
#2：写好单元测试
#3：要求代入测试数据，输出测试报告
import requests


class http:

    def __init__(self,url,param):
        self.url=url
        self.param=param
    def get_request(self):
        #print("123123")
        response=requests.get(self.url,self.param)
        return response.json()

    def post_request(self):
        response = requests.post(self.url, self.param)
        return response.json()

if __name__ == '__main__':
    url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/login'
    param = {'mobilephone':'15678934551','pwd':'234555'}
    t=http(url,param)
    print(t.get_request())
    print(t.post_request())
