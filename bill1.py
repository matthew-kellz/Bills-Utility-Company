from tabulate import tabulate
from datetime import datetime
from writing_bills import inputFloat, inputProvider, inputCustomer, ask_1_or_2, inputYear, inputMonth, inputDay
from yearly_report import get_years
from popular_company import  freq_companies
from bills_date_order import sorted_bills, ask_y_n, unique_years
from report_max import max_debit, max_credit
from company_success import total_bills
from report_menu import get_report_option

###############################################################################
# Question 2. writing and reading utility bills to bills.csv
###############################################################################
def get_input():
    
    user_preference = input("Please choose an option: ")
    
    return user_preference

def get_choice():
    """ display menu and ask for user choice """
    
    #Create a matrix of the different menu titles for use in the tabulate function
    options_list = [["View Bills"], ["Add New Bill"], ["Reports Menu"], ["Read T&Cs."], ["Exit Program"]]
    
    table_choices = tabulate(options_list, 
                   headers = ["Welcome to the Utility Billing Management System"], 
                   tablefmt = "fancy_grid", 
                   showindex= range(1, len(options_list)+1),
                   numalign = "center",
                   )
   
    print(table_choices)
    
    #return the user input specifying which choice they want
    user_option = get_input()
    
    return user_option


def read_bills(file_name = "bills.csv"):
    """Read bills from the file system 'bills.csv'
    The computational complexity of this function is O(n) """
    
    bills = []
    
    for line in open(file_name):
        # convert a line into a list of values
        # based on the comma separator
        bill = line.strip().split(',')
        bill[0] = bill[0].strip()
        bill[1] = bill[1].strip()
        for i in range(2,5):
            bill[i] = int(bill[i].strip())
        bill[5] = float(bill[5].strip())
        bill[6] = bill[6].strip()
        bills.append(bill)
   
    return bills

bills = read_bills(file_name = "bills.csv")
def write_bills(bills):
    """Write bills to the file system 'bills.csv'
    The computational complexity of this function is O(n) """
    
    bills_file = open("bills.csv", "w")
    
    for bill in bills: 
        # convert the bill into a comma separated list
        # ensure every index in each bill is a string
        for i in range(2,6):
            bill[i] = str(bill[i])
        
        #Remove extra columns the sort by date function added in
        while len(bill) >=8:
            bills.pop()
        bills_file.write(', '.join(bill) + '\n')
     
    # close the file after writing to it
    bills_file.close()


def view_bills(bills):
    """ Read bills from the file system bills.csv and 
    display bills using the tabulate module """
    
    table_output = tabulate(bills, 
                   headers = ["Company", "Name", "Year", "Month", "Day", "Amount", "Debit/Credit"], 
                   tablefmt = "fancy_grid", 
                   showindex= range(1, len(bills)+1),
                   numalign = "center",
                   )
        
    print(table_output)

    
def read_t_and_c():
    """ reads each line of the terms and conditions from a .txt file,
    printing each line """
    
    print()
    
    for line in open('t&c.txt'):
        
        # the computational complexity of this for loop is O(n) 
        print(line.strip('\n'))
        
    print()
    
###############################################################################
# User entering utility bill details
###############################################################################           

   
def add_new_bill(bills):
    """ creates a list of user input to append to bills """
    
    # variables assigned specific inputs
    provider = inputProvider("Please enter a provider: ") 
    customer = inputCustomer("Please enter the first name of the customer: ") + ' ' + inputCustomer("Please enter the second name of the customer: ")
    year = inputYear("Please enter a valid year (YYYY): ", int)
    #Change so they are only entering one date? And then it is split and assigned
    month = inputMonth("Please enter a valid month (MM): ", int)
    day = inputDay(year, month, "Please enter a valid day (DD): ", int)
    amount = inputFloat("Please enter an amount: ")
    debit_credit = ask_1_or_2("Please enter 1 for debit and 2 for credit: ")
    
    # to add a bill to a list - use append
    # variables appended to a list 
    bill = []
    bill.append(provider)
    bill.append(customer)
    bill.append(year)
    bill.append(month)
    bill.append(day)
    bill.append(amount)
    
    
    if debit_credit == 1:
        bill.append("debit")
    else:
        bill.append("credit")
        
    bills.append(bill)
    
    write_bills(bills)

###############################################################################
#Question 3. Report listing years, debits and credits
###############################################################################       

