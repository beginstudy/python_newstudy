kehu = input("请问你们有多少人用餐？")
kehu = int(kehu)

if kehu >= 8:
	print("我们现在没有空桌了！")
else:
	print("欢迎！")


zhengshu = input("请输入数字，让我看看这个数字能不能被10整除。")
zhengshu = int(zhengshu)

if zhengshu %10 == 0:
	print("能被10整除！")
else:
	print("不能被10整除！")