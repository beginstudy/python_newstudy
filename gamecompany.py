# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-02-10 15:33:01
# @Last Modified by:   Marte
# @Last Modified time: 2018-02-10 16:14:25
gamecompany = ['育碧','R星','水雷','P社','B社']
#print(gamecompany)

gamecompany[2] = '暴雪'
print(gamecompany)

gamecompany.append('红鸟')
print(gamecompany)

gamecompany = []

gamecompany.append('暴雪')
gamecompany.append('R星')
gamecompany.append('P社')
gamecompany.append('B社')
print(gamecompany)

gamecompany = ['R星','暴雪','P社']
gamecompany.insert(1,'B社')
print(gamecompany)

del gamecompany[1]
print(gamecompany)

input("Press <enter>")
