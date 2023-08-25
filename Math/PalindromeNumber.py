
def isPalindrome(x: int) -> bool:
    x = str(x)
    if x[0] == '-': return False
    for i in range(len(x)//2+1):
        if x[i] != x[len(x)-1-i]: return False
    return True

def SGS(x: int) -> bool:
    if str(x) != str(x)[::-1]:
        return False
    return True

def SGS2(x: int) -> bool:
    return str(x) == str(x)[::-1]

def main():
    print(isPalindrome(1231))

if __name__ == '__main__':
    main()