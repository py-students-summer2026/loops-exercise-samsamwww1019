def one(numbers):
    """
    Write a program that finds the largest element in a given list using a for loop.
    """
    print("\nmedium.one:")

    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    print('\t', largest)

def two(numbers):
    """
    Write a program that calculates the average of a list of numbers using a while loop. You are not allowed to use the built-in sum() function.
    """
    print("\nmedium.two:")

    total = 0
    i = 0

    while i < len(numbers):
        total += numbers[i]
        i += 1

    average = total / len(numbers)
    print('\t', average)

def three(text):
    """
    Write a program that checks if a given string is a palindrome using a for loop. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, e.g. radar, level, 12321, mom, noon, civic, deified, racecar, madam, refer, repaper, rotor, sagas, solos, stats, tenet, wow, ...
    """
    print("\nmedium.three:")

    backwards = ""

    for character in text:
        backwards = character + backwards

    if text == backwards:
        print('\t', f'{text} is a palindrome')
    else:
        print('\t', f'{text} is not a palindrome')

def four(first, ratio, n):
    """
    Write a program that prints the first n terms of the geometric sequence using a while loop. A geometric sequence is a sequence of numbers in which each term after the first is found by multiplying the previous term by a fixed, non-zero number called the common ratio, e.g. 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, ..., where the common ratio is 2.
    """
    print("\nmedium.four:")

    i = 0
    current = first

    while i < n:
        print('\t', current)
        current *= ratio
        i += 1

def five(numbers):
    """
    Write a program that finds the second largest element in a given list using a for loop.
    """
    print("\nmedium.five:")

    largest = numbers[0]
    second_largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    for number in numbers:
        if number != largest:
            second_largest = number
            break

    for number in numbers:
        if number != largest and number > second_largest:
            second_largest = number

    print('\t', second_largest)

def six(number):
    """
    Write a program that calculates the factorial of a given number using a while loop.
    """
    print("\nmedium.six:")

    product = 1
    i = 1

    while i <= number:
        product *= i
        i += 1

    print('\t', product)

def seven(number):
    """
    Write a program that checks if a given number is a perfect square using a for loop. A perfect square is a number that can be expressed as the product of two equal integers, e.g. 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, ...
    """
    print("\nmedium.seven:")

    is_perfect_square = False

    for i in range(0, number + 1):
        if i * i == number:
            is_perfect_square = True

    if is_perfect_square:
        print('\t', f'{number} is a perfect square')
    else:
        print('\t', f'{number} is not a perfect square')

def eight():
    """
    Write a program that prints the sum of all prime numbers between 1 and 100 using a while loop.
    """
    print("\nmedium.eight:")

    total = 0
    number = 2

    while number <= 100:
        divisor = 2
        is_prime = True

        while divisor < number:
            if number % divisor == 0:
                is_prime = False
            divisor += 1

        if is_prime:
            total += number

        number += 1

    print('\t', total)

def nine(sentence):
    """
    Write a program that counts the number of words in a given sentence using a for loop. Words can be separated by spaces, commas, periods, exclamation marks, question marks, etc. You may be interested in the built-in split() function, which splits a string into a list of words based on a delimiter. The delimiter is a space by default, but you can specify a different delimiter, e.g. split(','), split('.'), split('!'), split('?'), etc. You can even specify multiple delimiters, e.g. split(',.!?').
    """
    print("\nmedium.nine:")

    count = 0
    in_word = False
    separators = [' ', ',', '.', '!', '?']

    for character in sentence:
        if character not in separators:
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False

    print('\t', count)

def ten(first_list, second_list):
    """
    Write a program that prints the common elements between two lists using a while loop.
    """
    print("\nmedium.ten:")

    i = 0
    common = []

    while i < len(first_list):
        if first_list[i] in second_list and first_list[i] not in common:
            common.append(first_list[i])
        i += 1

    print('\t', common)