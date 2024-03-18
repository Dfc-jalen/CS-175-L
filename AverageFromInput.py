#Jalen Smith
#Mr. Eckert
#CS 176-L

#line in 'numbers.txt'

def main():
    
    infile = open('num.txt', 'r')

    count = 0
    total = 0
    numbers = 0
    for line in infile:
        
        
        line = line.strip()
        line = float(line)
        line1 = round(line,2)
            
        numbers += 1
            
        total = total + float(line)
        
            #print('I read in', numbers,'number(s)','Current number is:',   float(line)   , '  Total is: ', total)
        print(f'I read in number(s) {numbers} Current number is:   {line}0     Total is:  {total:>5}0')
            

        count+=1
    r = total/count
    print('Average:',str(float(r)))


# Call the main function.
if __name__ == '__main__':
    main()
