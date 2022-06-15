#input
in1 = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
in1b = in1.encode()
res1 = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
res1b = bytes.fromhex(res1)
inLen = len(in1)

#key
key = "ICE"
keyLen = len(key)
xorKey = key * (inLen//keyLen) + key[:inLen%keyLen]
xorKey = xorKey.encode()

res = bytes([a ^ b for a, b in zip(xorKey, in1b)])
print(res.hex())
print(res1)
