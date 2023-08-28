class Solution:
    @staticmethod
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        # Old Approach
        # d = dict()
        # for alp in magazine:
        #     if alp in d.keys():
        #         d[alp] += 1
        #     else:
        #         d[alp] = 1
        # print('magazine', d)
        # for alp in ransomNote:
        #     if d[alp] < ransomNote.count(alp):
        #         return False
        # return True

        d = dict()
        for alp in set(magazine):
            d[alp] = magazine.count(alp)
        for alp in set(ransomNote):
            if d.get(alp, 0) < ransomNote.count(alp):
                return False
        return True

def main():
    print(Solution.canConstruct("a", "b"))

if __name__ == '__main__':
    main()