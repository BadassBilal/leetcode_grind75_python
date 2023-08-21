def can_attend_meetings(intervals: list[(int,int)]) -> bool:
    sortarr = sorted(intervals, key=lambda x: (x[0],x[1])) #sorting the list w.r.t first elem of tuples and then by second.
    for i, tup in enumerate(sortarr[:-1]):
        # first condition is matching the end with the following start. Second condition is overlapping of first elem in various meeting
        if intervals[i][1] > intervals[i+1][0] or intervals[i][0] <= intervals[i+1][0]: return False
    return True

def main():
    print(can_attend_meetings([(15,15),(15,25),(15,20)]))


if __name__ == '__main__':
    main()