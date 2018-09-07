TempStr = input("请输入带有富豪的温度数值：")
if TempStr[-1] in ['f','F']:
	print(TempStr)
	C = (eval(TempStr[0:-1]) - 32)/1.8
	print(format(C))
elif TempStr[-1] in ['C','c']:
	F = 1.8*eval(TempStr[0:-1]) + 32
	print(format(F))
else:
	print("wrong")
