#!/usr/bin/python3

def islower(c):
    # Check if the ASCII value of the character is between the ASCII values of 'a' and 'z'
    return ord('a') <= ord(c) <= ord('z')

# Test cases
print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))
