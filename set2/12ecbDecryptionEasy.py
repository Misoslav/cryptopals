import cbc, os
from Crypto.Cipher import AES
from base64 import b64decode
from string import printable 

blocksize = 16
pad = lambda x: x + ((blocksize-len(x)%blocksize)*chr(blocksize-len(x)%blocksize)).encode()
secret = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
key = os.urandom(16)
secret = b64decode(secret).decode()

def oracle(p):
	in1 = p + secret
	in1 = pad(in1.encode())
	cipher = AES.new(key, AES.MODE_ECB)
	return cipher.encrypt(in1)

def getBlockSize():
	orig = oracle("")
	for i in [8, 16, 24, 32]:
		if orig == oracle(i * "a")[i:]:
			return i
	return 0

def detectEcb(blocksize):
	c = oracle("a"*blocksize*2)
	if c[:blocksize] == c[blocksize:2*blocksize]:
		return True
	else:
		return False

def breakOracle():
	blocksize = getBlockSize()
	assert detectEcb(blocksize)
	plaintext = ""
	secretLen = len(oracle(""))
	for i in range(secretLen):
		currentFill = "*"*(blocksize-1-i%blocksize)
		match = oracle(currentFill)
		for j in printable:
			if match[(i//blocksize)*blocksize:(i//blocksize+1)*blocksize] == oracle(currentFill + plaintext + j)[(i//blocksize)*blocksize:(i//blocksize+1)*blocksize]:
				plaintext += j
				break
	print(plaintext)

breakOracle()
