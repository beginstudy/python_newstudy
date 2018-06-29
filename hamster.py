def pet(petname,animaltype='猫'):
	"""显示宠物信息"""
	print("\n我有一只" + animaltype + "。")
	print("它的名字叫" + petname + "。")

pet('仓鼠','杰克')
pet('猫', '提米')
pet(petname='小崔',animaltype='狗')
pet(petname='willie')
pet(animaltype='乌龟',petname='milk')

def describe_pet(pet_name='安尼莫',animal_type='蛇'):
	print("\n我有一只" + animal_type + "。")
	print("它的名字叫" + pet_name + "。")

describe_pet()