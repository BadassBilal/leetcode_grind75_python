class Cmp:

    def __init__(self, num):
        self.value = str(num)

    def __repr__(self):
        pass

    def __gt__(self, other):
        return self.value + other.value > other.value + self.value


def largestNumber(nums: list[int]) -> str:
    # nums.sort(key=lambda x: int(str(x)[0]), reverse=True)
    numString = [Cmp(num) for num in nums]
    numString.sort()


def main():
    print(largestNumber([3,30,34,5,9]))

if __name__ == '__main__':
    main()