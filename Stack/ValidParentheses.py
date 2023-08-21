
def SGS4(s: str) -> bool:
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in mapping.values():  # Check if char is an opening symbol
            stack.append(char)
        elif char in mapping.keys():  # Check if char is a closing symbol
            if not stack or mapping[char] != stack.pop():
                return False

    return len(stack) == 0


def isValid(s: str) -> bool:
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()', '').replace('[]', '').replace('{}', '')
    return False if len(s) > 0 else True


def SGS2(s: str) -> bool:
    stack = []
    match = {'(': ')', '{': '}', '[': ']'}
    for char in s:
        if char in match:
            stack.append(char)
        elif len(stack) == 0 or match[stack[-1]] != char:
            return False
        else:
            stack.pop()
    return len(stack) == 0


def SGS1(s: str) -> bool:
    if not s:
        return True
    l = []
    d = {')': '(', '}': '{', ']': '['}
    for p in s:
        if p in '({[':
            l.append(p)
        else:
            if not l:
                return False
            if len(l) > 0 and l[-1] != d[p]:
                return False
            l.pop()
    return not l
def isValid(stri: str) -> bool:
    if not stri or len(stri) % 2 == 1: return False
    d = {")": "(", "}": "{", "]": "["}
    l = []
    for s in stri:
        match s:
            case '{' | '[' | '(':
                l.append(s)
            case '}' | ']' | ')':
                # if l and d[s] != l.pop():
                #     return False (WRONG)
                # if not stack or mapping[char] != stack.pop():
                #     return False (CORRECT)
                if l and l.pop() == d[s]: continue
                else: return False

    # print (f'list {l}')
    return True if not l else False

    # return True if not l else return False if l


def main():
    for expr in ["[","]","){","(]","{}","{{","([]){}","(())","({}[])","{{)","{{}","))"]:
        print(f"Expression: {expr} | Valid?: {isValid(expr)}")

if __name__ == '__main__':
    main()