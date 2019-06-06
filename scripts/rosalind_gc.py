# python3


# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

def gc(file):
	gc_contents = {}
	strings = {}
	with open(file, 'r') as f:
		for line in f:
			line = line.strip()
			if line.startswith(">"):
				id = line.replace(">", "")
				strings[id] = ""
			else:
				strings[id] += line
	for k in strings.keys():
		gc_content = (strings[k].count("G") + strings[k].count("C")) / float(len(strings[k]))
		gc_contents[k] = gc_content
	gc_contents = sorted(gc_contents.items(), key=lambda d: d[1], reverse = True)
	highest_gc = gc_contents[0]
	return highest_gc


if __name__ == "__main__":
	highest_gc = gc("../data/rosalind_gc.txt")
	print(highest_gc[0])
	print(highest_gc[1]*100)