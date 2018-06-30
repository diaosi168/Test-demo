
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
            request=[]
        cursor.close()
        cnn.close()
        return request

if __name__ == '__main__':
    import configparser

    cf = configparser.ConfigParser()
    cf.read('db.conf')
    config = eval(cf.get('DATABASE','config'))

    t=Test_Dbsql(config)

    query_1 ='select * from student where id<%s'
    condtion_1 =(20,)
    print(t.get_data(query_1,condtion_1))
    query_2 = 'insert into student(age,name)values (%s,%s)'
    condtion_2 = (20, 'duolala')
    print(t.get_data(query_2,condtion_2 ))