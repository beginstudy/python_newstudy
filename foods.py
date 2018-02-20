# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-02-19 13:36:53
# @Last Modified by:   Marte
# @Last Modified time: 2018-02-19 13:51:21
players = ['麦克','马丁','科利尔','佛伦斯','杰克']

print("这是我对的前三名球员：")
for player in players[:3]:
    print(player)

my_foods = ['pizza','falafel','carrot','cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)