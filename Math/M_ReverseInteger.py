import sys

class Solution:
    def reverse(num: int) -> int:
        # if -(2**31)-1 < num < 2**31: return 0 #if num not in range(-(2**31)-1, 2**31+1): return 0 (Not Working) [Solution: Because I was comparing it in the first which was in-bounds, not the result which was out-of-bounds]
        # sign = -1 if num < 0 else 1
        # l = list(str(abs(num)))
        # num = int("".join(l[::-1]))
        # return num * sign

        sign = -1 if num < 0 else 1
        rev = sign * int(str(abs(num))[::-1])
        return rev if -(2 ** 31) - 1 < rev < 2 ** 31 else 0
        # sys.maxsize == 9223372036854775807 (Could be used for INTSIZE.MAX but not instead of 2**31)


def main():
    print('main', Solution.reverse(1534236469))


if __name__ == '__main__':
    main()