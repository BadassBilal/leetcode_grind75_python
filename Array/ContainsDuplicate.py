def containsDuplicate(nums: list[int]) -> bool:
    '''65/74 Testcases solved'''
    for x in nums:
        if nums.count(x) > 1 : return True
    return False

def containsDuplicateRevised(nums: list[int]) -> bool: #Used Dictionary
    '''74/74 Testcases solved - 495ms - 33.63mb'''
    d = dict()
    for num in nums:
        if d.get(num) == None: d[num] = 0
        if d.get(num) != None and d.get(num) == 1: return True
        d[num] += 1
    return False

def SGS1(nums: list[int]) -> bool:
    '''Used Set - if set is made, duplicates are eliminated'''
    a = set(nums)
    if (len(a) != len(nums)):
        return True

def SGS2(nums: list[int]) -> bool:
    '''Used Set - Populate Set and then comparing alongside'''
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

def SGS3(nums: list[int]) -> bool:
    '''Used Sorting and then Comparing adjacent'''
    n = len(nums)
    nums.sort()
    for i in range(1, n):
        if nums[i] == nums[i - 1]:
            return True
    return False

def main():
    print(containsDuplicateRevised([1,2,3,6]))


if __name__ == '__main__':
    main()