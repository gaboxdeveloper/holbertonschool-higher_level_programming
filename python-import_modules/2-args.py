#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lenarg = len(argv)
    i = 1
    if lenarg > 2:
        print(f"{lenarg - 1}: arguments")
        while i < lenarg:
            print(f"{i}: {argv[i]}")
            i += 1
    elif lenarg == 1:
        print(f"0: arguments")
    elif lenarg == 2:
        print(f"1: argument")
        print(f"1: {argv[1]}")
