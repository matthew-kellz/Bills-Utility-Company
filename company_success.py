def total_bills(bills):
    """ creates a dictionary with keys of total amount and values of the added amounts"""
    
    total_debited_bills = 0
    total_credited_bills = 0
    for bill in bills:
        if bill[-1] == "debit":
            total_debited_bills += 1
        else:
            total_credited_bills += 1
            
    # an empty dictionary
    total_breakdown = {}
    # the value is assigned to its corresponding key
    total_breakdown["total_debits"] = total_debited_bills
    total_breakdown["total_credits"] = total_credited_bills
    
    return total_breakdown
