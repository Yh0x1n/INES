import random

def random_id():
    numbers = '1234567890'
    len = 4
    return int(''.join(random.sample(numbers, len)))

def token_generator():
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    Symbols = '¿?¡!$%&#-_+\/<ñ>'
    all = upper + lower + numbers + Symbols
    len = 10

    return ''.join(random.sample(all, len))