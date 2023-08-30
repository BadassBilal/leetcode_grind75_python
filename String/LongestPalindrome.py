def longestPalindrome(stri: str) -> int:
    unique = set()
    pairs = 0
    for s in stri:
        if s in unique:
            pairs += 2
            unique.remove(s)
        else:
            unique.add(s)
    return pairs + 1 if unique else pairs




def main():
    print(longestPalindrome('acdxca'))

if __name__ == '__main__':
    main()