


def hammingWeight(n: int) -> int:

    return bin(n).count('1')


def main():
    print(hammingWeight(0o0000000000000000000000010000000))


if __name__ == '__main__':
    main()