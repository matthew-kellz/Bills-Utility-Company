from datetime import datetime

def sorted_bills(bills):
    """ uses the datetime function to sort the bills, removes the date after its use """
    
    # a copy of bills is first created to be ordered
    sorted_list = []
    for bill in bills:
        sorted_list.append(bill)
    
    # the datetime date is appended to the end of each bill
    for bill in sorted_list:
        bill.append(datetime(bill[2], bill[3], bill[4]))
    
    # the bills are ordered by date, in the last index of each bill
    sorted_list = sorted(sorted_list, key=lambda x: x[-1])
    
    # the appended date is then removed 
    for bill in sorted_list:
        while len(bill) > 7:
            bill.pop()
            
    return sorted_list
   
def ask_y_n(message):
    """ allows only input of y or n """
    # while loop continues until no exception raised
    
    specific_choice = ''
    while specific_choice == '':
        
        try:
            specific_choice = input(message)
        
        except ValueError:
            print("Invalid input. The choice must be y or n.")
        
        # not in goes through list and sees if the input is not in it
        # this computational complexity is O(1) as it does not vary with the 
        # size of the input
        if specific_choice not in ["y", "n"]:    
             #this will send it to the print message and back to the input option
             specific_choice = ''
             print("Invalid input. The choice must be y or n.")
             
    return specific_choice

def unique_years(bills):
    """ creates a list containing only the unique years from bills """
    # initialize a null list
    unique_years = []
     
    # traverse for all elements
    for bill in bills:
        # check if exists in unique_list or not
        if bill[2] not in unique_years:
            unique_years.append(bill[2])
    # print list
    return unique_years
