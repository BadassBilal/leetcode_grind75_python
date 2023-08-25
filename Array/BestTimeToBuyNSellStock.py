import sys

def maxProfit(prices: list[int]) -> int:
    currentMin = sys.maxsize
    overallProfit = 0
    for price in prices:
        currentMin = min(currentMin, price) #Finding Minimum and updating as we traverse list
        overallProfit = max(overallProfit, price-currentMin) #Finding Max by overall profit, not immediate profit
    return overallProfit

def main():
    print(maxProfit([1,4,1,4,3,1]))


if __name__ == '__main__':
    main()