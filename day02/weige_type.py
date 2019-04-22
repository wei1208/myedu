# 查询或者获取list 里面的值(元素)
# a[索引]: 或者叫下标值  元素从0开始数
def list_sel(w):
    print(w[2])
    print(w[0:2])
    print(w[1:4])
    print(w[-2:2])

def list_del():
    # 定义一个list
    qlist = ['a', 4, 'nihao', '8', '就是', '哈','你好']
    # 调用删除方法 不填参数 默认删除最后一位
    qlist.pop()
    print(qlist)
    qlist.pop(3)
    print(qlist)
     # 将切片获取的 元素 重新定义一个list 保存起来
    alist = qlist[:-3]
    print(alist)
    alist = qlist[2:3]
    print(alist)
def list_add():
    wlist = ['w','x','wei','88','伟']
    # 增加元素 ,增加在末尾

    wlist.append('10086')
    print(wlist)
    wlist.append('你好')
    print(wlist)
    # 元素更换位置
    # 更改list中的元素
def list_update():
    wlist = ['a', 4, 'nihao', '8', '就是', '哈', '哈哈哈哈', [1, 2, 3]]
    wlist[0] = '8'
    print(wlist)
    wlist[-2] = '10086'
    print(wlist)
# 查询字典中的元素
adict = {"username":"yansl","password":"123456"}
bdict = {'5':"yansl","password":[2,5]}
def dict_sel():
    print(adict['username'])
    b = bdict['password']
    print(b)
    bdict['password'] = '2224153253'
    print(bdict)





if __name__ == '__main__':
    #wlist = ['wuxuewei','吴学伟','2224153253','ylgyu']
    #list_sel(wlist)
    #list_del()
    #list_add()
    # list_update()
    dict_sel()