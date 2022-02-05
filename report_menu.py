from tabulate import tabulate

def get_report_option():
    """ summarises options using tabulate and prompts user for input """
    
    report_options = [["Total Debits and Credits Per Year"],
                      ["The Most Popular Utility Company"],
                      ["Bills in Date Order"],
                      ["Highest Amount of Debits and Credits"],
                      ["The Success of the Company"],
                      ["Average Spent per Period of Time"],
                      ["Average Time between Bills"],
                      ["Return to Main Menu"]]
    
    report_output = tabulate(report_options, 
                   headers = ["Reports Menu"], 
                   tablefmt = "fancy_grid",
                   numalign = "center",
                   showindex= range(1, len(report_options)+1),
                   floatfmt=".2f"
                   )
    
    print(report_output)
    
    return input("Please choose a report: ")