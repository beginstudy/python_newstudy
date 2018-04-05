favorite_languages = {
	'jen' : ['python','ruby'],
	'sarah' : ['C'],
	'jack' : ['ruby','go'],
	'sam' : ['C++','Java'],
}

for name,languages in favorite_languages.items():
	 print("\n" + name.title() + "最喜欢的语言只有：")
	 for language in languages:
	 	print("\t" + language.title())