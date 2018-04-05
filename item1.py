alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

alien_0 = {'color':'green'}
print("这个字典是：" + alien_0['color'] + '.')

alien_0['color'] = 'yellow'
print("这个字典现在是：" + alien_0['color'] + '.')



alien_0 = {'x_position': 0,'y_position':25,'speed':'fast'}#访问字典alien_0中的键speed(速度)，值为快
print("最初的 x_position:" + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':#如果向右移动速度为slow
	x_increment = 1#将1存储到变量x_increment中
elif alien_0['speed'] == 'medium':#如果速度为medium
	x_increment = 2#将2存储到变量x_increment中
elif alien_0['speed'] == 'fast':
	x_increment = 3

alien_0['x_position'] = x_increment#确定x的移动量+X的原始位置，并关联到字典中的x_position
print("新 X坐标：" + str(alien_0['x_position']))

alien_1 = {'color' : 'green','points' : 5,'wula!!!' : 3}
print(alien_1)

del alien_1['wula!!!']
print(alien_1)