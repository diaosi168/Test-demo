def s12():
    num = 0
    jj=18
    k=0
    while True:
        k = k + 1
        ii = int(input("请输入年龄："))

        if ii > jj:

            sex = input("请输入性别：")
            if sex == 'f' or sex == 'm':

                print("可加入足球队！")

                num += 1

            else:
                print("性别不符！")
        else:
            print("年龄不符合标准!")

        print("询问K：%d" % k, "次数;可加入足球队的总人数：%d" % num)

s12()