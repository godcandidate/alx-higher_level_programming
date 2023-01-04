#!/usr/bin/python3
for letter in reversed(range(97, 123)):
    diff = 0

    if letter % 2 != 0:
        diff = 32

    print("{:c}".format(letter - diff), end='')
