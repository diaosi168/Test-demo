
import pymysql.connections

class Test_Dbsql:

    def __init__(self,config):
        self.config=config

    def get_cnn(self):
        return pymysql.connect(**config)

    def get_data(self,query,condition,state):
        cnn=self.get_cnn()
        cursor=cnn.cursor()

        #select
        if state==1:
            cursor.execute(query,condition)
            print(cursor.fetchall())

        #insert
        elif state==2:
            cursor.execute(query,condition)
            cursor.execute('commit')

        cursor.close()
        cnn.close()

if __name__ == '__main__':
    config = {'host': '118.126.108.173',  # 主机
              'user': 'python',  # 用户名
              'password': 'python5666',  # 密码
              'port': 3306,  # 端口
              'database': 'test_summer',  # 数据库名
              }
    query_1 ='select * from student where id<%s'
    condtion_1 =(20,)

    query_2 = 'insert into student(age,name)values (%s,%s)'
    condtion_2 = (20, 'duolala')