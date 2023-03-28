print('https://replit.com/@Levashov/hack')

import random

def good_password_generator(length):
    alphabet = (
        '0123456789'
        'abcdefghijklmnopqrstuvwxyz'
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        '!@#$%^&*()_+'
    )
    result = ''
    for i in range(length):
        print(i)
        symbol = random.choice(alphabet)
        result += symbol
    return result

print(good_password_generator(1))
print(good_password_generator(3))
print(good_password_generator(5))
print(good_password_generator(10))
print(good_password_generator(20))


with open('passwords.txt') as f:
    content = f.read()

passwords = content.split('\n')
i = 0

def bad_password_generator():
    global i
    password = passwords[i]
    i += 1
    return password

print(bad_password_generator())
print(bad_password_generator())
print(bad_password_generator())
print(bad_password_generator())
print(bad_password_generator())
print(bad_password_generator())


# def func(a, b, c):
#     print(a)
#     result = b * c
#     return result

# result = func(1, 2, 3)
# print(result)