def yearly_report(bills):
    """ creating a matrix for debits and credits per year and a table summary
    finds the max yearly debits and credits and their years """
    
    years = get_years(bills)
    yearly_bills = []
    for year in years:
        
        # a list for each year, their total debits and total credits
        year_list = [year, 0, 0]
        
        # function with computational complexity of O(n^2), caused by the nested for loop
        for bill in bills: 
            if bill[2] == year:
                if bill[-1] == 'debit':
                    year_list[1] += bill[5]
                else:
                    year_list[2] += bill[5]
            else:
                pass
        
        # appends each yearly list to the matrix
        yearly_bills.append(year_list)
    
    table_output = tabulate(yearly_bills, 
                   headers = ["Year", "Total Debited", "Total Credited"], 
                   tablefmt = "fancy_grid", 
                   showindex= range(1, len(yearly_bills)+1),
                   numalign = "center",
                   )
    
    max_debit = 0
    max_credit = 0

    for year in yearly_bills:
        
        #updates the max debits and credits as it moves through the matrix
        if year[1] > max_debit:
            max_debit = year[1]
        
        else:
            pass
        
        if year[2] > max_credit:
            max_credit = year[2]
        else:
            pass
    
        
    max_dr_year = 0
    max_cr_year = 0
    
    for year in yearly_bills:
        
        # the year which has the highest debit 
        if year[1] == max_debit:
            max_dr_year = year[0]
        else:
            pass
        
        # the year with the highest credit
        if year[2] == max_credit:
            max_cr_year = year[0]
        else:
            pass
        
    text_dr = "The maximum amount of yearly debits are €{max_dr}, this amount occurs in the year {year}".format(max_dr = round(max_debit, 2), year = max_dr_year)
    text_cr = "The maximum amount of yearly credits are €{max_cr}, this amount occurs in the year {year}".format(max_cr = round(max_credit, 2), year = max_cr_year)
    
    print(table_output)
    print(text_dr, "\n")
    print(text_cr, "\n")

###############################################################################
#Question 4. Report showing the most popular utility company.  
###############################################################################


def popular_companies(bills):
    """ creates a dictionary of each company and its frequency """
    
    company_freq = freq_companies(bills)
            
    count = 0
    popular_company = ''
    
    # iterates through dictionary and finds the highest value for frequency
    for company in company_freq:
        
        if company_freq[company] >= count:
            count = company_freq[company]
            popular_company = company
            
        else:
            pass
       
    print("="*60)  
       
    # centres text in the middle of the title
    print("|{:^58}|".format('Report detailing the popularity of each utility company'))

    print("="*60)

    row = '| {:<30} | {:>23} |'

    print(row.format('Company','Frequency'))

    print("-"*60)

    for company in company_freq:    #iterates through the years and prints the key and values from the dictionary 

        print(row.format(company, company_freq[company]))

        print("-"*60)

    print()
    
    print("The most popular utility company is measured using the amount of bills charged against each provider.\n")
    # list comprehension to access the keys from the dictionary for the most popular company
    keys = [k for k, v in company_freq.items() if v == count]
    if len(keys) == 1:
        
        text_most_popular = "The most popular utility company is {company} and the amount of bills charged against them is {amount}.\n".format(company = popular_company, amount = count)
        print(text_most_popular)
    
    else:
        
        text_most_popular = "The joint most popular companies are {companies} and the amount of bills charged against them is {amount}\n".format(companies = set(company for company in keys), amount = count)
        print(text_most_popular)
     
    

###############################################################################
# Question 5. Report showing the bills in date order
###############################################################################


def ask_specific_year(message):
    """ request specific year from user to summarise bills for and
    exception raised if year is not in the bills.
    Year must be of type int """
    
    different_years = unique_years(bills)
    specific_years = sorted(different_years)
    
    # allows user see the years to choose from
    print("\nThe different years to choose from are ", *specific_years)
    
    
    year_requested = ''
    while year_requested == '':
        try:
            year_requested = int(input(message))
        
        # ValueError raised if year is not in the years for bills
        except ValueError:
            print("\nInvalid input.\nPlease enter a number from the following list", *specific_years)
            continue
        
        if year_requested not in specific_years:
            year_requested = ''
            print("\nPlease choose a year from the specified list!")        
        
    return year_requested


def bills_specific_year(bills): 
    """ creates a matrix of bills only for the specified year and 
    returns the matrix """
        
    year = ask_specific_year("Please enter the year you would like to see the bills for:")
        
    year_bill_list = []
        
    # list of bills with specified year created using a for loop and append
    for bill in bills:
        if bill[2] == year:
            year_bill_list.append(bill)
                
        else:
            pass
        
    # date is created by concatenating strings for year, month and day
    shorter_list = []
    for item in year_bill_list:
        date = str(item[4]) + "/" + str(item[3]) + "/" + str(item[2])
        table_info = item[:2] + item[5:7]
        table_info.append(date)
        shorter_list.append(table_info)
            
        
    return shorter_list

        
