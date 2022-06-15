import os
from Crypto.Cipher import AES
from base64 import b64decode
from string import printable
from random import randint
import math

blocksize = 16
block = lambda x, y: x[y*blocksize:(y+1)*blocksize]
pad = lambda x: x + ((blocksize-len(x)%blocksize)*chr(blocksize-len(x)%blocksize)).encode()
unpad = lambda x: x[:-x[-1]]

randBytes = os.urandom(randint(0,16))
key = os.urandom(16)
secret = "Ahoj jak se mas???".encode()
def oracle(x):
	global randBytes
	cipher = AES.new(key, AES.MODE_ECB)
	return cipher.encrypt(pad(randBytes + x.encode() + secret))

#----------------------------------
def getPreLen():
	global blocksize
	orig = oracle("")
	prelen = 0
	while True:
		if block(orig, prelen) == block(oracle("a"), prelen):
			prelen += 1
		else:
			break
	#prelen *= blocksize
	for i in range(blocksize):
		if block(oracle("a"*i+"b"), prelen) == block(oracle("a"*i+"c"), prelen):
			prelen *= blocksize
			prelen += blocksize - i			
			break
	return prelen

def breakOracle():
	plaintext = ""
	preLen = getPreLen()
	preBlocks = math.ceil(preLen/blocksize)
	secretLen = len(oracle("")) - preLen
	for i in range(secretLen):
		currentFill = "a"*(blocksize - preLen%blocksize) + "*"*(blocksize-1-i%blocksize)
		match = oracle(currentFill)
		for j in printable:
			if match[(i//blocksize+preBlocks)*blocksize:(i//blocksize+1+preBlocks)*blocksize] == oracle(currentFill + plaintext + j)[(i//blocksize+preBlocks)*blocksize:(i//blocksize+1+preBlocks)*blocksize]:
				plaintext += j
				break
	print(plaintext)

breakOracle()
