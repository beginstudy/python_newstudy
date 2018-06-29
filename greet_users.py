def greet_users(names):
	"""想列表中的每位用户都发出简单的问候"""
	for name in names:
		msg = "你好！" + name + "!"
		print(msg)

usernames = ['蕾哈娜' ,'太阳','马沟']
greet_users(usernames) 