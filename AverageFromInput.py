#Jalen Smith
#Mr. Eckert
#CS 176-L




#line in 'numbers.txt'

def main():
    
    infile = open('numbers.txt', 'r')

    count = 0
    total = 0 
    for line in ('numbers.txt','r',3):
        ask = float(input('enter a number: '))
        total = ask + total
        count +=1
        print('I read in', count,'number(s)','Current number is:', total, 'Total is: ', total)
        print('')
    r = total/count
    print('Average:',str(float(r)))



    


# Call the main function.
if __name__ == '__main__':
    main()
