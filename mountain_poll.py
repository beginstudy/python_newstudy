responses = {}

#设置一个标志，指出调查是否继续
投票活动 = True

while 投票活动:
	#提示输入被调查者的名字和回答
	name = input("\n请问你的名字是？")
	response = input("你想住多少天？")

	#将答卷存储在字典中
	responses[name] = response

	#看看是否还有人要参与调查
	repeat = input("还有人要参与调查吗？(yes/no)")
	if repeat == 'no':
		投票活动 = False

	#调查结束，显示结果
	print("\n---调查结果---")
	for name,response in responses.items():
		print(name + "想住" + response + '天。')