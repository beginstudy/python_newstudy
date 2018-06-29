def get_name(firstname,lastname):
	"""返回整洁的姓名"""
	all_name = firstname + '' + lastname
	return all_name.title()

#这是一个无限循环！
while True:
	print("\n请告诉我你的姓名：")
	print("(出入'q'随时可以退出)")
	
	f_name = input("姓氏：")
	if f_name == 'q':
		break

	l_name = input("名字：")
	if l_name == 'q':
		break

	get_formatted = get_name(f_name,l_name)
	print("\n你好！" + get_formatted + "。")