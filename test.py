# def simple_generator():
#     yield 1
#     yield 2
#     yield 3

# for value in simple_generator():
#     print(value)



import random
random_iter = iter(lambda: random.randint(0, 5), 2)

for num in random_iter:
    print(num)