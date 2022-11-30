#!/usr/bin/python3
for i in range(97, 123)[::-1]:
    if i % 2 == 0:
        k = i
    else:
        k = i - 32
    print("{0:c}".format(k), end="")
