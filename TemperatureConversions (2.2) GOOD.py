#Jalen Smith
#CS 175-L
#Mr. Eckert 

import os
import sys

def main():
    controlLoop()

def convertToKelvin(fahren):
    kelvin = (fahren-32) * 5/9 + 273.15
    return kelvin
    
def convertToCentigrade(fahren):
    celsius = (fahren - 32) * 5/9
    return celsius

def doConversion():
    
    fahren = getFahrenheit()
    print(' ')
    if fahren == None:
        print('no more attempts')
        exit()
    kelvin = convertToKelvin(fahren)
    celsius = convertToCentigrade(fahren)

    r = round(kelvin,2)
    c = round(celsius,2)
    
    print('Fahrenheit:', fahren, 'Kelvin:' , r, 'Centigrade: ', c )
      
def repeat():
    question1 = int(input('How many conversions would you like to do this time?: '))
    for x in range(question1):
        doConversion()
    
def controlLoop():
    question = input('Do you want to do some conversions(yes or no)?: ')
    
    if question == 'no':
        print('ok goodbye')
    else:
        repeat()   

def getFahrenheit():
    count = 3 
    while count > 0:
        fahren = int(input('Enter Fahrenheit temperature (must be -50 to 130) you only have 3 chances: '))
        
        if count == 0:
            print('f')
            sys.exit()

        if fahren >= -50 and fahren <= 130:
            return fahren

        else:
            print('please try again')
            count -= 1 
    
# Call the main function.
if __name__ == '__main__':
    main()
