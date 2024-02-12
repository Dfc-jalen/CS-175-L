#JALEN SMITH
#C175-L
#PROF ECKERT

# import sys
# import os
# from colorama import init, Fore, Back, Style

# Initializes Colorama
# init(autoreset=True)

# print(Style.BRIGHT + Fore.RED + "CHEESY")


print( '''                Here are the restaurant options:)''' + '\n' +  
'''
1. Joe's gourmet burgers ---> Vegetarian: (No) Vegan: (No) Gluten-Free (No)

2. Main street pizza company ---> Vegetarian: (Yes) Vegan: (No) Gluten-Free (Yes)

3. Corner Cafe ---> Vegetarian: (Yes) Vegan: (Yes) Gluten-Free (Yes)

4. Mama's Fine Italian ---> Vegetarian: (Yes) Vegan: (No) Gluten-Free (No)

5. The Chef's Kitchen ---> Vegetarian: (Yes) Vegan: (Yes) Gluten-Free (Yes)''')

print(' ')

while True:
  try:
    
    vegetarian = input('              Is anyone in your party vegetarian?: ')
    print(' ')
    print( vegetarian)
    print(' ')
    
    if vegetarian != 'yes':
      print('try again')
      continue
    elif vegetarian == 'yes':
      vegetarian = 'yes'

    elif vegetarian == 'no':
      vegetarian = 'no'
      
    elif  vegetarian != 'no':
      print('try again')
    try:
      
      vegan = input('                   Is anyone in your party vegan?: ')
      print(' ')
      print( (vegan))
      print(' ')
      
      
      if vegan != 'yes':
        print('try again')
      
        
      
      elif vegan == 'yes':
        vegan = 'yes'
  
      elif  vegan != 'no':
        print('try again')
        


      gluten_free = input('             Is anyone in your party gluten-free?: ')
      print(' ')
      print( (gluten_free))
      print(' ')
      
      
        
        
      if gluten_free != 'yes' and gluten_free == 'no':
        print('try again')

      if gluten_free == 'yes':
        gluten_free = 'yes'
        
        if vegetarian.lower() == 'yes' and vegan.lower() == 'yes' and gluten_free.lower() == 'yes':
          print(' ')
          print(f'''The restaurant options are: 
  
                                            Corner Cafe
  
                                               and 
  
                                          The Chef's Kitchen
            ''')
          break
  
        elif vegetarian.lower() == 'yes' and vegan.lower() == 'yes' and gluten_free.lower() == 'no':
            print(' ')
            print( f'''The restaurant options are:
  
                                              Corner Cafe
  
                                                 and 
  
                                            The Chef's Kitchen
            ''')
            break
  
        elif vegetarian.lower() == 'no' and vegan.lower() == 'yes' and gluten_free.lower() == 'yes':
            print(' ')
            print( f'''The restaurant options are: 
  
                                             Corner Cafe 
  
                                                and 
  
                                          The Chef's Kitchen
            ''')
            break
  
        elif vegetarian.lower() == 'no' and vegan.lower() == 'yes' and gluten_free.lower() == 'no':
            print(' ')
            print( f'''The restaurant options are: 
  
                                             Corner Cafe 
  
                                                 and 
  
                                            The Chef's Kitchen
            ''')
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
            break
  
  
  
  
  
        if vegetarian.lower() == 'yes' and vegan.lower() == 'yes' and gluten_free.lower() == 'yes':
            print(' ')
            print(f'''The restaurant options are: 
  
                                            Corner Cafe
  
                                               and 
  
                                          The Chef's Kitchen
            ''')
            break
  
        elif vegetarian.lower() == 'yes' and vegan.lower() == 'yes' and gluten_free.lower() == 'no':
            print(' ')
            print(Style.BRIGHT + Fore.LIGHTCYAN_EX + f'''The restaurant options are:
  
                                              Corner Cafe
  
                                                 and 
  
                                            The Chef's Kitchen
            ''')
            break
  
        elif vegetarian.lower() == 'no' and vegan.lower() == 'yes' and gluten_free.lower() == 'yes':
            print(' ')
            print(Style.BRIGHT + Fore.LIGHTWHITE_EX + f'''The restaurant options are: 
  
                                             Corner Cafe 
  
                                                and 
  
                                          The Chef's Kitchen
            ''')
            break
  
        elif vegetarian.lower() == 'no' and vegan.lower() == 'yes' and gluten_free.lower() == 'no':
            print(' ')
            print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + f'''The restaurant options are: 
  
                                             Corner Cafe 
  
                                                 and 
  
                                            The Chef's Kitchen
            ''')
            break
  
        elif vegetarian.lower() == 'yes' and vegan.lower() == 'no' and gluten_free.lower() == 'yes':
            print(' ')
            print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + f'''The restaurant options are: 
  
                                    Main Street Pizza Company 
  
                                               and 
  
                                           Corner Cafe 
  
                                               and 
  
                                        The Chef's Kitchen
            ''')
            break
  
        elif vegetarian.lower() == 'no' and vegan.lower() == 'no' and gluten_free.lower() == 'yes':
            print(' ')
            print(Style.BRIGHT + Fore.LIGHTBLUE_EX + f'''The restaurant options are: 
  
                                    Main Street Pizza Company 
  
                                              and 
  
                                          Corner Cafe 
  
                                              and 
  
                                        The Chef's Kitchen
            ''')
            break
  
        elif vegetarian.lower() == 'yes' and vegan.lower() == 'no' and gluten_free.lower() == 'no':
            print(' ')
            print(Style.BRIGHT + Fore.GREEN + f'''The restaurant options are: 
  
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
            print(Style.BRIGHT + Fore.RED + f'''The restaurant options are: 
  
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
  
      elif gluten_free == 'no':
        gluten_free = 'no'
        if vegetarian.lower() == 'yes' and vegan.lower() == 'yes' and gluten_free.lower() == 'yes':
          print(' ')
          print(f'''The restaurant options are: 

                                            Corner Cafe

                                               and 

                                          The Chef's Kitchen
            ''')
          break

        elif vegetarian.lower() == 'yes' and vegan.lower() == 'yes' and gluten_free.lower() == 'no':
            print(' ')
            print( f'''The restaurant options are:

                                              Corner Cafe

                                                 and 

                                            The Chef's Kitchen
            ''')
            break

        elif vegetarian.lower() == 'no' and vegan.lower() == 'yes' and gluten_free.lower() == 'yes':
            print(' ')
            print( f'''The restaurant options are: 

                                             Corner Cafe 

                                                and 

                                          The Chef's Kitchen
            ''')
            break

        elif vegetarian.lower() == 'no' and vegan.lower() == 'yes' and gluten_free.lower() == 'no':
            print(' ')
            print( f'''The restaurant options are: 

                                             Corner Cafe 

                                                 and 

                                            The Chef's Kitchen
            ''')
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
            break





        if vegetarian.lower() == 'yes' and vegan.lower() == 'yes' and gluten_free.lower() == 'yes':
            print(' ')
            print(f'''The restaurant options are: 

                                            Corner Cafe

                                               and 

                                          The Chef's Kitchen
            ''')
            break

        elif vegetarian.lower() == 'yes' and vegan.lower() == 'yes' and gluten_free.lower() == 'no':
            print(' ')
            print(Style.BRIGHT + Fore.LIGHTCYAN_EX + f'''The restaurant options are:

                                              Corner Cafe

                                                 and 

                                            The Chef's Kitchen
            ''')
            break

        elif vegetarian.lower() == 'no' and vegan.lower() == 'yes' and gluten_free.lower() == 'yes':
            print(' ')
            print(Style.BRIGHT + Fore.LIGHTWHITE_EX + f'''The restaurant options are: 

                                             Corner Cafe 

                                                and 

                                          The Chef's Kitchen
            ''')
            break

        elif vegetarian.lower() == 'no' and vegan.lower() == 'yes' and gluten_free.lower() == 'no':
            print(' ')
            print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + f'''The restaurant options are: 

                                             Corner Cafe 

                                                 and 

                                            The Chef's Kitchen
            ''')
            break

        elif vegetarian.lower() == 'yes' and vegan.lower() == 'no' and gluten_free.lower() == 'yes':
            print(' ')
            print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + f'''The restaurant options are: 

                                    Main Street Pizza Company 

                                               and 

                                           Corner Cafe 

                                               and 

                                        The Chef's Kitchen
            ''')
            break

        elif vegetarian.lower() == 'no' and vegan.lower() == 'no' and gluten_free.lower() == 'yes':
            print(' ')
            print(Style.BRIGHT + Fore.LIGHTBLUE_EX + f'''The restaurant options are: 

                                    Main Street Pizza Company 

                                              and 

                                          Corner Cafe 

                                              and 

                                        The Chef's Kitchen
            ''')
            break

        elif vegetarian.lower() == 'yes' and vegan.lower() == 'no' and gluten_free.lower() == 'no':
            print(' ')
            print(Style.BRIGHT + Fore.GREEN + f'''The restaurant options are: 

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
            print(Style.BRIGHT + Fore.RED + f'''The restaurant options are: 

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
  
    
    except:
    
      if vegetarian.lower() == 'yes' and vegan.lower() == 'yes' and gluten_free.lower() == 'yes':
        print(' ')
        print(f'''The restaurant options are: 
  
                                        Corner Cafe
  
                                           and 
  
                                      The Chef's Kitchen
        ''')
        break
  
      elif vegetarian.lower() == 'yes' and vegan.lower() == 'yes' and gluten_free.lower() == 'no':
        print(' ')
        print( f'''The restaurant options are:
  
                                          Corner Cafe
  
                                             and 
  
                                        The Chef's Kitchen
        ''')
        break
  
      elif vegetarian.lower() == 'no' and vegan.lower() == 'yes' and gluten_free.lower() == 'yes':
        print(' ')
        print( f'''The restaurant options are: 
  
                                         Corner Cafe 
  
                                            and 
  
                                      The Chef's Kitchen
        ''')
        break
  
      elif vegetarian.lower() == 'no' and vegan.lower() == 'yes' and gluten_free.lower() == 'no':
        print(' ')
        print( f'''The restaurant options are: 
  
                                         Corner Cafe 
  
                                             and 
  
                                        The Chef's Kitchen
        ''')
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
        break
  
    
    
    
  
      if vegetarian.lower() == 'yes' and vegan.lower() == 'yes' and gluten_free.lower() == 'yes':
        print(' ')
        print(f'''The restaurant options are: 
        
                                        Corner Cafe
                                        
                                           and 
                                           
                                      The Chef's Kitchen
        ''')
        break
    
      elif vegetarian.lower() == 'yes' and vegan.lower() == 'yes' and gluten_free.lower() == 'no':
        print(' ')
        print(Style.BRIGHT + Fore.LIGHTCYAN_EX + f'''The restaurant options are:
        
                                          Corner Cafe
                                         
                                             and 
                                             
                                        The Chef's Kitchen
        ''')
        break
    
      elif vegetarian.lower() == 'no' and vegan.lower() == 'yes' and gluten_free.lower() == 'yes':
        print(' ')
        print(Style.BRIGHT + Fore.LIGHTWHITE_EX + f'''The restaurant options are: 
        
                                         Corner Cafe 
                                         
                                            and 
                                            
                                      The Chef's Kitchen
        ''')
        break
    
      elif vegetarian.lower() == 'no' and vegan.lower() == 'yes' and gluten_free.lower() == 'no':
        print(' ')
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + f'''The restaurant options are: 
        
                                         Corner Cafe 
                                         
                                             and 
                                             
                                        The Chef's Kitchen
        ''')
        break
    
      elif vegetarian.lower() == 'yes' and vegan.lower() == 'no' and gluten_free.lower() == 'yes':
        print(' ')
        print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + f'''The restaurant options are: 
        
                                Main Street Pizza Company 
                                    
                                           and 
                                           
                                       Corner Cafe 
                                       
                                           and 
                                           
                                    The Chef's Kitchen
        ''')
        break
    
      elif vegetarian.lower() == 'no' and vegan.lower() == 'no' and gluten_free.lower() == 'yes':
        print(' ')
        print(Style.BRIGHT + Fore.LIGHTBLUE_EX + f'''The restaurant options are: 
        
                                Main Street Pizza Company 
                                    
                                          and 
                                          
                                      Corner Cafe 
                                      
                                          and 
                                          
                                    The Chef's Kitchen
        ''')
        break
    
      elif vegetarian.lower() == 'yes' and vegan.lower() == 'no' and gluten_free.lower() == 'no':
        print(' ')
        print(Style.BRIGHT + Fore.GREEN + f'''The restaurant options are: 
        
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
        print(Style.BRIGHT + Fore.RED + f'''The restaurant options are: 
        
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
  
  
  
  
      
    
    
  except:
    print(' ')
