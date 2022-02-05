def get_companies(bills):
    """ capitalizes each word in the company name and returns a list of the companies """
    
    # set an empty list
    company_list = list()
    # add each company from bills after capitalizing the first letter 
    for bill in bills:
        company_name = bill[0].title()
        company_list.append(company_name)
        
    return company_list

def freq_companies(bills):
    companies = get_companies(bills)
    freq_company = {}
    
    # a nested for loop means this function is O(n^2) 
    for company in companies:
        
        frequency = 0
        
        # company is the key and frequency is the value
        freq_company[company] = frequency
        
        for bill in bills: 
            
            if bill[0].title() == company:
                freq_company[company] += 1
            else:
                pass
            
    return freq_company