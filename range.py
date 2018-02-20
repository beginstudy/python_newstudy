# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-02-15 13:31:06
# @Last Modified by:   Marte
# @Last Modified time: 2018-02-17 16:35:54
for value in range(1,5):
    print(value)

numbers = list(range(2,8))
print(numbers)

odd_numbers =list(range(3,18,3))#odd是奇数
print(odd_numbers)

cubics = []#cubic是立方
for value in range(1,5):
    cubic = value**3#此处的cubic是临时变量
    cubics.append(cubic)
print(cubics)

#以下是简化代码
for value in range(1,7):
    cubics.append(value**3)
print(cubics)
print(min(cubics))
print(max(cubics))
print(sum(cubics))

input("Press <enter>")