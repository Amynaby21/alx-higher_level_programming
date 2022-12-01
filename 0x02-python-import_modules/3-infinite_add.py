#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    my_sum = 0
    for i in range(len(sys.argv) - 1):
        if (len(sys.argv)) > 1:
            my_sum += (int(sys.argv[i]))
    print("{}" .format(my_sum))

