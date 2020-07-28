# ^_^ coding:utf-8 ^_^

"""
Finding a Protein Motif
url: http://rosalind.info/problems/mprt/

Given: At most 15 UniProt Protein Database access IDs.
Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.
"""

import urllib2

# obtain the data from the web page
def read_data(file):
    fp = open(file, 'r')
    seq = {}
    for line in fp:
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
    fp.close()
    return seq

def obtain_motif(file):
    import re
    seq = read_data(file)
    for i in seq.keys():
        motif_point = []
        p = re.compile(r'N[^P](S|T)[^P]')
        for j in range(len(seq[i])-3):
            if p.match(seq[i][j:j+4]):
                motif_point.append(str(j+1))

        print(' '.join(motif_point))
        return motif_point

if __name__ == "__main__":
    obtain_motif("../data/rosalind_mprt.txt")
