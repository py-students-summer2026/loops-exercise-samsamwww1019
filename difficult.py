def one(number):
    """
    Write a program that finds the prime factors of a given number using a for loop. A prime factor is a prime number that divides another number exactly without leaving a remainder, e.g. the prime factors of 12 are 2 and 3.
    """
    print("\ndifficult.one:")

    prime_factors = []

    for factor in range(2, number + 1):
        if number % factor == 0:
            is_prime = True

            for divisor in range(2, factor):
                if factor % divisor == 0:
                    is_prime = False

            if is_prime:
                prime_factors.append(factor)

    print('\t', prime_factors)

def two(n):
    """
    Write a program that calculates the nth term of the Fibonacci sequence using a while loop.
    """
    print("\ndifficult.two:")

    if n == 1:
        print('\t', 0)
        return

    if n == 2:
        print('\t', 1)
        return

    first = 0
    second = 1
    i = 3

    while i <= n:
        total = first + second
        first = second
        second = total
        i += 1

    print('\t', second)

def three(first_text, second_text):
    """
    Write a program that checks if a given string is an anagram using a for loop.
    """
    print("\ndifficult.three:")

    first_text = first_text.lower().replace(" ", "")
    second_text = second_text.lower().replace(" ", "")

    first_letters = []
    second_letters = []

    for character in first_text:
        first_letters.append(character)

    for character in second_text:
        second_letters.append(character)

    is_anagram = True

    if len(first_letters) != len(second_letters):
        is_anagram = False
    else:
        for character in first_letters:
            if character in second_letters:
                second_letters.remove(character)
            else:
                is_anagram = False

    if is_anagram:
        print('\t', 'anagrams')
    else:
        print('\t', 'not anagrams')

def four(first, difference, n):
    """
    Write a program that prints the first n terms of the arithmetic sequence using a while loop. An arithmetic sequence is a sequence of numbers in which each term after the first is found by adding a fixed, non-zero number called the common difference to the previous term, e.g. 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, ..., where the common difference is 2.
    """
    print("\ndifficult.four:")

    i = 0
    current = first

    while i < n:
        print('\t', current)
        current += difference
        i += 1

def five(numbers):
    """
    Write a program that finds the median of a given list of numbers using a for loop. The median is the middle value of a list of numbers when they are sorted in ascending order. If the list has an odd number of elements, the median is the middle element. If the list has an even number of elements, the median is the average of the two middle elements.
    """
    print("\ndifficult.five:")

    sorted_numbers = numbers.copy()

    for i in range(len(sorted_numbers)):
        for j in range(i + 1, len(sorted_numbers)):
            if sorted_numbers[j] < sorted_numbers[i]:
                temporary = sorted_numbers[i]
                sorted_numbers[i] = sorted_numbers[j]
                sorted_numbers[j] = temporary

    middle = len(sorted_numbers) // 2

    if len(sorted_numbers) % 2 == 1:
        median = sorted_numbers[middle]
    else:
        median = (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2

    print('\t', median)

def six(number):
    """
    Write a program that checks if a given number is a perfect number using a while loop. A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself, e.g. 6 is a perfect number because 1 + 2 + 3 = 6.
    """
    print("\ndifficult.six:")

    total = 0
    divisor = 1

    while divisor < number:
        if number % divisor == 0:
            total += divisor
        divisor += 1

    if total == number:
        print('\t', f'{number} is a perfect number')
    else:
        print('\t', f'{number} is not a perfect number')

def seven(number):
    """
    Write a program that prints the sum of all digits in a given number using a for loop. For example, the sum of the digits in 12345 is 1 + 2 + 3 + 4 + 5 = 15.
    """
    print("\ndifficult.seven:")

    total = 0

    for digit in str(number):
        total += int(digit)

    print('\t', total)

def eight(sentence):
    """
    Write a program that finds the longest word in a given sentence using a while loop.
    """
    print("\ndifficult.eight:")

    words = sentence.split()
    longest = words[0]
    i = 0

    while i < len(words):
        if len(words[i]) > len(longest):
            longest = words[i]
        i += 1

    print('\t', longest)

def nine(sentence):
    """
    Write a program that checks if a given string is a pangram using a for loop. A pangram is a sentence that contains every letter of the alphabet at least once, e.g. The quick brown fox jumps over the lazy dog.
    """
    print("\ndifficult.nine:")

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()
    is_pangram = True

    for letter in alphabet:
        if letter not in sentence:
            is_pangram = False

    if is_pangram:
        print('\t', 'pangram')
    else:
        print('\t', 'not a pangram')

def ten():
    """
    Write a program that prints the prime numbers between 1 and 1000 using a while loop.
    """
    print("\ndifficult.ten:")

    number = 2

    while number <= 1000:
        divisor = 2
        is_prime = True

        while divisor < number:
            if number % divisor == 0:
                is_prime = False
            divisor += 1

        if is_prime:
            print('\t', number)

        number += 1