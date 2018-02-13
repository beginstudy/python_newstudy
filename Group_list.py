# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-02-12 15:09:13
# @Last Modified by:   Marte
# @Last Modified time: 2018-02-12 16:21:25
game = ["The Witcher3","r6","ARK","Shougun2","Warhammer","Napoleon Total War"]
game.sort()#sort是永久排序
print(game)

game.sort(reverse=True)
print(game)

print("\n这是原来的列表")
print(game)

print("\n这是临时排序过的列表")
print(sorted(game,reverse=True))

print("\n再次输出又是原来的清单")
print(game)

game.reverse()#倒着打印列表
print("\n倒着打印列表")
print(game)

print("\n显示列表game的长度")
print(len(game))

list1 = [123, 'xyz', 'zara']
print("\n显示列表list1的长度")
print(len(list1))


input("Press <enter>")
