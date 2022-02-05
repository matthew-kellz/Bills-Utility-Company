from datetime import datetime

def inputFloat(message):
    """ takes input of type float, raises a ValueError if of other type """
    
    user_input = 0
    while user_input == 0: # continues asking for user input if not of type float
    
        try:
           user_input = float(input(message))
           
        except ValueError:
           print("\nThis is not a valid amount!")
           user_input = 0
       
    return user_input

def inputProvider(message):
    """ takes provider from user, repeats input prompt if all characters are digits """
    
    provider_input = ''
    
    while provider_input == '':
        
        provider_input = input(message)
            
        # initialises the number of digits to 0
        count = 0
        for char in provider_input:
            # values corresponding to the ASCII table for numbers
            if (ord(char) <65) or (ord(char) > 122):
                
                # for non-character the count increases by 1
                count+=1
                
        if count >= len(provider_input):
            provider_input = ''
            print("\nInvalid input.\nThere must be letters in the provider name.")
    
    return provider_input
            

def inputCustomer(message):
    """ accepts user input, raises a ValueError if every character is not a letter """
    
    customer_input = ''
    
    while customer_input == '':
        
        customer_input = input(message)
        
        if not customer_input.replace(" ", "").isalpha():# allows only letters 
            customer_input = ''
            print("\nInvalid customer name, only letters are allowed!")
        
    return customer_input
        

def ask_1_or_2(message):
    """ accepts input raising an error if the input is not 1 or 2"""
    
    user_input = 0
    
    while user_input == 0:
        
        try:
            user_input = int(input(message))
        
        except ValueError:
            print("\nThe input must be an integer!")
            continue
        
        if user_input not in [1,2]:
            
            user_input = 0
            print("\nThe number must be 1 or 2.")
            
    return user_input
            
def inputYear(message, input_type=str):
    """ takes input from the user, raising a ValueError if the input
    is not of the specified type 
    accepts only integers between the current year and 2010 """
    
    # the computational complexity of this while loop is O(n)
    year = 0
    
    while year == 0:
        
        try:
            # asks for input and converts to the specified type
            year = input_type(input(message))
           
       
        except ValueError: 
            # raises a ValueError if the input cannot be converted
            print("\nThe year must be an integer!")
            continue
        
        # year between this current year and 2010
        if year > datetime.today().year or year < 2010:
            print("\nThe year must be between 2010 and 2021")
            year = 0
        
    return year


def inputMonth(message, input_type=str):
    """ takes input for the month, between 1 and 12
    raises a ValueError if the input is invalid for type int is of invalid type """
    
    # The big Omega notation for this while loop is 1, the best case scenario
    month = 0
    
    while month == 0:
        
        try:
            month = input_type(input(message))
                                                   
        except ValueError:
            print("\nThe month must be an integer!")
            continue 
        
        # month between 1 and 12
        if month > 12 or month < 1:
            print("\nThe month must be between 1 and 12")
            month = 0
   
    return month
          
  
def checkLeap(year):
    """Checking if the given year is leap year"""  
    
    # returns a boolean, true corresponds to a leap year
    if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):   
        return True  
        
  # Else it is not a leap year  
    else:  
        return False
    
    
def inputDay(year,month, message, input_type=str):
    """ takes user input for day, ensures it is consistent with the year and 
    month entered. Raises a ValueError if input does not match the function 
    defined input """
    
    day = 0
    
    while day == 0:
        
        try:
            day = input_type(input(message))
            
        except:
            print("\nThe day must be a integer!")
            continue
        
        if month in [4,6,9,11]:
                
            if day > 30 or day < 1:
                print("\nThe day must be between 1 and 30") 
                day = 0
                
            else:
                return day
                
        # checks if month is Februrary
        elif month == 2:
            leap_check = checkLeap(year)
                
            # nested if statements here are O(n), there is a finite running time
            if leap_check == True:
                if day > 29 or day < 1:
                    
                    print("\nThe day must be between 1 and 29")
                    day = 0
                    
                else:
                    return day
                
            else:
                if day > 28 or day < 1:
                    
                    print("\nThe day must be between 1 and 28")
                    day = 0
                    
                else:
                    return day 
                    
        # else the month has 31 days
        else:
            
            if day > 31 or day < 1:
                print("\nThe day must be between 1 and 31")
                day = 0
                
            else:
                return day
            
    return day
          

