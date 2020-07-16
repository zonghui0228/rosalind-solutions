# obtain the data from the web page
def read_data(file):
	import urllib2
	fp = open(file, 'r')
	seq = {}
	for line in fp:
		# print line
		query = line.strip()
		url = 'http://www.uniprot.org/uniprot/' + query + '.fasta'
		# header = {'Host': 'scholar.google.com',
		# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0',-google 1point3acres
		# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		# 'Accept-Encoding': 'gzip, deflate',
		# 'Connection': 'keep-alive'}
		req = urllib2.Request(url) 
		con = urllib2.urlopen(req)
		doc = con.readlines()
		for line in doc:
			if line.startswith('>'):
				seq[query] = ''
			else:
				seq[query] += line.strip('\n')
		con.close()
	return seq

# print read_data("rosalind_pm.txt")

def obtain_motif(file):
	import re
	seq = read_data(file)
	for i in seq.keys():
		motif_point = []
		print i
		# print seq[i]
		p = re.compile(r'N[^P](S|T)[^P]')
		for j in range(len(seq[i])-3):
			# print seq[i][j:j+3]
			if p.match(seq[i][j:j+4]):
				motif_point.append(str(j+1))
		# str1 = ''
		# print motif_point
		print ' '.join(motif_point)
# obtain_motif("rosalind_mprt.txt")

# list1 = [21, 22, 23]
# print ' '.join(list1)





