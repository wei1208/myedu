import json
adict = {"username":"yansl","password":"123456"}
bdict = {5:"yansl","password":[2,5]}
cdict_str = '{"username":"yansl","password":"123456"}'

# 查询字典中的元素
def dict_sel():
    # 通过Key来访问，sky可以时候str类型，一可以是int类型
    print(adict['username'])
    print(bdict[5])
# 将访问到的值，可以重新赋予值给新的
    b = bdict['password']
    print(b)
# 删除字典中的元素
def dict_del():
    adict.pop('password')
    print(adict)
def dict_add():
    # 方法一
    # 字典中的key 不能重复 ，相同key只取括号里面的值
    # 方式二
    # 使用dict()时，两个字典中
    adict.update(bdict)
    print(adict)





def dict_update():
    adict['username'] = '吴学伟'
    print(adict)
    adict.update(bdict)
    print(adict)
    adict['passwrod'] = '2224153253'
    print(adict)
#增加字典中的元素
def dict_add1():
    adict['sex'] = '男'
    print(adict)
# 字典转换字符串  json.dumps()
def dict2str():
    print(type(adict))
    # 将adict 转换成 字符串类型 再重新赋值 给adict_str
    adict_str = json.dumps(adict)
    print(adict_str)
    print(type(adict_str))
# 字符串转换字典 json.loads()
def str2dict():
    print(type(cdict_str))
    # 将cdict_str 转换成字典 再重新赋值给cdict_str
    cdict = json.loads(cdict_str)
    print(cdict)
    print(type(cdict))


if __name__ == '__main__':
    #dict_sel()

    #dict_del()
    #dict_update()
    #dict_add()
    #dict_add1()
    #dict2str()
    str2dict()