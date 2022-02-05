def max_debit(bills):
    """ gets the maximum debit for a bill, returning the corresponding company """
    
    # using list comprehension to find the max from the amount list
    max_dr = max([bill[5] for bill in bills if bill[6] == "debit"])
    max_dr_year = []
    max_dr_name = []
    for bill in bills:
        if bill[5] == max_dr:
            if bill[6] == "debit":
                max_dr_year.append(bill[2])
                max_dr_name.append(bill[1])
                
    # prints the name and the amount of the highest debit
    print("="*60)  
       
    print("|{:^58}|".format('Report detailing the maximum debit'))

    print("="*60)

    row = '| {:<30} | {:>23} |'

    print(row.format('Name','Amount'))

    print("-"*60)

    for name in max_dr_name:    #iterates through the years and prints the key and values from the dictionary 

        print(row.format(name, max_dr))


    print()
    
    # adjusts for more than one equally high debit
    if len(max_dr_year) >1:
        text_dr = "The highest amount of a bill that is a debit is €{}.\nThis amount occurs in more than one year. The years are {}".format(max_dr, max_dr_year)
        print(text_dr)
        
    else:
        text_dr = "The highest amount of a bill that is a debit is €{}.\nThis amount occurs in the year {}".format(max_dr, max_dr_year[0])
        print(text_dr)
    


def max_credit(bills):
    """ gets the maximum credit for a bill, returning the corresponding company """
    
    max_cr = max([bill[5] for bill in bills if bill[6] == "credit"])
    max_cr_year = []
    max_cr_name = []
    for bill in bills:
        if bill[5] == max_cr:
            if bill[6] == "credit":
                max_cr_year.append(bill[2])
                max_cr_name.append(bill[1])
                
    # prints the name and amount of the highest credit         
    print("="*60)  
       
    print("|{:^58}|".format('Report detailing the maximum credit'))

    print("="*60)

    row = '| {:<30} | {:>23} |'

    print(row.format('Name','Amount'))

    print("-"*60)

    for name in max_cr_name:    #iterates through the years and prints the key and values from the dictionary 

        print(row.format(name,max_cr))


    print()
    
    # adjusts for more than one equally high credit        
    if len(max_cr_year) >1:
        text_cr = "The highest amount of a credited bill is €{}.\nThis amount occurs in more than one year. The years are {}\n".format(max_cr, max_cr_year)
        print(text_cr)
        
    else:
        text_dr = "The highest amount of a credited bill is €{}.\nThis amount occurs in the year {}\n".format(max_cr, max_cr_year[0])
        print(text_dr)
        