"""
Day 13 - Debugging Playground
Author: Sanjay

Practice debugging common Python mistakes.
"""

def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


def find_largest(numbers):
    if not numbers:
        return None

    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for letter in text:
        if letter in vowels:
            count += 1

    return count


def reverse_string(text):
    return text[::-1]


def factorial(n):
    if n < 0:
        raise ValueError("Factorial doesn't exist for negative numbers.")

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def main():

    print("=== Debugging Playground ===\n")

    print("Division")
    print(divide_numbers(20, 5))

    print("\nLargest Number")
    nums = [5, 18, 7, 42, 11]
    print(find_largest(nums))

    print("\nVowel Counter")
    print(count_vowels("Python Programming"))

    print("\nReverse String")
    print(reverse_string("Angela"))

    print("\nFactorial")
    print(factorial(5))


if __name__ == "__main__":
    main()