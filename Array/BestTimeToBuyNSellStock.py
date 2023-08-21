import sys

def maxProfit(prices: list[int]) -> int:
    currentMin = sys.maxsize
    overallProfit = 0
    for price in prices:
        currentMin = min(currentMin, price)
        overallProfit = max(overallProfit, price-currentMin)
    return overallProfit

def main():
    print(maxProfit([1,4,1,4,3,1]))


if __name__ == '__main__':
    main()