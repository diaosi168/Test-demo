
import pymysql.connections

class Test_Dbsql:

    def __init__(self,config):
        self.config=config

    def get_data(self,query,condition,state):
        cnn=pymysql.connect(**config)
        cursor=cnn.cursor()

        #select
        if state==1:
            cursor.execute(query,condition)
            print(cursor.fetchall())
            request=cursor.fetchall()
        #insert
        elif state==2:
            cursor.execute(query,condition)
            cursor.execute('commit')
            request=[]   #定义一个空列表
        cursor.close()
        cnn.close()
        return request

if __name__ == '__main__':
    import configparser

    cf = configparser.ConfigParser()
    cf.read('db.conf')
    config = eval(cf.get('DATABASE','config'))  #根据指定的未知传入section ，option

    t=Test_Dbsql(config)   #原始配置文件中读取出来的数据是str，要转换成dictionary，需要加一个eval，加eval是Python能够识别的最原始的数据类型

    query_1 ='select * from student where id<%s'
    condtion_1 =(20,)
    print(t.get_data(query_1,condtion_1,1))
    query_2 = 'insert into student(age,name)values (%s,%s)'
    condtion_2 = (20, 'duolala')
    print(t.get_data(query_2,condtion_2,2))