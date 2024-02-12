#Jalen Smith
#11/30/2020
#Mr. Eckert 
#Computer Science
#Cs 175L 

print( '''                Here are the restaurant options:)''' + '\n' +  
'''
1. Joe's gourmet burgers ---> Vegetarian: (No) Vegan: (No) Gluten-Free (No)

2. Main street pizza company ---> Vegetarian: (Yes) Vegan: (No) Gluten-Free (Yes)

3. Corner Cafe ---> Vegetarian: (Yes) Vegan: (Yes) Gluten-Free (Yes)

4. Mama's Fine Italian ---> Vegetarian: (Yes) Vegan: (No) Gluten-Free (No)

5. The Chef's Kitchen ---> Vegetarian: (Yes) Vegan: (Yes) Gluten-Free (Yes)''')

while True:
  print(' ')
  vegetarian = input('              Is anyone in your party vegetarian?: ')
  print(' ')
  print( vegetarian)
  print(' ')

  vegan = input('                   Is anyone in your party vegan?: ')
  print(' ')
  print( (vegan))
  print(' ')

  gluten_free = input('             Is anyone in your party gluten-free?: ')
  print(' ')
  print( (gluten_free))
  print(' ')


  if vegetarian.lower() == 'yes' and vegan.lower() == 'yes' and gluten_free.lower() == 'yes':
    
    print(' ')
    print(f'''The restaurant options are: 
  
                                      Corner Cafe
  
                                         and 
  
                                    The Chef's Kitchen
      ''')
    
    
    ask = (input('Do you want to see the restaurant options again?  yes or no): '))
    
    if ask == 'yes':
      continue
    if ask == 'no':
      print('Alright have a good day!')
      break
  
  elif vegetarian.lower() == 'yes' and vegan.lower() == 'yes' and gluten_free.lower() == 'no':
      print(' ')
      print( f'''The restaurant options are:
  
                                        Corner Cafe
  
                                           and 
  
                                      The Chef's Kitchen
      ''')
  ask1 = (input('Do you want to see the restaurant options again? (yes or no ): '))

  if ask1 == 'yes':
    continue
  if ask1 == 'no':
    print('Alright have a good day!')
    break
  
  elif vegetarian.lower() == 'no' and vegan.lower() == 'yes' and gluten_free.lower() == 'yes':
      print(' ')
      print( f'''The restaurant options are: 
  
                                       Corner Cafe 
  
                                          and 
  
                                    The Chef's Kitchen
      ''')
  ask1 = (input('Do you want to see the restaurant options again? (yes or no): '))

    
  if ask1 == 'yes':
    continue
  if ask1 == 'no':
    print('Alright have a good day!')
    break
    
      
  
  elif vegetarian.lower() == 'no' and vegan.lower() == 'yes' and gluten_free.lower() == 'no':
      print(' ')
      print( f'''The restaurant options are: 
  
                                       Corner Cafe 
  
                                           and 
  
                                      The Chef's Kitchen
      ''')
  ask = (input('Do you want to see the restaurant options again? ( yes or no): '))
  if ask == 'yes':
    continue
  if ask == 'no':
    print('Alright have a good day!')
    break
      
  
  elif vegetarian.lower() == 'yes' and vegan.lower() == 'no' and gluten_free.lower() == 'yes':
      print(' ')
      print( f'''The restaurant options are: 
  
                              Main Street Pizza Company 
  
                                         and 
  
                                     Corner Cafe 
  
                                         and 
  
                                  The Chef's Kitchen
      ''')
  ask = (input('Do you want to see the restaurant options again? yes or no): '))
  if ask == 'yes':
    continue
  if ask == 'no':
    print('Alright have a good day!')
    break
      
  
  elif vegetarian.lower() == 'no' and vegan.lower() == 'no' and gluten_free.lower() == 'yes':
      print(' ')
      print( f'''The restaurant options are: 
  
                              Main Street Pizza Company 
  
                                        and 
  
                                    Corner Cafe 
  
                                        and 
  
                                  The Chef's Kitchen
      ''')
  ask = (input('Do you want to see the restaurant options again? yes or no: '))
  if ask == 'yes':
    continue
  if ask == 'no':
    print('Alright have a good day!')
    break
      
  
  elif vegetarian.lower() == 'yes' and vegan.lower() == 'no' and gluten_free.lower() == 'no':
      print(' ')
      print( f'''The restaurant options are: 
  
                                 Mama's Fine Italian 
  
                                       and 
  
                                Main Street Pizza Company 
  
                                       and 
  
                                    Corner Cafe 
  
                                       and 
  
                                The Chef's Kitchen
      ''')
  ask = (input('Do you want to see the restaurant options again? ( yes or no): '))
  if ask == 'yes':
    continue
  if ask == 'no':
    print('Alright have a good day!')
    break
      
  
  elif vegetarian.lower() == 'no' and vegan.lower() == 'no' and gluten_free.lower() == 'no':
      print(' ')
      print( f'''The restaurant options are: 
  
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
  ask = (input('Do you want to see the restaurant options again? ( yes or no): '))
  if ask == 'yes':
    continue
    
  if ask == 'no':
    print('Alright have a good day!')
    break
      
  
  
  
  
  
  
