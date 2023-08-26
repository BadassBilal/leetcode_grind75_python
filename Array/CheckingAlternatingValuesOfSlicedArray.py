#print(f"{x}%{len(l)}", x%len(l))
#print(f"{x}: {x+sz} | ",list(itertools.islice(l,x,x+sz)))
#print(list(itertools.islice(l,2)))

def circslice(l, a, b):
    if b>=a:
        return l[a:b]
    else:
        return l[a:]+l[:b]

def adjacentcheck(l):
    return len(set(l[::2]))==1 and len(set(l[1::2]))==1
    '''
    Adjacent Solution using zip keyword
    for sub in lists:
        print(all(x!= y for x, y in zip(sub, sub[1:])))
    '''

def main():
    l =[1,2,1,2,2,1,1]
    sz = 3

    for x in range(len(l)+1):
        new_list = circslice(l, x % len(l), (x + sz) % len(l))
        print(f" {new_list}|{adjacentcheck(new_list)}")

if __name__ == '__main__':
    main()
