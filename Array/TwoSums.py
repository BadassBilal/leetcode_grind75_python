def twoSum(nums: list[int], target: int) -> list[int]:
    '''
    Docstring
    Using Dictionary as searching takes Time Complexity O(1) and Space Complexity O(n)
    Saves like value-index string as we need to return index
    2  | 0
    next is 7. We'll make a query which finds target-value=9-7=2 which exists
    return this.index and 2's index.
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
