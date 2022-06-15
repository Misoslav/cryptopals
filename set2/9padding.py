in1 = "YELLOW SUBMARINE"
blocksize = 32
pad = lambda x: x + (blocksize-len(x)%blocksize)*chr(blocksize-len(x)%blocksize)
print(pad(in1).encode())
