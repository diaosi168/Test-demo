
import ddt

#ddd  全名data driver test
#
#
#

def print_msg(*args):   #* 一个*代表动态参数
    print(args)

print_msg(1,2,3,4)   #---元祖
print_msg([1,2,3,4]) #---元祖
print_msg({'age':33,'name':'duolala'})   #---元祖
