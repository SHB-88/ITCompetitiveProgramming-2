alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def num_hash(num):
	if num < 26:
		return alpha[num-1]
	else:
		q, r = num//26, num % 26
		if r == 0:
			if q == 1:
				return alpha[r-1]
			else:
				return num_hash(q-1) + alpha[r-1]
		else:
			return num_hash(q) + alpha[r-1]


print(num_hash(26))
print(num_hash(22))
print(num_hash(23))
print(num_hash(225))


