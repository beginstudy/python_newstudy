prompt = "如果你要告诉我你是谁，请先打印出一条信息。"#将消息存储在prompt中
prompt += "\n你的名字是？"#运算符+=在上一个字符串后面附加一个字符串。

name = input(prompt)
print("\n你好，" + name + "!")