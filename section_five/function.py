'''def fact(n,m=1):
	s=1
	for i in range(1,n+1):
		s=s*i
	return s//m
a=fact(10,2)'''
s = 2
ls = ["f","F"]#通过使用[]创建了一个全局变量列表
def fact(n,*b):
	global s#全局变量
	#组合数据类型，没有在函数中创建的话，是跟全局变量有关
	for i in range(1,n+1):
		s=s*i
	for item in b:
		s*=item
	return s,item
(a,b)=fact(10,3)#元组类型
print(a,b)
'''f = lambda x,y:x+y
a = f(1,2)#慎用 特殊情况使用
print(a)'''