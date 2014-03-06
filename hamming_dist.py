class HammDist:
	def __init__(self):
		pass

	def checkio(self, n, m):
		nb = bin(n)[2:].zfill(20)
		mb = bin(m)[2:].zfill(20)
		npm = ''
		for i in range(20):
			if nb[i] == '0' and mb[i] == '0':
				npm = npm + '0'
			elif nb[i] == '1' and mb[i] == '1':
				npm = npm + '0'
			else:
				npm = npm + '1'
		return npm.count("1")

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio(117, 17) == 3, "First example"
#     assert checkio(1, 2) == 2, "Second example"
#     assert checkio(16, 15) == 5, "Third example"