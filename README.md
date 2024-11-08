# Palindrome_primes

A palindrome is a word that is spelled the same forwards and backwards.
A prime number is a number that only has 2 divisors/factors, 1 and the number itself. In other words, the number can only be evenly divided by 1 and the number itself.

In this program, the user will be asked to specify 2 integers, the starting number and the ending number.

For all numbers between the starting number and ending number, the following will be done:
- the number is converted into a string to check if it is a palindrome
- then it is divided by numbers ranging from 2 and (ending number - 1) to see if it can be divided evenly. If it can, it is not a prime number
- if the number is palindromic and prime, it is printed out
