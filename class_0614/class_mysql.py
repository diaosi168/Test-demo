
import pymysql.connections  #操作数据库


class DoMySql:
    def __init__(self,config,sql,data):
        self.config=config
        self.sql=sql
        self.data=data


    def get_data(self):
        #登录上数据
        cnn=pymysql.connect(**self.config)
        #游标--》cursor-->获取操作数据库的权限
        cursor=cnn.cursor()
        #执行语句
        cursor.execute(self.sql,self.data)  #新增一条插入信息读取
        result=cursor.fetchall()
        cursor.close()
        cnn.close()
        return result

if __name__ == '__main__':
    # 数据库的登录信息
    config = {'host': '118.126.108.173',  # 主机
              'user': 'python',  # 用户名
              'password': 'python5666',  # 密码
              'port': 3306,  # 端口
              'database': 'test_summer',  # 数据库名
              }






