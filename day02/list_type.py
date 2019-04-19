
def list_sel(b):


    # print(b[-1])
    # print(b[2:5])
    # print(b[0:2])
    # print(b[:4])
    # print(b[2:4])
    # print(b[2:])
      print(b[5:])
def list_del():
    alist = ['a', 4, 'nihao', '8', '你好', '哈哈', '伟']
    alist.pop()
    print(alist)
    alist.pop(3)
    print(alist)
    blist = alist[:-3]
def list_add():
    alist = ['a', 4, 'nihao', '8', '你好', '哈哈', '伟']
    alist.append('哈哈哈哈')
    print(alist)
    blist = [1,2,3,4]
    alist.append(blist)
    print(alist)
    alist[0] = 5
    print(alist)
def list_update():
    alist = ['a', 4, 'nihao', '8', '你好', '哈哈', '伟']
    alist[3] = '伟'
    print(alist)
# 替换
if __name__ == '__main__':
    alist = ['a',4,'nihao','8','你好','哈哈','伟']
    # list_del()
    # list_add()
    # list_update()
    # 长度
    print(len(alist))