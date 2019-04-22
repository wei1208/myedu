def for_demo():
    for w in range(4,6):
        print(w)
    for i in range(-3,10,2):
        print(i)
blist = ['hello','word','吴学伟','123',1,2,3,]
# 遍历:就是对每个列表中的元素都做一次操作
def for_list():
    for i in blist:
        print(i)
def for_list2():
    # 获取list的长度
    w = len(blist)
    # 通过长度设置循环次数
    # 把i当作索引值来遍历元素
    for i in range(w):
        print(blist[i])
# 停止所有循环
def for_break():
    for i in range(5):
        print(i)
        if i ==2:
            break
# countinue:停止本轮循环，直接开始下一次循环
def for_countinue():
    for w in range(5):
        range(w)
        if w ==2:
            continue
        print('第%s循环' % w)
        print('')
# 计算1到50之间的奇数和?
def sum():
    a = 0
    for i in range (1,50,2):
        a += i
        print(i)
    print(a)
def  for_w():
    for i in range(1, 10):
        for j in range(1, 10):
            print(j, "x", i, "=", i * j, "\t", end="")
            if i == j:
                print("")
                break
def jiujiu():
    for i in range(1,10):
        x = i+1
        for j in range(1,x):
            print('%s * %s = %s'%(j,i,j*i),end='   ')
        print('')

def for_wei():
    wei = 0
    sum2 = 0
    while wei <=100:
        if wei % 2 ==0:
            sum2 += wei
        wei += 1
        print('1-100之间偶数和为：%d' % sum2)

if __name__ == '__main__':
    # for i in range(6):
    # print(i)
    # print('me,too')
    # for_demo()
    # for_list()
    # for_list2()
    # for_break()
    # for_countinue()
    #  sum()
    # for_wei()
    # for_w()
    jiujiu()