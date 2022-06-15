def validatePad(x):
	for i in range(x[-1]):
		assert x[-1] == x[-1-i]
