import cbc, os
from Crypto.Cipher import AES
from random import randint

blocksize = 16
pad = lambda x: x + ((blocksize-len(x)%blocksize)*chr(blocksize-len(x)%blocksize)).encode()
countDistincts = lambda x: len(set([x[blocksize*i:blocksize*(i+1)] for i in range(len(x)//blocksize)]))
f = open("10file.txt", "r")
fileContent = f.read()
fileContent = "\x00" * 1000
fileContent = fileContent.encode()

def randEncrypt():
	global fileContent
	randVal = randint(0,1)
	key = os.urandom(16)
	randPad = os.urandom(randint(5,10))
	in1 = randPad + fileContent + randPad
	in1 = pad(in1)
	if randVal == 1:
		cipher = AES.new(key, AES.MODE_ECB)
		cipherText = cipher.encrypt(in1)
	else:
		IV = os.urandom(blocksize)
		cipherText = cbc.encrypt(in1, key, IV)
	return randVal, cipherText

for i in range(100):
	realVal, cipherText = randEncrypt()
	guessedVal = int(countDistincts(cipherText) < len(cipherText)//blocksize)
	if guessedVal != realVal:
		print(cipherText)
