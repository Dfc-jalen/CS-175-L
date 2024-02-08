print(' ')

com1 = float(input('Enter Comission rate percentage (ex 0.03) on stock purchase: '))
com2 = float(input('Enter Comission rate percentage (ex 0.03) on stock sale: '))

print(' ')

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

print(f'Amount paid for the stock: ${Amountpaid:,.2f}')
print(f'Commision paid on the purchase: ${commision1:,.2f}')
print(f'Amount the Stock sold for: ${stock_sell:,.2f}')
print(f'Commision paid on the sale: ${commision2:,.2f}')
print(f'Profit (or lose if negatve) : ${profit:,.2f}')