def report_date_order(bills):
    """ reports bills ordered from oldest to newest or vice versa.
    summarises bills for a specific year if user requests """
    
    sorted_list = sorted_bills(bills)
            
    # asks user for monthly or yearly summary
    input_order = ask_1_or_2("Please enter 1 to see bills from lowest to highest,\n" +
                             "Please enter 2 to see bills from highest to lowest.\n"+
                             "Enter:")
    
    # summarises by year if input is 1
    if input_order == 1:
        print("="*74)
        print("|{:^72}|".format("A summary of the bills from Lowest to Highest"))
        print("="*74)
        row = '|{:<10}|{:^19}|{:^15}|{:^10}|{:^14}| '
        print(row.format('Date','Company', 'Name', 'Amount', "Debit/Credit"))
        print("+", "-"*70, "+")
        for item in sorted_list:
            date = str(item[4]) + "/" + str(item[3]) + "/" + str(item[2])
            print(row.format(date, item[0], item[1], item[5], item[6]))
            print("+", "-"*70, "+")
       
    # summarises by month if input is 2
    else:
        print("="*74)
        print("|{:^72}|".format("A summary of the bills from Highest to Lowest"))
        print("="*74)
        row = '|{:<10}|{:^19}|{:^15}|{:^10}|{:^14}| '
        print(row.format('Date','Company', 'Name', 'Amount', "Debit/Credit"))
        print("-"*72)
        for item in reversed(sorted_list):
            date = str(item[4]) + "/" + str(item[3]) + "/" + str(item[2])
            print(row.format(date, item[0], item[1], item[5], item[6]))
            print("+", "-"*70, "+")
    
            
    specific_year = ask_y_n("Would you like to see a specific year (y/n)?:")
    
    # summarises specific year if user input is "y"
    if specific_year == "y":
        shorter_list = bills_specific_year(bills)
        
        table_output = tabulate(shorter_list, 
                   headers = ["Company", "Name", "Amount", "Debit/Credit", "Date"], 
                   tablefmt = "fancy_grid", 
                   showindex= range(1, len(shorter_list)+1),
                   numalign = "center",
                   )
        
        print(table_output)
        
    # returns nothing otherwise
    else:
        return
    
###############################################################################
# Question 6.  Report displaying the highest amount for a bill that is a 
# credit, and one for a debit.
###############################################################################

def ask_max(bills):
    """ returns max_debit or max_credit based on user preference """
    
    input_max = ask_1_or_2("Please enter 1 to see the maximum debited amount,\n"+
                           "Please enter 2 to see the maximum credited amount.\n"+
                           "Enter:")
    
    if input_max == 1:
        return max_debit(bills)
    
    else:
        return max_credit(bills)
    
###############################################################################
#Question 7. A report to indicate how successful the company is
###############################################################################

def company_success(bills):
    """ details the number of bills and therefore the company's success """
    
    total_breakdown = total_bills(bills)
    
    different_years = unique_years(bills)
    
    # dictionary created with years as keys and frequency for each year as values
    years_frequency = {}
    
    # nested for loops have a complexity of O(n^2)
    for year in different_years:
        
        # frequency begins at 0 and increases by the amt of each bill in that year
        frequency = 0
        years_frequency[year] = frequency
        
        for bill in bills:
            if bill[2] == year:
                years_frequency[year] += 1
            else:
                pass
            
           
    print("="*60)
        
    print("|{:^58}|".format('Report detailing the frequency of bills in each year'))

    print("="*60)

    row = '| {:<30} | {:>23} |'

    print(row.format('Year','Frequency'))

    print("-"*60)

    for year in different_years: #iterates through the years and prints the key and values from the dictionary 

        print(row.format(year, years_frequency[year]))
        
        print("-"*60)

    print()       
    
    print('The total number of bills outlines the success of the company.\n'+
          "The number of bills currently is {length}\n".format(length = len(bills)))
    print("The number of bills debited to the company is {debit} \nThe number of bills credited to the company is {credit}".format(debit = total_breakdown["total_debits"], credit = total_breakdown["total_credits"]))


