
def findDuplicate(nums: list[int]) -> int:

    # return sum(nums)-sum([x for x in range(len(nums))]) # 15 Cases Solved Only

    s = set()
    for num in nums:
        if num in s:
            return num
        s.add(num)
    return None

def main():
    print(findDuplicate([1,3,4,2,2]))


if __name__ == '__main__':
    main()