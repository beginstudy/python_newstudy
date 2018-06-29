sandwiches = ['鸡蛋三明治','鸡肉三明治','火腿三明治','蔬菜三明治']
finished_sandwiches = []

while sandwiches:
	current_sandwiches = sandwiches.pop()
	print("我做了你的" +current_sandwiches)
	finished_sandwiches.append(current_sandwiches)

print("\n目前做好的三明治有：")
for finished_sandwiche in finished_sandwiches:
	print(finished_sandwiche)


sandwiches_orders = ['牛肉','牛肉','猪肉','鸡肉','牛肉','猪肉','鱼肉']
print("\n牛肉卖完了！")

while '牛肉' in sandwiches_orders:
	sandwiches_orders.remove('牛肉')
print("\n我们现在只有：" + str(sandwiches_orders))
	