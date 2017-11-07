'''
The stock prices of one unit of a stock is given.
You can buy and sell only once.
Find out the maximum profit you can make.

input : 100 20 30 110 10 60 200 20
output : 200-10 = 190

'''

def maxProfit(stocks):
    '''
    Returns the Maximum Profit that
    can be earned by buying and selling 
    a stock
    '''

    max_profit = 0
    profit = 0

    for i in range(len(stocks)):
        a = [x for x in stocks[0:i:]]

        if len(a) != 0:      
            profit = stocks[i] - min(a)

        if max_profit < profit:
            max_profit = profit

    return max_profit

if __name__ == '__main__':

    # stocks = [100, 20, 30, 110, 10, 60, 200, 20]
    stocks = [100, 20, 30, 110, 70, 80, 200]

    print maxProfit(stocks)
