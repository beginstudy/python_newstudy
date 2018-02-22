# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-02-22 21:02:07
# @Last Modified by:   Marte
# @Last Modified time: 2018-02-22 21:53:04
answer = 17
if answer !=42:
    print("That is not the correct answer.Please try again!")

age = 19
if age == 18:
    print("true")
if age != 18:
    print("false")
if age < 25:
    print("bufuhe")

age = 50
if age >= 40:
    print("keyi")

age_0 = 26
age_1 = 16
if age_0 >=21 and age_1 >=21:
    print("true")
else:
    print("false")

age_1 = 23
if age_0 >=21 and age_1 >=21:
    print("true")

if age_0 <=30 or age_1 <=16:
    print("tongguo")

requested_toppings = ['mushrooms','onions','pineapple']
if 'mushrooms' in  requested_toppings:
    print("true")

if 'bannane' not in requested_toppings:
    print('false')

banned_used = ['andrew','carolina','david']
user = 'marie'

if user not in banned_used:
    print(user.upper() + ",you can post a response if you wish.")