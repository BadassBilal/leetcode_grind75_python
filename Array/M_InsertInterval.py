
def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    prev, forw = False, False
    intervals.append(newInterval)
    sortarr = sorted(intervals, key=lambda x: [x[0],x[1]])
    i = sortarr.index(newInterval)

    if sortarr[i-1][1] > sortarr[i][0]: prev = True
    if sortarr[i][1] > sortarr[i+1][0]: forw = True

    if prev and forw:
        sortarr[i] = [sortarr[i-1][0], sortarr[i+1][1]]
        sortarr.remove(sortarr[i-1])
        sortarr.remove(sortarr[i+1])
    elif prev and not forw:
        sortarr[i] = [sortarr[i-1][0], sortarr[i][1]]
        sortarr.remove(sortarr[i-1])
    elif not prev and forw:
        sortarr[i] = [sortarr[i][0], sortarr[i+1][1]]
        sortarr.remove(sortarr[i+1])

    return sortarr








def main():
    insert(intervals = [[1,3],[6,9]], newInterval = [2,5])

if __name__ == '__main__':
    main()