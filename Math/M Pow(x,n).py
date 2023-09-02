class Solution:
    @staticmethod
    def myPow(x: float, n: int) -> float:
        return x ** n

    @staticmethod
    def myPower(x: float, n: int) -> float:
        if n == 0: return 1
        if n < 0: x = 1/x
        digit = x
        for i in range(abs(n)-1):
            digit *= x
        return digit


def main():
    print(Solution.myPow(0.00001,2147483647))
    print(Solution.myPower(0.00001,2147483647))

if __name__ == '__main__':
    main()