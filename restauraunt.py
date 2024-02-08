# CS 175 LAB
# JALEN SMITH
# PROFESSOR ECKERT 
# Restaurant


# print(Style.BRIGHT + Fore.RED + "CHEESY")


print( '''                Here are the restaurant options:)''' + '\n'  + 
'''
1. Joe's gourmet burgers ---> Vegetarian: (No) Vegan: (No) Gluten-Free (No)

2. Main street pizza company ---> Vegetarian: (Yes) Vegan: (No) Gluten-Free (Yes)

3. Corner Cafe ---> Vegetarian: (Yes) Vegan: (Yes) Gluten-Free (Yes)

4. Mama's Fine Italian ---> Vegetarian: (Yes) Vegan: (No) Gluten-Free (No)

5. The Chef's Kitchen ---> Vegetarian: (Yes) Vegan: (Yes) Gluten-Free (Yes)''')

print(' ')

while True:
  
  vegetarian = input('              Is anyone in your party vegetarian?: ')
  print(' ')
  
  vegan = input('                   Is anyone in your party vegan?: ')
  print(' ')
  
  gluten_free = input('             Is anyone in your party gluten-free?: ')
  print(' ')
  
  

  if vegetarian.lower() == 'yes' and vegan.lower() == 'yes' and gluten_free.lower() == 'yes':
    print(' ')
    print(f'''              The restaurant options are: 
    
                                    Corner Cafe
                                    
                                       and 
                                       
                                  The Chef's Kitchen
    ''')
    break

  elif vegetarian.lower() == 'yes' and vegan.lower() == 'yes' and gluten_free.lower() == 'no':
    print(' ')
    print(f'''               The restaurant options are:
    
                                      Corner Cafe
                                     
                                         and 
                                         
                                    The Chef's Kitchen
    ''')
    break

  elif vegetarian.lower() == 'no' and vegan.lower() == 'yes' and gluten_free.lower() == 'yes':
    print(' ')
    print(                f'''The restaurant options are: 
    
                                     Corner Cafe 
                                     
                                        and 
                                        
                                  The Chef's Kitchen
    ''')
    break

  elif vegetarian.lower() == 'no' and vegan.lower() == 'yes' and gluten_free.lower() == 'no':
    print(' ')
    print(                f'''The restaurant options are: 
    
                                     Corner Cafe 
                                     
                                         and 
                                         
                                    The Chef's Kitchen
    ''')
    break

  elif vegetarian.lower() == 'yes' and vegan.lower() == 'no' and gluten_free.lower() == 'yes':
    print(' ')
    print(              f'''The restaurant options are: 
    
                            Main Street Pizza Company 
                                
                                       and 
                                       
                                   Corner Cafe 
                                   
                                       and 
                                       
                                The Chef's Kitchen
    ''')
    break

  elif vegetarian.lower() == 'no' and vegan.lower() == 'no' and gluten_free.lower() == 'yes':
    print(' ')
    print(             f'''The restaurant options are: 
    
                            Main Street Pizza Company 
                                
                                      and 
                                      
                                  Corner Cafe 
                                  
                                      and 
                                      
                                The Chef's Kitchen
    ''')
    break

  elif vegetarian.lower() == 'yes' and vegan.lower() == 'no' and gluten_free.lower() == 'no':
    print(' ')
    print(             f'''The restaurant options are: 
    
                               Mama's Fine Italian 
                              
                                     and 
                                     
                              Main Street Pizza Company 
                              
                                     and 
                                     
                                  Corner Cafe 
                                
                                     and 
                                     
                              The Chef's Kitchen
    ''')
    break

  elif vegetarian.lower() == 'no' and vegan.lower() == 'no' and gluten_free.lower() == 'no':
    print(' ')
    print(               f'''The restaurant options are: 
    
                                Joe's Gourmet Burgers 
                                
                                      and 
                                      
                                Mama's Fine Italian
                                
                                      and
                                      
                                Main Street Pizza Company
                                
                                      and 
                                      
                                   Corner Cafe
       
                                      and 
                                      
                                  Chef's Kitchen
    ''')
    break

