from sys import version, platform, getsizeof
from ctypes import string_at
import struct

print(version, platform)
# 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] win32


def show_size(x, level=0):
    print('\t' * level, f'type={x.__class__}, size={getsizeof(x)}, object={x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'item'):
            for xx in x.items():
                show_size(xx, level+1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


a = 5
b = 5.14
c = 'Hello world!'
d = [1, 2, 3, 4]

# print(id(a))
# print(getsizeof(a))
#
# print(string_at(id(a), getsizeof(a)))
# print(struct.unpack('LLLcc', string_at(id(a), getsizeof(a))))
#
# print('*' * 50)
# print(id(b))
# print(getsizeof(b))
#
# print(string_at(id(b), getsizeof(b)))
# print(struct.unpack('LLLl', string_at(id(b), getsizeof(b))))
#
# print('*' * 50)
# print(id(c))
# print(getsizeof(c))
#
# print(string_at(id(c), getsizeof(c)))
# print(struct.unpack('LLLLLl' + 'c' * 13, string_at(id(c), getsizeof(c))))
#
# print('*' * 50)
# print(id(d))
# print(getsizeof(d))

# print(string_at(id(d), getsizeof(d)))
# print(struct.unpack('LLLLLLLLLLLLL', string_at(id(d), getsizeof(d))))
