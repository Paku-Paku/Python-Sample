"""
3で割り切れる場合はFizz
5で割り切れる場合はBuzz
３でも5でも割り切れる場合はFizzBuzz
"""

def fizzbuzz(number=100):
    for i in range(1, number+1):
        if i % 15 == 0:        
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()