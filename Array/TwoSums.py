def twoSum(nums: list[int], target: int) -> list[int]:
    '''
    Using Dictionary as searching takes O(1)
    '''
    d = dict()
    for index, value in enumerate(nums):
        diff = target - value
        if diff in d.keys(): return [index, d.get(diff)]
        d[value] = index


def main():
    print(twoSum(nums=[2, 7, 11, 15], target=9))


if __name__ == "__main__":
    main()
