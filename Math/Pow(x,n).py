class Solution:
    @staticmethod
    def myPow(x: float, n: int) -> float:
        return x ** n

    @staticmethod
    def myPower(x: float, n: int) -> float:
        if n == 0: return 1
        elif n < 0:
            x, const = 1/x, 1/x
        else: const = x
        for i in range(abs(n)-1):
            x *= const
        return x


def main():
    print(Solution.myPow(2,-2))
    print(Solution.myPower(2,-2))

if __name__ == '__main__':
    main()