
def moveZeroes(nums: list[int]) -> None:
    index = 0
    mid = 0
    for num in nums:
        match num:
            case 0:
                mid += 1
            case _ if num != 0:
                nums[index], nums[mid] = nums[mid], nums[index]
                mid += 1
                index += 1
    return nums

def main():
    print(moveZeroes([0,1,0,3,12]))


if __name__ == '__main__':
    main()