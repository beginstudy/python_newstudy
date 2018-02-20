# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-02-19 13:54:13
# @Last Modified by:   Marte
# @Last Modified time: 2018-02-19 14:13:15
dimensions = (200,50)#这次练习元组,元组不可变，且用圆括号标识
print(dimensions[0])
print(dimensions[1])

numbers = (123,456,789)
for number in numbers:
    print(number)

print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,60)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)