###############################################################################
#Question 8. The average spent per period of time(month/year) that can be entered 
# by the user.      
###############################################################################
def yearly_spend(bills):
    """ calculates the average debits, credits, total and average spent 
    classified as the average difference between debits and credits """
    
    # initializes each total to 0 and adds to each one as one iterates through bills
    total_figure = 0
    different_years = unique_years(bills)
    total_debited = 0
    total_credited = 0
    
    # updating total figure
    for bill in bills:
        total_figure += bill[-2]
    
    # updating total debits and credits
    for bill in bills:
        if bill[-1] == "debit":
            total_debited += bill[-2]
            
        else:
            total_credited += bill[-2]
            
    # the first entry in the matrix, total_amt
    # each total is divided by the length of bills to get the average
    
    total_amt = []
    
    average_yearly_total = round(total_figure/len(different_years),2)
    average_yearly_debit = round(total_debited/len(different_years), 2)
    average_yearly_credit = round(total_credited/len(different_years), 2)
    average_yearly_spend = round((total_debited - total_credited)/ len(different_years), 2)
    
    total_column = ["Totals", average_yearly_debit, average_yearly_credit, average_yearly_total, average_yearly_spend]
    total_amt.append(total_column)
    
    return total_amt


def spend_each_year(bills):
    """ calculates the averages for each year in bills and appends to the matrix """
    
    total_amt = yearly_spend(bills)
    different_years = unique_years(bills)
            
    # each total is set to 0 for each year and increased accordingly
    # this nested for loop checks each year for each bill in bills
    for year in different_years:
        yearly_total = 0
        yearly_debit = 0
        yearly_credit = 0
        total_freq = 0

        for bill in bills: 
            if bill[2] == year:
                total_freq += 1
                yearly_total += bill[-2]
                if bill[-1] == "debit":
                    yearly_debit += bill[-2]
                else:
                    yearly_credit += bill[-2]
                    
            else:
                pass 
            
        # adds the summary of each year to the matrix
        year_summary = [year, round(yearly_debit/total_freq, 2), round(yearly_credit/total_freq, 2), round(yearly_total/total_freq, 2), round((yearly_debit - yearly_credit)/total_freq, 2)]
        
        total_amt.append(year_summary)
    return total_amt


def average_spend(bills):
    """ displays a summary of the average spent by year or month. 
    displays a summary for a specific time period at the users request """
    
    time_period = ask_1_or_2("Would you like to see the average spend by month or year?\n"+
                             "Please enter 1 to see the breakdown by year,\n"+
                             "Please enter 2 to see the breakdown by month.\nEnter: ")
    
    total_amt = spend_each_year(bills)
    
    # yearly summary for 1 
    if time_period == 1:
        table_output = tabulate(total_amt, 
                   headers = ["Year", "Average Yearly Debits", "Average Yearly Credits", "Average Yearly Total", "Average Yearly Spend"], 
                   tablefmt = "fancy_grid",
                   numalign = "center"
                   )
        
        print(table_output)
        
        print("The average total spend per year is the difference between the average debits and credits.\nThe figure is €{average_amt}".format(average_amt = round(total_amt[0][-1], 2)))
        print("The average debit per year is €{average_debits}".format(average_debits = round(total_amt[0][1], 2)))
        print("The average credit per year is €{average_credits}".format(average_credits = round(total_amt[0][2], 2)))
    
    # else monthly summary
    else:
        #each yearly average is divided by 12
        total_monthly = []
        for year in total_amt:
            year[1] /= 12
            year[2] /= 12
            year[3] /= 12
            year[4] /= 12
            total_monthly.append(year)
        table_output = tabulate(total_monthly, 
                   headers = ["Year", "Average Monthly Debits", "Average Monthly Credits", "Average Monthly Totals", "Average Monthly Spend"], 
                   tablefmt = "fancy_grid",
                   numalign = "center",
                   floatfmt=".2f"
                   )
        
        average_monthly_spend = total_monthly[0][-1]
        average_monthly_debits = total_amt[0][1]
        average_monthly_credits = total_amt[0][2]
        print(table_output)
        
        print("The average spend per month is €{average_amt}".format(average_amt = round(average_monthly_spend,2)))
        print("The average spend per month for debits is €{average_debits}".format(average_debits = round(average_monthly_debits,2)))
        print("The average spend per month for credits is €{average_credits}".format(average_credits = round(average_monthly_credits,2)))
    
    
    # a summary of the average spent for a specific, valid period
    optional_yearly_av = ask_y_n("Would you like to see the average spend for a specific period of time (y/n)?: ")
    
    if optional_yearly_av == "y":
        
        # asks for valid starting and ending years
        starting_year = 0
        while starting_year == 0:
            
            starting_year = ask_specific_year("Please enter the starting year: ")
            ending_year = ask_specific_year("Please enter the ending year: ")
            
            if starting_year > ending_year:
                print("The ending year cannot be smaller than the starting year.\n")
                continue
            
            else: 
                break
            
        # caluclates the total and average debits and credits over this period
        debited_amt = 0
        credited_amt = 0
        for bill in bills:
            if bill[2] in range(starting_year, ending_year + 1):
                if bill[6] == "debit":
                    debited_amt += bill[5]
                else:
                    credited_amt += bill[5]
        difference = debited_amt - credited_amt
        
        month_or_year = ask_1_or_2("Enter 1 to see the yearly average spend,\n"+
                                   "Enter 2 to see the monthly average spend.\nEnter:")
        
        # summarises the yearly average
        if month_or_year == 1:
            
            yearly_average = difference /((ending_year + 1) - starting_year)
            
            print("The yearly average spend over this period of time is €{spend}".format(spend = round(yearly_average, 2)))
        
        # summarises the monthly average
        else:
            months = ((ending_year + 1) - starting_year)*12
            
            monthly_average = difference/months
            print("The monthly average spend over this period of time is €{spend}".format(spend = round(monthly_average, 2)))
   
    else:
        pass
    
