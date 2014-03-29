#Your optional code here
#You can import some modules or create additional functions
class Fizzbuzz:
	def __init__(self):
		pass

	def checkio(self, number):
		if number % 3 == 0 and number % 5 == 0:
			return "Fizz Buzz"
		elif number % 5 == 0:
			return "Buzz"
		elif number % 3 == 0:
			return "Fizz"
		else:
			return str(number)

#Some hints:
#Convert a number in the string with str(n)

#These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
# 	f=Fizzbuzz()
# 	assert f.checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
# 	assert f.checkio(6) == "Fizz", "6 is divisible by 3"
# 	assert f.checkio(5) == "Buzz", "5 is divisible by 5"
#     assert f.checkio(7) == "7", "7 is not divisible by 3 or 5"