
def findDuplicate(nums: list[int]) -> int:
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