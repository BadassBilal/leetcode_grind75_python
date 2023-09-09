from random import choices

class Solution:

    def __init__(self, data: list[int]):
        self.data = data
        self.sum = sum(data)
        self.weights = []
        for d in self.data:
            self.weights.append(d/self.sum)


    def pickIndex(self) -> int:
        return self.data.index(choices(self.data, self.weights)[0])

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