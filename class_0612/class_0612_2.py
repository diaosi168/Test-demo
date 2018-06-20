

import requests

class Http:
    def __init__(self,url,param):
        self.url=url
        self.param=param

    def get_post_http_requests(self,method):
        try:
            if method.upper()=='GET':
                response=requests.get(self.url,self.param)
            elif method.upper()=='POST':
                response=requests.post(self.url,self.param)
                return response.json()
            else:
                print('请求数据不正确!')
            return response.json()
        except AssertionError as e:
            print('请求失败！')
            raise e

if __name__=="__main__":
    url='http://v.juhe.cn/laohuangli/d'
    param={'date':'2018-09-11','key':'a8f2732319cf0ad3cce8ec6ef7aa4f34'}
    t=Http(url,param)
    print(t.get_post_http_requests('GET'))



