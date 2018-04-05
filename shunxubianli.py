favorite_languages = {
	'博姆特' : 'python',
	'塔瓦塔' : 'C++',
	'依德娃德' : 'C',
	'莎拉' : 'Java',
}

for name in sorted(favorite_languages.keys()):#sorted是按照顺序遍历字典中所有的键
	print(name.title() + "，谢谢你告诉我。")

print("\n" + "这些学生最喜欢的语言分别是：")
for zhi in favorite_languages.values():#values遍历字典中所有的值
	print(zhi.title())

for name,yuyan in favorite_languages.items():#items是遍历字典中所有的键-值
	print("名字：" + name)
	print("语言：" + yuyan)

for name in favorite_languages.keys():#keys是遍历字典中所有的键
	print("名字:" + name)


water = {
	'长江' : '中国',
	'黄河' : '中国',
	'尼罗河' : '埃及',
	'恒河' : '印度',
}

for nile,egypt in water.items():
	print("河流：" + nile)
	print("国家：" + egypt)

for nile in water.keys():
	print("\n河流：" + nile)

for egypt in water.values():
	print("所属国家：" + egypt) 

print("三大河流所经过的国家：" )
for country in set(water.values()):#set(集合)让提取的值不重复
	print( country.title())