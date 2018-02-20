# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-02-13 16:19:22
# @Last Modified by:   Marte
# @Last Modified time: 2018-02-13 17:08:40
games = ['Creative Assembly','CD Projekt Red','Rockstar North']
for game in games:
    print(game.title() + "的游戏我玩过！")#全开头大写
    print("我很期待" + game.title() + "的下一款游戏！\n")

print("我很期待" + games[1].title() + "的下一款游戏！\n")#因为没有缩进，所以只在循环结束后执行一次