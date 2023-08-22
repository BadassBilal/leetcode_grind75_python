def isValidAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t) #sorted use TimSort O(n * log n)


def main():
    isValidAnagram("anagram", "nagaram")

if __name__ == '__main__':
    main()