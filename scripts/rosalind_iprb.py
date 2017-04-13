Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #k个AA,m个Aa，n个aa，随机拿两个，求子代含有A的概率
>>> def pro(k,m,n):
	i=m*m+4*n*n+4*m*n-4*n-m
	j=4*(k+m+n)*(k+m+n-1)
	return 1-float(i)/j

>>> pro(2,2,2)
0.7833333333333333
>>> pro(24,20,30)
0.7102924842650871
>>> 
