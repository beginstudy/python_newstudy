favorite_languages = {
	'jen' : 'python',
	'sarah' : 'C++',
	'edward' : 'Java',
	'phil' : 'python'
}

print("Sarah's favorite languages is " + favorite_languages['sarah'].title() + ".")

user_0 = {
	'username' : 'efermi',
	'first' : 'enrico',
	'last' : 'fermi',
}

for key, value in user_0.items():
	print("\nkey: " + key.title())
	print("value: " + value.upper())

for name, languages in favorite_languages.items(): #将键放在变量name里，将值放在变量languages里，然后for循环遍历favorite_languages字典
	print("\n" + name.title() + "'s favorite languages is " + languages.title() + ".")

for name in favorite_languages.keys():
	print(name.title())

friends = ['phil','sarah']
for name in favorite_languages.keys():
	print("\n"+name.title())

	if name in friends:
		print("你好！" + name.title() + ",我发现你最喜欢的语言是：" + favorite_languages[name].title() + "!")

	if 'erin' not in favorite_languages:
		print("Erin,请你接受调查！")