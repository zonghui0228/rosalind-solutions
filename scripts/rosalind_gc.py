Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> fp=open('C:\\Users\\sony\\Desktop\\rosalind_gc.txt','r')
>>> str=fp.read()
>>> list=str.split('>')
>>> del list[0]
>>> dict={}
>>> for i in range(len(list)):
	dict[list[i][0:13]]=float(list[i].count('C')+list[i].count('G'))/(list[i].count('A')+list[i].count('T')+list[i].count('C')+list[i].count('G'))


	
>>> 
KeyboardInterrupt
>>> print sorted(dict.items(), key=lambda d: d[1])
[('Rosalind_5573', 0.4962871287128713), ('Rosalind_4480', 0.5028636884306987), ('Rosalind_8391', 0.5062571103526735), ('Rosalind_8944', 0.5069605568445475), ('Rosalind_8470', 0.5096153846153846)]
>>> 
