def recursion(a):
	if a == 0:
		return 1
	else:
		return a*recursion(a-1)
def fact(s):
	if s == "":
		return s
	else:
		return fact(s[1:])+s[0]
def f(n):#费波纳基数列
	if n==1 or n==2:
		return 1
	else:
		return f(n-1)+f(n-2)
#汉诺塔问题
count = 0
def hanoi(n,src,dst,mid):#圆盘数量 原来的主子 目的柱子 中间柱子
	global count
	if n==1:
		print("{}:{}->{}".format(1,src,dst))
		count += 1
	else:
		hanoi(n-1,src,mid,dst)
		print("{}:{}->{}".format(n,src,dst))
		count += 1
		hanoi(n-1,mid,dst,src)

hanoi(5 ,'A','C','B')
print(count)