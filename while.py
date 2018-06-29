current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1#将current_number的值加1


prompt = "\n告诉我一些事，和我将返回你一条信息："
prompt += "\n输入 '退出' 结束这个问题。"
message = ""
while message != '退出':
	message = input(prompt)

	if message != "退出":
		print(message)