
def countBits(n: int) -> list[int]:
    # d = dict()
    # for i in range(n):
    #     d[n] = bin(n)[2:].count('1')
    # print(d)

    # l = list()
    # for i in range(n+1):
        # l.append(bin(i)[2:].count('1'))
    # return l

    return [bin(i)[2:].count('1') for i in range(n+1)]




def main():
    print(countBits(2))

if __name__ == '__main__':
    main()