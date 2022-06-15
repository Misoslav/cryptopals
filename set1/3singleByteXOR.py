from string import ascii_lowercase, whitespace
from collections import Counter
from re import sub
freq = [8.2, 1.5, 2.8, 4.3, 13, 2.2, 2, 6.1, 7, 0.15, 0.77, 4, 2.4, 6.7, 7.5, 1.9, 0.1, 6, 6.3, 9.1, 2.8, 1, 2.4, 0.15, 2, 0.07]
abc = [a for a in ascii_lowercase]
in1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
in1b = bytes.fromhex(in1)
in1c = Counter(in1b.decode())
in1len = len(in1b)

def countFreq(byteIn):
	global abc, freq, in1len
	value = 0
	letterCount = Counter(byteIn.decode())
	for letter, letterFreq in zip(abc, freq):
		#if float(letterCount[letter])/in1len*100 >= letterFreq * 0.7 - 1 and letterCount[letter] <= letterFreq * 1.3 + 1:
		#	value += 1
		value += (float(letterCount[letter])/in1len*100 - letterFreq)**2
	return (value/len(abc))**0.5

outAr = []

for char in range(128):
	byteOut = bytes([char ^ a for a in in1b])
	strVal = countFreq(byteOut.decode().lower().encode())
	strOut = sub("[" + whitespace.replace(" ", "") + "]", '', byteOut.decode())
	outAr.append((strVal, strOut))

outAr.sort(key=lambda x: x[0], reverse=True)
for x in outAr:
	print(str(x[0]) + " " + x[1])

