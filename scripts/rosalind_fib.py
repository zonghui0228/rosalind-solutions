Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #斐波那契函数，初始数目为n，增长率为k,
>>> def fib(n,k):
	if n<=2:
		return 1;
	else:
		return fib(n-1,k)+k*fib(n-2,k);

	
>>> fib(5,3)
19
>>> fib(32,3)
108412748857L
>>> fib(34,4)
18788331166609L
>>> 
