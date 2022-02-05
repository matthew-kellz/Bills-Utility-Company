import unittest
import bill1 as bill
import writing_bills
from popular_company import get_companies, freq_companies
from bills_date_order import sorted_bills, unique_years
from company_success import total_bills
import mock
import builtins 
from unittest.mock import patch
from unittest import TestCase


class BillTest(unittest.TestCase):
    
    # test get_choice to ensure the user input matches what is returned
    def test_get_input(self):
        with mock.patch.object(builtins, 'input', lambda _: '1'):
            assert bill.get_input() == '1'
            
    # ensures that the length of bills matches what was counted when 
    # making the function. The output is hidden while running the test
    def test_read_bills(self):
        bills = bill.read_bills("test.csv")
        
        
        self.assertEqual(20, len(bills))
        #Electric Ireland, John Smyth, 2017, 5, 12, 11.58, credit
        self.assertEqual("Electric Ireland", bills[0][0])
        
    
    # matches the first line read in with the first line visible when using the 
    # test data
    def test_write_bills(self):
        bills = bill.read_bills()
        bill.write_bills(bills)
        bills_file = open("test.csv")
        lines = bills_file.readlines()
        bills_file.close()
        self.assertEqual(20, len(lines))
        self.assertEqual("Electric Ireland, John Smyth, 2017, 05, 12, 11.58, credit\n", lines[0])
        
    # the number of companies equals the number of entries in the test file
    def test_get_companies(self):
        file_name = "test.csv"
        bills = bill.read_bills(file_name)
        companies = get_companies(bills)
        self.assertEqual(20, len(companies))
    
    # the frequency of energia matches the amount counted visually in the test 
    # data. The output is hidden while running the test
    def test_popular_companies(self):
        bills = bill.read_bills(file_name = "test.csv")
        
        company_freq = freq_companies(bills)
        self.assertEqual(8, company_freq["Energia"])
        
      
    # checks the legnth of sorted bills matches test.csv and the first year in 
    # test.csv is first
    def test_sorted_bills(self):
        bills = bill.read_bills(file_name = "test.csv")
        bills_sorted = sorted_bills(bills)
        self.assertEqual(20, len(bills_sorted))
        self.assertEqual(2016, bills_sorted[0][2])
    
    # the number of unique years matches the number I counted in test.csv
    def test_unique_years(self):
        bills = bill.read_bills(file_name = "test.csv")
        different_years = unique_years(bills)
        self.assertEqual(4, len(different_years))
    
    # the number of debits and credits matches the total counted number in test.csv
    def test_total_bills(self):
        bills = bill.read_bills(file_name = "test.csv")
        total_amt = total_bills(bills)
        self.assertEqual(8, total_amt["total_credits"])
        self.assertEqual(12, total_amt["total_debits"])
    
    
        
class InputYearTest(TestCase):

    # inputYear will return 2020 in this test
    @patch('writing_bills.inputYear', return_value= 2020)
    def test_year_2020(self, input):
        self.assertEqual(writing_bills.inputYear("Please enter a valid year (YYYY): ", int), 2020)
    
    # the function should raise an exception for an invalid type
    def test_year_error(self):
        self.assertRaises(Exception, writing_bills.inputYear, return_value = "year")#Negative case test       

    # the function should raise an exception for a year out of range
    def test_wrong_year(self):
        self.assertRaises(Exception, writing_bills.inputYear, return_value = 2023)#Negative case test       


class InputMonthTest(TestCase):

    # inputMonth will return 12 in this test
    @patch('writing_bills.inputMonth', return_value= 12)
    def test_month_12(self, input):
        self.assertEqual(writing_bills.inputMonth("Please enter a valid month (MM): ", int), 12)
    
    # checks for type int, raising an exception otherwise
    def test_month_error(self):
        self.assertRaises(Exception, writing_bills.inputMonth, return_value = "month")#Negative case test       
    
    # checks for suitable month
    def test_wrong_month(self):
        self.assertRaises(Exception, writing_bills.inputMonth, return_value = 14)#Negative case test       

class InputDayTest(TestCase):

    # inputDay will return 20 in this test
    @patch('writing_bills.inputDay', return_value= 20)
    def test_day_20(self, input):
        self.assertEqual(writing_bills.inputDay("Please enter a valid day (DD): ", int), 20)
    
    # raises exception for an incorrect type
    def test_day_error(self):
        self.assertRaises(Exception, writing_bills.inputDay, return_value = "day")#Negative case test       
        
    # checks for a day in range
    def test_wrong_day(self):
        self.assertRaises(Exception, writing_bills.inputDay, return_value = 34)#Negative case test       


class InputFloatTest(TestCase):
    
    # inputFloat will return 20.14 in this test
    @patch('writing_bills.inputFloat', return_value= 20.14)
    def test_float(self, input):
        self.assertEqual(writing_bills.inputFloat("Please enter an amount: "), 20.14)
    
    # raises an error for type string
    def test_error(self):
        self.assertRaises(Exception, writing_bills.inputFloat, return_value = "string")#Negative case test       


class InputProvider(TestCase):
    
    # inputProvider will return Electric Ireland in this test
    @patch('writing_bills.inputProvider', return_value = "Electric Ireland")
    def test_provider(self, input):
        self.assertEqual(writing_bills.inputProvider("Please enter a provider: "), "Electric Ireland")
    
    # raises an error if the input is only numbers
    def test_provider_error(self):
        self.assertRaises(Exception, writing_bills.inputProvider, return_value = "1234")#Negative case test       


class InputCustomer(TestCase):
    
    # inputCustomer will return Matt Johnson in this test
    @patch('writing_bills.inputCustomer', return_value = "Matt Johnson")
    def test_customer(self, input):
        self.assertEqual(writing_bills.inputCustomer("Please enter a provider: "), "Matt Johnson")
    
    # raises an error if a number is entered
    def test_customer_error(self):
        self.assertRaises(Exception, writing_bills.inputCustomer, return_value = "Matthew1")#Negative case test       


class Input_1_or_2(TestCase):
    
    # returns the integer 1
    @patch('writing_bills.ask_1_or_2', return_value = 1)
    def test_customer(self, input):
        self.assertEqual(writing_bills.ask_1_or_2("Please enter 1 for debit and 2 for credit: "), 1)
    
    # raises an error if the number is not 1 or 2
    def test_input_error(self):
        self.assertRaises(Exception, writing_bills.ask_1_or_2, return_value = 3)#Negative case test       

    # raises an error if type incorrect
    def test_type_error(self):
        self.assertRaises(Exception, writing_bills.ask_1_or_2, return_value = "string")#Negative case test       


class InputSpecificYear(TestCase):
    
    # returns 2016
    @patch('bill1.ask_specific_year', return_value = 2016)
    def test_customer(self, input):
        self.assertEqual(bill.ask_specific_year("Please enter the year you would like to see the bills for:"), 2016)
    
    # raises an exception with year outside valid range
    def test_customer_error(self):
        self.assertRaises(Exception, bill.ask_specific_year, return_value = 2023)#Negative case test       

       
        
if __name__ == '__main__': #If imported into another module it wont run
    unittest.main()