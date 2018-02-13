# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-02-10 16:17:47
# @Last Modified by:   Marte
# @Last Modified time: 2018-02-12 14:49:04
music = ['《LUA》','《Stand By me》','《久远 -光と波の记忆-》','《Wake》','《The Source》','《Berceau》']
print(music)

del music[3]
print(music)

music.insert(3,'《Wake》')

music.append('《Fairy Dolce》')

print(music)

#music = ['《LUA》', '《Stand By me》', '《久远 -光と波の记忆-》', '《Wake》', '《The Source》', '《Berceau》', '《Fairy Dolce》']
#print(music)

popped_music = music.pop()
print(music)
print(popped_music)

last_music = music.pop(2)
print("我最后听的一首歌是：" + last_music.title() + "。")
print(music)

too_music = '《Wake》'
music.remove(too_music)
print(music)
print("\n删除" + too_music.title())

input("Press <enter>")