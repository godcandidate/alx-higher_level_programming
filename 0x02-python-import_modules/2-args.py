#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    l = len(sys.argv) - 1

    if l == 0:
        print("{} arguments.".format(l))
    else:
        if l == 1:
            print("{} argument:".format(l))
        else:
            print("{} arguments:".format(l))

        i = 0
        for arg in sys.argv:
            if i != 0:
                print("{}: {}".format(i, arg))
            i += 1
