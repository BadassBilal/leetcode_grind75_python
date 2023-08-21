import re

def isPalindrome(stri: str) -> bool:
    stri = re.sub(r'[^a-zA-Z0-9]','',stri).lower()  # Regex to eliminate Punctuation, lowercasing and eliminating space
    return stri == stri[::-1]  # Reversing the String

def main():
    print(isPalindrome("A man, a plan, a canal: Panama"))

if __name__ == '__main__':
    main()