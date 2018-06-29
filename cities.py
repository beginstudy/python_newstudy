prompt = "\n请告诉我你来自哪个城市："
prompt += "\n(输入退出以结束问题。)"

while True:
	city = input(prompt)

	if city == '退出':
		break
	else:
		print('我爱' + city.title() + "这座城市!")