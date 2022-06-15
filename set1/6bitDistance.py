from base64 import b64decode

def countBits(n):
	count = 0
	while (n):
		count += n & 1
		n >>= 1
	return count

f = open("6file.txt", "r")
fileContent = f.read()
fileContent = fileContent.replace("\n", "")
in1 = b64decode(fileContent)
in1len = len(in1)

def bitDif(w1, w2):
	xor = [countBits(a ^ b) for a,b in zip(w1,w2)]
	resBits = 0
	for a in xor:
		resBits += a
	return resBits

for i in range(3, 40):
	print(str(i) + "\t" + str(bitDif(in1[:i],in1[i:2*i])/i))
