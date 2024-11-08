# Find palindrome prime numbers between 2 integers

def palindrome_prime(num_1: int, num_2: int)-> None:

    for number in range(num_1, num_2):
        is_prime = True
        if str(number) == str(number)[::-1] and number >= 2:
            # If the number is palindromic, check if it's also prime
            for factor in range(2, number):
                # A prime number only as 1 and itself as factors
                if number % factor == 0:
                    is_prime = False
                    break

            if is_prime:
                print(number)

def main():
    start = int(input("Enter the start number: \n"))
    end = int(input("Enter the end number: \n"))

    print("The palindromic primes are:")
    palindrome_prime(start+1, end)

if __name__ == "__main__":
    main()