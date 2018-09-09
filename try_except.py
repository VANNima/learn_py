try:
	p=input("请输入一个整数")
	result = eval(p)**2
	print(result)
except NameError:
	print("输入出错")
else:
	print("输入对了")