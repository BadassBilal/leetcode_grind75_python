class Solution:
    def lenOfLongestSubstring(stri: str) -> int:
        '''124ms - 16.13mb'''
        init, ext, largest = 0, 1, 0 #Intial Approach - 124ms/16.13mb
        while ext <= len(stri):
            if len(stri[init:ext]) == len(set(stri[init:ext])):
                largest = len(stri[init:ext])
                ext+=1
            else:
                init+=1
                if init == ext - largest: ext+=1
        return largest

        # init, ext, largest, uniq = 0, 0, 0, set() # 651ms/16.3mb
        # while ext < len(stri):
        #     if stri[ext] not in uniq:
        #         uniq.add(stri[ext])
        #         largest=max(largest, len(uniq), ext-init)
        #         ext+=1
        #     else:
        #         uniq.clear()
        #         init = stri.find(stri[ext],init)+1
        #         uniq.add(stri[init])
        #         ext = init + 1
        # return largest

    def SGS1(s: str) -> int:
        '''Using Set'''
        myset = set()
        left = 0
        count = 0
        for right in range(len(s)):
            if s[right] not in myset:
                myset.add(s[right])
                count = max(count, right - left + 1)
            else:
                while s[right] in myset:
                    myset.remove(s[left])
                    left += 1
                myset.add(s[right])
        return count


    def SGS2(s: str) -> int:
        '''Using Dict'''
        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):
            """If s[r] not in seen, we can keep increasing the window size by moving right pointer"""
            if s[r] not in seen: output = max(output, r - l + 1)
            else:
                if seen[s[r]] < l:
                    output = max(output, r - l + 1)
                    """
                    There are two cases if s[r] in seen:
                    case1: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
                    case2: s[r] is not inside the current window, we can keep increase the window
                    """
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r


        return output

def main():
    print(Solution.lenOfLongestSubstring("abcabcbb"))

if __name__ == '__main__':
    main()