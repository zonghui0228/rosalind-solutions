# coding:utf-8
# Overlap Graphs

# Sample Dataset
# >Rosalind_0498
# AAATAAA
# >Rosalind_2391
# AAATTTT
# >Rosalind_2323
# TTTTCCC
# >Rosalind_0442
# AAATCCC
# >Rosalind_5013
# GGGTGGG

# Sample Output
# Rosalind_0498 Rosalind_2391
# Rosalind_0498 Rosalind_0442
# Rosalind_2391 Rosalind_2323

def read_fasta(file):                                #把fasta文件读入seq
	fp = open(file, 'r')
	seq = {}
	for line in fp:
		if line.startswith('>'):
			name = line.replace('>', '')
			name = name.replace('\n', '')
			seq[name] = ''
		else:
			seq[name] += line.replace('\n', '')
	fp.close()
	return seq

def graph(list_name, list_string):                                   #循环比较，窗口为1
	for i in range(len(list_name)): 
		for j in range(len(list_string)):
			if(i != j):
				if list_string[i][-3:] == list_string[j][:3]:        #窗口设置为n,则分别为[-n:],[:n], there n=3
					print list_name[i], list_name[j]

def main():                                                 
	seq = read_fasta("rosalind_grph.txt")
	list_name = []
	list_string = []
	for i in seq.keys():                 # 把seq中的序列读入两个list
		list_name.append(i)              # list_name里面包含序列名字
		list_string.append(seq[i])       # list_string里面包含对应字符串序列
	# print list_name
	# print list_string
	graph(list_name, list_string)
# main()