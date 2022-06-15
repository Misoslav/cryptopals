from string import ascii_lowercase, whitespace, printable
from collections import Counter
from re import sub
from base64 import b64decode
from itertools import product
freq = [8.2, 1.5, 2.8, 4.3, 13, 2.2, 2, 6.1, 7, 0.15, 0.77, 4, 2.4, 6.7, 7.5, 1.9, 0.1, 6, 6.3, 9.1, 2.8, 1, 2.4, 0.15, 2, 0.07]
abc = [a for a in ascii_lowercase]

f = open("6file.txt", "r")
fileContent = f.read()
fileContent = fileContent.replace("\n", "")
in1 = b64decode(fileContent)
in1len = len(in1)

def countFreq(byteIn):
	global abc, freq, in1len
	value = 0
	try:
		letterCount = Counter(byteIn.decode())
		for letter, letterFreq in zip(abc, freq):
			#if float(letterCount[letter])/in1len*100 >= letterFreq * 0.7 - 1 and letterCount[letter] <= letterFreq * 1.3 + 1:
			#	value += 1
			value += (float(letterCount[letter])/in1len*100 - letterFreq)**2
		#return value		
		return (value/len(abc))**0.5
	except:
		return 100

for keyLen in range(29, 30):
	print(keyLen)
	outAr = [[] for i in range(keyLen)]
	for i in range(keyLen):
		for char in range(128):
			byteOut = bytes([char ^ a for a in in1[i::keyLen]])
			try:
				strVal = countFreq(byteOut.decode().lower().encode())
			except:
				continue
			strOut = sub("[" + whitespace + "]", ' ', byteOut.decode())
			for char in strOut:
				if char not in printable:
					break
				if char in ";#\\$&~[]<>`":
					break
			else:
				outAr[i].append((strVal, strOut, char))		
	for i in range(keyLen):
		outAr[i].sort(key=lambda x: x[0], reverse=True)
	out1 = []
	outFreq = 0
	for i in range(keyLen):
		outFreq += outAr[i][0][0]
	outFreq /= keyLen
	for i in range(in1len):
		out1.append(outAr[i%keyLen][0][1][i//keyLen])
	print("".join([outAr[i][0][2] for i in range(29)]))
	print(str(outFreq) + "  " + "".join(out1))
