"""
There is a list of most active Stocks on Yahoo Finance https://finance.yahoo.com/most-active.
You need to compose several sheets based on data about companies from this list.
To fetch data from webpage you can use requests lib. To parse html you can use beautiful soup lib or lxml.
Sheets which are needed:
1. 5 stocks with most youngest CEOs and print sheet to output. You can find CEO info in Profile tab of concrete stock.
    Sheet's fields: Name, Code, Country, Employees, CEO Name, CEO Year Born.
2. 10 stocks with best 52-Week Change. 52-Week Change placed on Statistics tab.
    Sheet's fields: Name, Code, 52-Week Change, Total Cash
3. 10 largest holds of Blackrock Inc. You can find related info on the Holders tab.
    Blackrock Inc is an investment management corporation.
    Sheet's fields: Name, Code, Shares, Date Reported, % Out, Value.
    All fields except first two should be taken from Holders tab.


Example for the first sheet (you need to use same sheet format):
==================================== 5 stocks with most youngest CEOs ===================================
| Name        | Code | Country       | Employees | CEO Name                             | CEO Year Born |
---------------------------------------------------------------------------------------------------------
| Pfizer Inc. | PFE  | United States | 78500     | Dr. Albert Bourla D.V.M., DVM, Ph.D. | 1962          |
...

About sheet format:
- sheet title should be aligned to center
- all columns should be aligned to the left
- empty line after sheet

Write at least 2 tests on your choose.
Links:
    - requests docs: https://docs.python-requests.org/en/latest/
    - beautiful soup docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    - lxml docs: https://lxml.de/
"""

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl.styles import Alignment

# Define the URL for the Yahoo Finance page
url = 'https://finance.yahoo.com/most-active'

# Fetch the HTML content
response = requests.get(url)
html = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Extract data for the first sheet (youngest CEOs)
# Use BeautifulSoup and CSS selectors to navigate and extract data

# Create an Excel workbook
wb = Workbook()

# Create an Excel sheet for the first sheet
sheet1 = wb.active
sheet1.title = "5 Youngest CEOs"
sheet1['A1'] = "Name"
sheet1['B1'] = "Code"
sheet1['C1'] = "Country"
sheet1['D1'] = "Employees"
sheet1['E1'] = "CEO Name"
sheet1['F1'] = "CEO Year Born"

# Populate the sheet with data
# Loop through the extracted data and populate the cells

# Apply formatting
sheet1['A1'].alignment = Alignment(horizontal="left")
sheet1['B1'].alignment = Alignment(horizontal="left")
# Apply formatting for other columns as needed

# Create additional sheets, extract data, and populate them in a similar manner

# Save the Excel workbook
wb.save("yahoo_finance_data.xlsx")

