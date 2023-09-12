class Solution:
    def findAnagrams(s: str, p: str) -> list[int]:
        '''
        # 55/65 Passed
        rslt = []
        ana = len(p)
        sub = set(p)
        for i, x in enumerate(range(len(s)+1-ana)):
            substring = set(s[x:x + ana])
            if substring == sub: rslt.append(i)
        return rslt
        '''






def main():
    print(Solution.findAnagrams(s = "cbaebabacd", p = "abc"))


if __name__ == '__main__':
    main()