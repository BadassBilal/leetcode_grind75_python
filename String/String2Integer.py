class Solution:
    @staticmethod
    def myAtoi(s: str) -> int:
        l = s.lstrip(" ").split(' ')
        if len(l) == 1: return int(s)
        elif isinstance(l[0], str) and l[0].isdigit(): return int(l[0])
        else: return 0

def main():
    print(Solution.myAtoi('987 words and 987'))

if __name__ == '__main__':
    main()

