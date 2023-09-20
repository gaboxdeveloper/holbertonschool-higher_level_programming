#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lastdigit = (abs(number) % 10) * -1
        print(-lastdigit, end='')
        return -lastdigit
    else:
        lastdigit = abs(number) % 10
        print(lastdigit, end='')
        return lastdigit
