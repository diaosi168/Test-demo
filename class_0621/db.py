from conf.db import host,user,port
import os
print(host)


base_dir = str(os.path.dirname(os.path.dirname(__file__)))

base_dir = base_dir.replace('\\', '/')

file_path = base_dir + "/Config/DbConfig.ini"



print(type(base_dir))