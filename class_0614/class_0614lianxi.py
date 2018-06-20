
import pymysql.connections  #操作数据库


#数据库的登录信息
config={'host':'118.126.108.173',   #主机
'user':'python',                    #用户名
'password':'python5666',            #密码
'port':3306 ,                       #端口
'database':'test_summer',           #数据库名
}

#登录上数据
cnn=pymysql.connect(**config)

#游标--》cursor-->获取操作数据库的权限
cursor=cnn.cursor()

#查询 select
#sql='select * from student where id=%s'

#传参 ：元祖 列表 字典
#元祖的传参，如果只有一个数据记得加，号

#sql='select * from student where id=%s and age>%s'
#查询的时候传参：只能以元祖的形式传参 data=(2,20)
#执行语句
#cursor.execute(sql,data)

#insert 语句
sql_insert='insert into onlyjack(age,name) values(%s,%s)'
data=(18,'duolala')
#执行语句
cursor.execute(sql_insert,data)
cursor.execute('commit')
#fetchone  fetchall读取查询结果
#fetchone:从结果集里面读取一条数据
#fetchall:把查询结果里面的所有的值都读取出来
#如果你只有一条结果 你用fetchone ,fetchall都可以
#如果你查询的数据多余一条，你只用fetchone就会报错
#多条数据用fetchall不会报错

#result_1=cursor.fetchone()
#result_2=cursor.fetchall()

#print('one的数据',result_1)
#print('all的数据',result_2)


cursor.close()
cnn.close()






