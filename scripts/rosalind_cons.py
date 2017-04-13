#coding:utf-8
import os
import re
import string
os.chdir('C:\\Users\\sony\\Desktop')
#print os.getcwd()
data = open('C:\\Users\\sony\\Desktop\\rosalind_cons.txt')
line_count = 0
lenstring = 0
list = []
str2 = ''
for line in data:
    #print line
    p = re.compile(r'[^>]')
    match = p.match(line)
    if match:
        str1 = line
        str1 = str1.strip('\n')
        str2 += str1
        #print str2
        #lenstring = len(str2)
        #print lenstring
        #print str1
        #list.append(str1)
    else:
        lenstring = len(str2)
        #print lenstring
        list.append(str2)
        line_count += 1
        #print line_count
        str2 = ''
list.append(str2)
#print list
list.pop(0)
#print len(list)
#print line_count  #rows
#print lenstring   #cols
#print list[0][0]
string = ''
listA = ['A:']
listC = ['C:']
listG = ['G:']
listT = ['T:']
for i in range(lenstring):
    countA,countC,countG,countT = 0,0,0,0
    for j in range(line_count):
        if (list[j][i] == 'A'):
            countA += 1
        elif (list[j][i] == 'C'):
            countC += 1
        elif (list[j][i] == 'G'):
            countG += 1
        elif (list[j][i] == 'T'):
            countT += 1
    #print countA ,countC,countG,countT

    max1 = max(countA,countC,countG,countT)
    if max1 == countA:
        string += 'A'
    elif max1 == countC:
        string += 'C'
    elif max1 == countG:
        string += 'G'
    elif max1 == countT:
        string += 'T'
    listA.append(str(countA))
    listC.append(str(countC))
    listG.append(str(countG))
    listT.append(str(countT))
f = file('rosalind.txt','w')
f.write(string)
f.write('\n')
f.write(" ".join(listA))
f.write('\n')
f.write(" ".join(listC))
f.write('\n')
f.write(" ".join(listG))
f.write('\n')
f.write(" ".join(listT))
f.close()
