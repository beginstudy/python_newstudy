def pizza(尺寸,*配料):
	print("\n你点的" + str(尺寸) + "寸的披萨配料：")
	for 配料s in 配料:
		print("- " + 配料s)

pizza(16,'蘑菇')
pizza(12,'香菜','火腿','培根')

