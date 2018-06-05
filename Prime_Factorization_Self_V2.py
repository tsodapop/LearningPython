def main():

	while True:
		#Get an input from the user for the number they want to get the primes for.
		number_prime = int(input('What is the number you want to find the primes for? '))
		#Create an empty list for all of the prime factors
		prime_factors = []

		if number_prime >= 2:
			#While loop that will reset the inner for loop each time it finds a prime factor
			while True:
				#If number_prime = 1, it means there are no more primes
				if number_prime == 1:
					print('your prime factorization results in {}'.format(prime_factors))
					return False
				#For loop that we break out of if the prime number is divisible by i value	
				for i in range (2, number_prime + 1):
					if number_prime % i == 0:
						prime_factors.append(i)
						number_prime //= i			
						break
		else:
			print('Give me a number at least 2 or more.')

if __name__ == '__main__':
	main()
