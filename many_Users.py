users = {
	'alan': {
		'first' : 'alan',
		'last' : 'einstein',
		'location' : 'princeton',
	},

	'mcurie': {
		'first' : 'marie',
		'last' : 'curie',
		'location' : 'paris',
	},
}

for username,user_info in users.items():#遍历字典user，让每个键依次存储在变量username中，并以此将于当前键相关联的字典存储在变量user_info中
	print("\nUsername:" + username)
	full_name = user_info['first'] + "" + user_info['last']
	location = user_info['location']

	print("\tFull name:" + full_name.title())
	print("\tLocation:" + location.title())