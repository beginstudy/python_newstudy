number = input("输入一个数字，让我判定这是一个奇数还是偶数：")
number = int(number)

if number %2 == 0:#如果这个数字被2整除等于0，没有余数，那么...
	print("\n这个数字：" + str(number) + "是偶数。")
else:#否则...
	print("\n这个数字：" + str(number) + "是奇数。")
