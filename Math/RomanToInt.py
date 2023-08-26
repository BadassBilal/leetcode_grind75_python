def roman2int(s: str) -> int:
    total, prev = 0, 0
    d = {"I":1,"V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    for x in s[::-1]:
        num = d.get(x)
        if num < prev: total-= num
        else: total+= num
        prev = num
    return total


def main():
    print(roman2int("III"))
    print(roman2int("MCMXCIV"))
    print(roman2int("IV"))

if __name__ == '__main__':
    main()