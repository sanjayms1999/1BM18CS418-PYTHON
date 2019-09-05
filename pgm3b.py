import string
from random import randint
str1 = string.printable
print(str1)
print(len(str1))
for i in range(8):
    print(str1[randint(1, 100)],end="")