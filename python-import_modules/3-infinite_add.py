#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    largo = len(argv)
    if largo > 1:
        resultado = 0
        for i in range(1, largo):
            num = int(argv[i])
            resultado += num
        print(f"{resultado}")
    else:
        print("0")