###############################################################################
#Question 9. Average Time between bills
###############################################################################


def average_time(bills):
    """ calculates the average time between bills, debits and credits. 
    No for loop is nested, the highest complexity of this function is O(n)"""
    
    sorted_list = sorted_bills(bills)
    
    # appends the date to each bill which allows the difference to be calculated
    for bill in sorted_list:
        bill.append(datetime(bill[2], bill[3], bill[4]))
    
    # collects lists for the dates of bills, debited bills and credited bills
    dates = []
    dates_debit = []
    dates_credit = []
    
    for bill in sorted_list:
        dates.append(bill[-1])
        if bill[6] == "debit":
            dates_debit.append(bill[-1])
        else:
            dates_credit.append(bill[-1])
    
    # removes the date once it has been used
    for bill in sorted_list:
        while len(bill) > 7:
            bill.pop()

    # uses list comprehension to create a list of the difference in days for each variable
    differences = [(dates[i]-dates[i-1]).days for i in range(1, len(dates))]
    difference_debit = [(dates_debit[i]-dates_debit[i-1]).days for i in range(1, len(dates_debit))]
    difference_credit = [(dates_credit[i]-dates_credit[i-1]).days for i in range(1, len(dates_credit))]
    
    # the differences are summed divided by the length to get the average
    average_days = float(sum(differences))/len(differences)
    average_days_debit = float(sum(difference_debit))/len(difference_debit)
    average_days_credit = float(sum(difference_credit))/len(difference_credit)
    
    # matrix of the average time and values for bills, debits and credits
    table_input = [["Average days between all Bills", average_days],
                   ["Average days between Debits", average_days_debit],
                   ["Average days between Credits", average_days_credit]]
    table_output = tabulate(table_input, 
                   headers = ["Average number of days between bills"], 
                   tablefmt = "fancy_grid",
                   numalign = "center",
                   floatfmt=".0f"
                   )
    print(table_output)
    print("The average time between bills is {days} days.\n".format(days = int(average_days)))
    
###############################################################################
#End of Questions
###############################################################################


def report_menu():
    """ create a sub menu, allowing user to choose from reports """
    
    bills = read_bills()
    
    option = get_report_option()
    
    # the option will continually be displayed until a valid option is given
    # option 8 will return to the main menu
    while option != "8": 
        
        if option == "1":
            yearly_report(bills)
            
        elif option == "2":
            popular_companies(bills)
            
        elif option == "3":
            report_date_order(bills)
            
        elif option == "4":
            ask_max(bills)
            
        elif option == "5":
            company_success(bills)
            
        elif option == "6":
            average_spend(bills)
            
        elif option == "7":
            average_time(bills)
            
        else:
            print("That is an invalid option")
    
        
        option = get_report_option()
    
    
    
def main():
    """ calls each function based on user input """
    
    # read all of the bills from the file system
    bills = read_bills()
    
    # display menu and ask for user choice
    choice = get_choice()
    
    # process the choice - 5 to exit
    while choice != '5':
        
        if choice == "1":
            view_bills(bills)
        
        elif choice == "2":
            add_new_bill(bills)
            
        elif choice == "3":
            report_menu()
            
        elif choice == "4":
            read_t_and_c()
            
        else:
            print('Invalid Option')

        # display menu and ask for user choice
        
            
        choice = get_choice()
        

    write_bills(bills)
    
    # print goodbye and exit
    print("\nThank you very much for your time!\nHave a lovely day:)")
    
if __name__ == '__main__':
    main()

