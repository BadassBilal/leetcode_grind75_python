import itertools, bisect, random

class Solution:

    # def __init__(self, data: list[int]):
    #     self.data = data
    #     self.sum = sum(data)
    #     self.weights = []
    #     for d in self.data:
    #         self.weights.append(d/self.sum)
    #
    #
    # def pickIndex(self) -> int:
    #     return self.data.index(choices(self.data, self.weights)[0])

    def __init__(self, w):
        # Transform [1,10,20,10] --> [1,11,31,41] (to differentiate which identical number was picked).
        self.w = list(itertools.accumulate(w))

    def pickIndex(self):
        r = random.randint(1, self.w[-1])
        # print('randomint chosen:', r, self.w)
        return bisect.bisect_left(self.w, r)
        # where it should be placed to bisect the array. (Clever hack to get the index of the num)

def main():
    obj = Solution([10,7,8,10])
    print(obj.pickIndex())
    print(obj.pickIndex())
    print(obj.pickIndex())
    print(obj.pickIndex())
    print(obj.pickIndex())
    print(obj.pickIndex())
    print(obj.pickIndex())
    print(obj.pickIndex())
    print(obj.pickIndex())
    print(obj.pickIndex())
    print(obj.pickIndex())
    print(obj.pickIndex())
    print(obj.pickIndex())
    print(obj.pickIndex())
    print(obj.pickIndex())
    print(obj.pickIndex())

if __name__ == '__main__':
    main()