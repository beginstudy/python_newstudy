prompt = "\n告诉我一些事，我将返回你一条消息："
prompt += "\n输入'退出'以结束问题。"

active = True#这个变量active就是标志
while active:
	message = input(prompt)

	if message == '退出':
		active = False
	else:
		print(message)