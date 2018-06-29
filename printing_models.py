"""#首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_model = []"""
def print_models(unprinted_designs,completed_models):

	#模拟打印每个设计，知道没有未打印的设计为止
	#打印每个设计后，都将其移到列表completed_models中
	while unprinted_designs:
		current_design = unprinted_designs.pop()

		#模拟根据设计制作3D打印模型的过程
		print("打印好的MOD：" + current_design)
		completed_models.append(current_design)

def show_models(completed_models):
#显示打印好的所有模型
	print("\n所有打印好的MOD都在这里：")
	for MODs in completed_models:
		print(MODs)

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

print_models(unprinted_designs[:],completed_models)
show_models(completed_models)