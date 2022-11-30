#!/usr/bin/python3
for character in range(ord('z'), ord('a') - 1, - 1):
    print("{:c}" .format(character), end="")
    if character % 2 == 0 else character - 32
