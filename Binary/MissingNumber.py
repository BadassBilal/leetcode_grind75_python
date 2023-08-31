class Solution:
    def missingNumber(nums: list[int]) -> int:
        #return sum([x for x in range(max(nums)+1)])-sum(nums)
        return sum([x for x in range(len(nums) + 1)]) - sum(nums)

def main():
    print(Solution.missingNumber([0,1,2,3,4,5,7,8,9]))


if __name__ == '__main__':
    main()