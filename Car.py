#coding:utf-8

print("中文编码需要上面的一句设置，一般放到最开始")

print ('Hello,World!')

print ("Hello'World!")

print ('Hello"World!')

import this

import math

print (math.sin(math.pi/2))

print (5*2)

apple_price = 5
apple_weight = 2
apple_cost = apple_price * apple_weight
print (apple_cost)

print("appleCost:{}".format(apple_cost))

a = 10
b = 20
a, b = b, a
print ("a is {}, b is {}".format(a, b))

print (100/3.0)
print (round(100/3.0, 3))

#乘方
print (math.pow(3, 10))
print (3 ** 10)

#角pi..
print(math.radians(180))

print(min(1, 4, 9, 5, 6))

print(sum([1, 4, 9, 5, 6]))

print(divmod(10, 3)) #返回（商，余数）

print(10 > 3)

#and or !
print(False or True and True)

line = '你好！'
line2 = '小姐姐 '
print(line+line2)
print(line+line2*2) #字符串的乘法
print(len(line2)) #字符串是不可变类型的变量
print(id(line2)) #内存地址

#切片
string = 'ni hao! hello,world!'
print(string[0:10:2]) #开始位置：到第几个：步长
print(string[-10:]) #取后10个
print(string[::-1]) #翻转字符串

print(string.capitalize()) #首字母大写函数
print(string.center(10,'-'))
print(string.center(30,'-'))
print(string.count('o'))
print(string.startswith('n'))
print(string.endswith('n'))
print(string.find('o'))
print(string.find('z'))

#列表
varibals = [1, 'hello', 2, 'world']
varibals1 = list()
varibals1.append(1)
print(varibals1)
varibals1.append('1')
print(varibals1)
varibals1.append(varibals)
print(varibals1)
varibals1[0] = 10
print(varibals1)

aaa = [1, 2, 6, 3, 7]
varibals.sort()
print(varibals)

