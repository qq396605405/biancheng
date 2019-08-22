#判断奇偶数
shuzi=int(input('请输入一个数字'))
if shuzi%2==0:
    print('这是偶数')
else:
    print('这是奇数')


#判断闰年
nianfen=int(input('输入一个年份'))
if nianfen%100==0 and nianfen%400!=0:
    print('不是闰年')
elif nianfen%400==0:
    print('是闰年')
elif nianfen%100!=0 and nianfen%4==0:
    print('是闰年')


#判断质数
shu=int(input('输入一个数字'))
if shu>1:
    for i in range(2,shu):
        if shu%i==0:
            print('不是质数')
            break
    else:
        print('是质数')


#输出指定区域的素数
a=int(input('输入下限'))
b=int(input('输入上限'))
for i in range(a,b+1):
    t=0
    if i>1:
        for j in range(2,i):
            if i%j!=0:
                t=t+1
                if t==i-2:
                    print(i)


#计算阶乘
num=int(input('想计算哪个数字的阶乘'))
def f(x):
    if x==1:
        return 1
    else:
        return f(x-1)*x
print(f(num))



#99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('{0} X {1} = {2}'.format(j,i,i*j),end='  ')
    print('\n')




#斐波那契数列
number=int(input('要几项'))
def f(num):
    if num<=1:
        return 1
    else:
        return f(num-1)+f(num-2)
for i in range(number):
    print(f(i))



#如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153。检验某个数是否是阿姆斯特朗数
n=int(input('你要输入的是几位数'))
number=int(input('请输入你的数字'))
number_list=list(str(number))
sum=0
for i in range(len(number_list)):
    sum=sum+int((number_list[i]))**len(number_list)
if sum==number:
    print('这个数是阿姆斯特朗数')
else:
    print('这个数不是阿姆斯特朗数')


#十进制转二进制、八进制、十六进制
dec = int(input("输入数字："))
print("十进制数为：", dec)
print("转换为二进制为：", bin(dec))
print("转换为八进制为：", oct(dec))
print("转换为十六进制为：", hex(dec))


#最大公约数算法(两个数)
def gongyue(x,y):
    if x<y:
        smaller=x
    else:
        smaller=y
    for i in range(1,smaller+1):
        if x%i==0 and y%i==0:
            hcf=i
    return hcf
print(gongyue(12,16))

#最小公倍数
def gongbei(x,y):
    if x<y:
        smaller=x
    else:
        smaller=y
    for i in range(1,smaller+1):
        if x%i==0 and y%i==0:
            hcf=i
    gongbeishu=(x*y)/hcf
    return gongbeishu
print(gongbei(12,16))


#30 个人在一条船上，超载，需要 15 人下船。于是人们排成一队，排队的位置即为他们的编号。报数，从 1 开始，数到 9 的人下船。
#如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？


def yuesefu(nums, step, stay):
    #参数 nums：人数，step: 数到几的步数，stay: 最后留下多少人
    lists = list(range(1, nums+1))
    check = 0
    while len(lists) > stay:
        for i in lists[:]:
            check += 1
            if check == step:
                check = 0
                lists.remove(i)
                print("{}号下船了".format(i))
    return lists
stays = yuesefu(30, 9, 15)
print("最后留下的人：", stays)

#计算n个数的立方和

def lifanghe(number):
    he=0
    for i in range(number+1):
        he=he+i**3
    return he
print(lifanghe(3))

import numpy as np
a=np.array([1,2,3])


#检查一字符串是否存在于另一字符串
string = "www.runoob.com"
sub_str ="runoob"
if string.find(sub_str,50)==-1:
    print('不存在')
else:
    print('存在')


#利用正则表达式找出字符串中的URL
import re
string = 'Runoob 的网页地址为：https://www.runoob.com，Google 的网页地址为：https://www.google.com'
def f(str):
    res=re.findall(r'https://.*?com',str)
    return res
print(f(string))


#字符串逆序输出
str='xuyang'
str[::-1]
print(reversed(str))


L=[('b',3),('a',5),('c',7),('d',6)]
print(sorted(L, key=lambda x:x[1]) )              # 利用key

key_value = {}

# 初始化
key_value[2] = 56
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18
key_value[3] = 323

print("按值(value)排序:")
print(sorted(key_value.items(), key=lambda kv: (kv[0], kv[1])))

#打印当前时间并转化为标准格式
import time
import datetime
t=datetime.datetime.now()
print(t.strftime('%Y-%m-%d %H:%M:%S'))
dela=datetime.timedelta(1)  #一天时间

import numpy as np
arr=np.array([1,2,3])
arr[1]=arr[2]