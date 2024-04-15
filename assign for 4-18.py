#Jalen Smith
#Cs 175-L
#Mr. Eckert
#4/13/2024

import os
import matplotlib.pyplot as plt

def main():

    try:
        
        with open('exp.txt', 'r') as infile:
            good_data = [data.split('\t') for data in infile]

        amounts = []
        slice_labels = []

        for data in good_data:
            try:
                amounts.append(float(data[1]))
                slice_labels.append(data[0])
            except ValueError:
                print("Error: Could not convert string to float:", data[1])

    except IOError:
        print("Error: Unable to open file:", 'expenses')
        exit()

    plt.pie(amounts, labels=slice_labels)
    plt.title('Sales by Quarter')
    plt.show()

if __name__ == '__main__':
    main()


