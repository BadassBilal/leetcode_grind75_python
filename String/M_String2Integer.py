class Solution:
    @staticmethod
    def myAtoi(s: str) -> int:
        l = list(s.strip()) #Strips "STR" -> ['S', 'T', 'R']
        if not l: return 0  #If the list is empty.
        sign = -1 if l[0] == '-' else 1 # Either a positive or a negative, in last, multiply with the sign.
        if l[0] in ['+', '-']: l.pop(0) # Eliminating the sign
        big, i = 0, 0 # using Hundreth *100 + Ten * 10 + digit strat
        while (i < len(l) and l[i].isdigit()): #Checking if the string is actually an integer value
            big = big * 10 + int(l[i])
            i += 1
        total = sign * big
        return max(-2 ** 31, total) if sign == -1 else min(2 ** 31 - 1, total) #have to stay within range

        '''
        l = s.lstrip(" ").split(' ')
        if len(l) == 1: return int(s)
        else:
            print(l)
            l = list(filter(lambda x: isinstance(x, str) and x.isdigit(), l))
            return list(map(int, l))[0]
        '''

def main():
    print(Solution.myAtoi('-42'))

if __name__ == '__main__':
    main()

