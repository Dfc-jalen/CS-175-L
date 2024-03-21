#Jalen Smith
#Mr. Eckert
#CS 176-L

#line in 'numbers.txt'
import os

def main():

    
    try:
        infile = open('numb.txt', 'r')
    except IOError:
        print('SystemExit: File not found: numbers.txt - existing')
        exit()
              

    count = 0
    total = 0
    numbers = 0 
    line = float 

    for line in infile:
        #print("The content of line is:", line)

        try:
            
            line = line.strip()
            
            numbers += 1
            
            total = total + float(line)
        
            #print('I read in', numbers,'number(s)','Current number is:',   float(line)   , '  Total is: ', total)
            print(f'I read in number(s)  {numbers} Current number is: {line}    Total is:  {total:>5}')
            

            count+=1

            
        except ValueError:
            
            line = line.strip()
            
            numbers -=1
            
            
            

            
    if total == 0:
        print('The average is 0')
        exit()
    
    r = total/count
    
    print('Average:',str(float(r)))


# Call the main function.
if __name__ == '__main__':
    main()
