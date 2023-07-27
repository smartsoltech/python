def fizzbuzz():
    for num in range(1, 101):
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizzbuzz()

# Создание генератора чисел от 1 до 100 с заменой чисел, кратных трем, на "Fizz", чисел, кратных пяти, на "Buzz", и чисел, кратных и трем, и пяти, на "FizzBuzz"
fizzbuzz = ("FizzBuzz" if num % 15 == 0 else "Fizz" if num % 3 == 0 else "Buzz" if num % 5 == 0 else num for num in range(1, 101))

# Получение и вывод всех элементов из генератора
print(list(fizzbuzz))
