import requests   #爬虫，正则

'''class http():
    host ='httt://127.0.0.1/mane=123$esx=1456'
    get=requests.get(host).json()
    post=requests.post(host).json()
    print(get,post)'''


#requests 模块

#pip install requests在线安装
#url='https://www.baidu.com/baidu?'

#get

#.text 获取它相应的内容，它返回的是字符串str
#print(type(requests.get(url).text))
#.content 返回raw原始报文，下载图片用这个式的
#print(type(requests.get(url).content))
#.json  返回的是字典dict格式，推荐用json，可以根据keys去取值
#result=requests.get(url).json()


#post
#print('post请求：',requests.post(url).json())
'''if result['reason']=='successrd':
    print('请求成功！')

else:
    print('请求失败！')'''

#url='https://www.baidu.com/baidu?'
#param={'tn:monline_3_dg','ie:utf-8','wd:ketangpai'}
#response=requests.get(url,param).json()
#print(response)
#http状态码 ？ 404 --》检查地址是否有问题
#  200 --》就是请求成功了吗？不一定，200只能说服务器接收到了请求，并且给出了相应
# 503 --》开头的都是服务器的问题
# 403 301 302 500 502 505




'''class http():
    def __init__(self,url):
        self.url=url
    def get(self):
        print(requests.get(self.url).text)
    def post(self):
        print(requests.post(self.url).text)
t=http('http://www.baidu.com')
t.get()
t.post()


class http:
    def __init__(self,url,param):
        self.url=url
        self.param=param
    def get_request(self):
        response=requests.get(self.url,self.param)
        return response.json()
    def post_request(self):
        response = requests.post(self.url, self.param)
        return response.json()
t=http(url,param)
t.get_request()
t.post_request()'''





class http():  #http请求类，专门完成get或者post请求
    def __init__(self,url,param):
        self.url=url
        self.param=param

    def get_post_requst(self,method):
         try:  #try下面接监控代码
            if method.upper()=='GET':
                response=requests.get(self.url,self.param)
            elif method.upper()=='POST':
                response = requests.post(self.url, self.param)
                return  response.json()
            else:
                print('请求的方法不存在')
            return response.json()
         except Exception as e:
             print('请求失败，出现的错误结果是%s'%e)
        #except 抓到错误，然后代码可以继续运行
        #把异常信息获取到，并且对异常进行处理，收集异常并把异常写进日志
             raise e   #你处理完了异常之后，要把错误物归原主


if __name__=='__main__':
    url = 'http://v.juhe.cn/laohuangli/d'
    param={'date':'2018-09-11','key':'a8f2732319cf0ad3cce8ec6ef7aa4f33'}
    t=http(url,param)
    t.get_post_requst('POST')
    print(t.get_post_requst("POST")) #得到的结果是无法通过的
