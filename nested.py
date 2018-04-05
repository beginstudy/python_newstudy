# alien_0 = {'color' : 'green', 'points' : 5}
# alien_1 = {'color' :'red', 'points' : 6}
# alien_2 = {'color' : 'blue', 'points' : 14}

# aliens = [alien_0,alien_1,alien_2]

# for alien in aliens:
# 	print(alien)

aliens = []

for alien_number in range(30):#创建30个蓝色外星人
	new_alien = {'color' : 'blue', 'points' :4, 'speed' : 'slow'}
	aliens.append(new_alien)

for alien in aliens[0:4]:
	if alien['color'] == 'blue':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

for alien in aliens[:9]:#遍历前三个外星人
	print(alien)
print("......")

print("创建的外星人个数：" + str(len(aliens)))
