#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    i = 0

    sum = 0
    for arg in sys.argv:
        if i != 0:
            sum += int(arg)
        i += 1
    print(sum)
