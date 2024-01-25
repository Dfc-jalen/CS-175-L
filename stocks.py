total = 0
com1 = float(input('Enter Comission rate percentage (ex 0.03) on stock purchase: '))
com2 = float(input('Enter Comission rate percentage (ex 0.03) on stock sale: '))

shares1 = int(input('Enter number of shares purchased: ' ))
shares2 = int(input('Enter number of shares sold: '))
purchase = int(input('Enter purchase price per share: '))
sell = float(input('Enter sell price per share: '))
print(' ')

Amountpaid = (shares1*purchase)
commision2 = (shares1*sell*com1)
commision1 = shares1*purchase*com1
stock_sell = (shares1*sell)
profit = stock_sell - Amountpaid - commision2 - commision1 

print(f'Amount paid for the stock ${Amountpaid:,.2f}')
print(f'Amount paid for the stock ${commision1:,.2f}')
print(f'Amount paid for the stock ${stock_sell:,.2f}')
print(f'Amount paid for the stock ${commision2:,.2f}')
print(f'Amount paid for the stock ${profit:,.2f}')
 
