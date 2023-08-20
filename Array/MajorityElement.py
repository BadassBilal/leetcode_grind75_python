

def majorityElement_Dict(nums: list[int]) -> int:
    '''Passed - 146ms - 17.86mb'''
    d = dict()
    for num in nums:
        if d.get(num) != None:
            d[num] = d.get(num)+1
        else:
            d[num] = 0
    return max(d, key=d.get)

def majorityElement_Sort(nums: list[int]) -> int:
    '''Passed - 156ms - 17.96mb'''
    nums.sort()
    return nums[len(nums)//2]

def majorityElement_MooresAlgo(nums: list[int]) -> int:
    '''Passed - 156ms - 17.87mb'''
    count = 0
    for num in nums:
        if count == 0: cand = num
        count += 1 if num == cand else -1
    return cand

def main():
    print(majorityElement_Sort([2,2,1,1,1,2,2]))
    print(majorityElement_Dict([2,2,1,1,1,2,2]))
    print(majorityElement_MooresAlgo([2,2,1,1,1,2,2]))


if __name__ == '__main__':
    main()