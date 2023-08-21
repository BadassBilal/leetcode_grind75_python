

def SqOfSortedArray(nums: list[int]) -> list[int]:
    return sorted(list(map(lambda x: x*x, nums)))
    # list(map()) --> [x**2 for x in nums]

def main():
    print(SqOfSortedArray([-4,-1,0,3,10]))


if __name__ == '__main__':
    main()