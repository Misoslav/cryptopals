f = open("8file.txt", "r")
block_len = 32
out = []
for line in f.readlines():
	line = line.strip()
	out.append((len(set([line[block_len*i:block_len*(i+1)] for i in range(len(line)//block_len)])), line, set([line[4*i:4*i+block_len] for i in range(len(line)//block_len)])))
out.sort(key=lambda x: x[0], reverse=True)
for i in out:
	print(i)
