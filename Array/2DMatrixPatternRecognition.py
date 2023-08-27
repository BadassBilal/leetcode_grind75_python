l = [[1, 2, 3],
     [4, 1, 3],
     [7, 6, 1]]
'''
l = [[1,2,3],
     [4,5,6],
     [7,8,9]]
Pattern to Recognize:
[ a     x]
[ y     a]    
'''
for x in range(len(l)-1):
    for y in range(len(l)-1):
        if l[x][y] == l[x+1][y+1] and l[x+1][y]/2 == l[x][y+1]:
            print(f'[{l[x][y]}|{l[x][y+1]}]')
            print(f'[{l[x+1][y]}|{l[x+1][y+1]}]')

