#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        r = a / b
        return r
    except ZeroDivisionError:
        return None
    finally:
        print(r)
