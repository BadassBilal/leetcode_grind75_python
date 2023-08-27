def longestCommonPrefix(strs: list[str]) -> str:
    '''
    If the array is sorted alphabetically:
    > The first element of the array
    > the last element of the array
    will have "MOST DIFFERENT PREFIXES" of all comparisons.

    If this is true, you only have to compare these two strings.
    '''

    rslt = ''
    strs.sort()
    for x in range(min(len(strs[0]),len(strs[-1]))):
        if strs[0][x] != strs[-1][x]:
            return rslt
        rslt+=strs[0][x]
    return rslt

def main():
    print(longestCommonPrefix(["aaa","aa","aaa"]))


if __name__ == '__main__':
    main()