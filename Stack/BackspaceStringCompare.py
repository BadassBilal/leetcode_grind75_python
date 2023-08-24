
def backspaceCompare(s: str, t: str) -> bool:
    '''
    when variable length and we want to apply the same thing to diff variables
    make a new function like decorator function within the main one, and
    return while applying function on s str and t str like this.
    '''
    def bkspCompare(stri: str):
        stk = []
        for i in stri:
            if i == "#" and len(stk) != 0: stk.pop()
            elif i=="#": continue
            else: stk.append(i)
        print(stri, stk)
        return "".join(stk)


    return bkspCompare(s) == bkspCompare(t)

def main():
    print(backspaceCompare("y#fo##f", 'y#f#o##f'))


if __name__ == '__main__':
    main()