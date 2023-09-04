def addBinary(a: str, b: str) -> str:
    return str(bin(int(a, 2) + int(b, 2)))[2:] #to eliminate "0b" in the start.

def main():
    print(addBinary('11','1'))


if __name__ == '__main__':
    main()