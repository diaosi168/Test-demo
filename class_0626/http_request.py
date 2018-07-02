


import requests  #完成HTTP请求

class HttpRequests:
    def __init__(self,url,param):
        self.url=url
        self.param=param
    def http_request(self,method,cookies=None):
        if method.upper()=='GET':
            res=requests.get(self.url,self.param,cookies=cookies)
        elif method.upper()=='POST':
            res=requests.get(self.url,self.param,cookies=cookies)
        else:
            print('您的请求方式不对！')
        return res



if __name__ == '__main__':

    #请求地址URL
    register='http://119.23.241.154:8080/futureloan/mvc/api/member/register'
    login='http://119.23.241.154:8080/futureloan/mvc/api/member/login'
    recharge='http://119.23.241.154:8080/futureloan/mvc/api/member/recharge'

    #请求参数
    register_param={'mobilephone' : '18565752547', 'pwd' : '123456'}
    login_param={'mobilephone' : '18565752547', 'pwd' : '123456'}
    recharge_param={'mobilephone' : '18565752547', 'amount' : '500'}

    #注册
    res_register=HttpRequests(register,register_param).http_request('get',cookies=None)
    print(res_register.json())

    #登录cookie是必须登录了之后才会生成的
    res_login=HttpRequests(login,login_param).http_request('get')
    print(res_login.json())
    cookies=res_login.cookies  #登录请求发出之后才能获取cookies
    print(cookies)

    #充值
    res_recharge=HttpRequests(recharge,recharge_param).http_request('get',cookies=cookies)
    print(res_recharge.json())
    print(res_recharge.cookies=={})