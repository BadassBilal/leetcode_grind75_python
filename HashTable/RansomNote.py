class Solution:
    @staticmethod
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        d = dict()
        for alp in magazine:
            if alp in d.keys():
                d[alp] += 1
            else:
                d[alp] = 1
        print('magazine', d)
        for alp in ransomNote:
            print('ransomNote:', d)
            if alp in d.keys() and d[alp] >= 1:
                d[alp] -= 1
            else:
                return False
        return True

def main():
    print(Solution.canConstruct("aaba", "aab"))

if __name__ == '__main__':
    main()