import requests  # Include HTTP Requests module
from urllib.request import urlopen  # import urlopen
import time  # import time module
import csv  # import csv module
import pandas as pd  # import pandas module
from bs4 import BeautifulSoup  # Include BS web scraping module

# initialize lists

header = []
tddata = []
csvrow1 = []
csvrow2 = []
csvrow3 = []
display1 = []
display2 = []
display3 = []
stockName = []
stockName1 = []
count = 0


# function to fetch the stock information from yahoo website using ticker symbol
def web_scrap(a, company, value):
    url = 'https://finance.yahoo.com/quote/' + a  # yahoo finance url
    stockName.clear()  # clear the list
    stockName1.clear()  # clear the list
    html = urlopen(url)  # open url
    soup = BeautifulSoup(html, "lxml")  # use beautifulsoup
    div = soup.find('div', {'id': 'quote-summary'})  # web scrape the content based on div
    div1 = div.find('div', {
        'class': 'D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)'})  # further web scrape the content based on inner div
    div2 = div.find('div', {
        'class': 'D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)'})  # further web scrape the content based on inner div
    rows = div1.find('table')  # web scrape the content based on table
    rows1 = div2.find('table')  # web scrape the content based on table
    for data in rows:
        for cell in data.findAll(['tr']):  # web scrape the content based on tr
            for cell1 in cell.findAll(['td']):  # web scrape the content based on td
                stockName.append(cell1.get_text())
    for data1 in rows1:
        for secondcell in data1.findAll(['tr']):  # web scrape the content based on tr
            for secondcell1 in secondcell.findAll(['td']):  # web scrape the content based on td
                stockName1.append(secondcell1.get_text())
    return [value, a, company, stockName[3], stockName[1], stockName[13], stockName1[1]]


# function to fetch the most archives from the money cnn
def most_activers():
    value = 'Most Actives'
    html = urlopen('https://money.cnn.com/data/hotstocks/')  # open url
    soup = BeautifulSoup(html, "lxml")  # use beautiful soup
    table = soup.findAll('table', {'class': 'wsod_dataTable wsod_dataTableBigAlt'})[
        0]  # web scrape the content based on 0th table
    rows = table.findAll('tr')  # web scrape the content based on tr
    for data in rows:
        for cell in data.findAll(['td'])[0:1]:  # web scrape the content based on td
            company = cell.get_text()
            display1.append(company)
            newcompany = company.split(' ', 1)[1]
            ticker = company.split()  # extract only the ticker
            csvrow1.append(web_scrap(ticker[0], newcompany, value))  # function call web_scrap
    df1 = pd.DataFrame(csvrow1)
    df1.to_csv('stocks.csv', header=False, index=False)  # content is appended to csv file


# function to fetch the gainers from the money cnn
def Gainers():
    value = 'Gainers'
    html = urlopen('https://money.cnn.com/data/hotstocks/')  # open url
    soup = BeautifulSoup(html, "lxml")  # use beautiful soup
    table = soup.findAll('table', {'class': 'wsod_dataTable wsod_dataTableBigAlt'})[
        1]  # web scrape the content based on 1st table
    rows = table.findAll('tr')  # web scrape the content based on tr
    for data in rows:
        for cell in data.findAll(['td'])[0:1]:  # web scrape the content based on td
            company = cell.get_text()
            display2.append(company)
            newcompany = company.split(' ', 1)[1]
            ticker = company.split()  # extract only the ticker
            csvrow2.append(web_scrap(ticker[0], newcompany, value))  # function call web_scrap
    df2 = pd.DataFrame(csvrow2)
    df2.to_csv('stocks.csv', mode='a', header=False, index=False)  # content is appended to csv file


# function to fetch the losers from the money cnn
def Losers():
    value = 'Losers'
    html = urlopen('https://money.cnn.com/data/hotstocks/')  # open url
    soup = BeautifulSoup(html, "lxml")  # use beautiful soup
    table = soup.findAll('table', {'class': 'wsod_dataTable wsod_dataTableBigAlt'})[
        2]  # web scrape the content based on 2nd table
    rows = table.findAll('tr')  # web scrape the content based on tr
    for data in rows:
        for cell in data.findAll(['td'])[0:1]:  # web scrape the content based on td
            company = cell.get_text()
            display3.append(company)
            newcompany = company.split(' ', 1)[1]
            ticker = company.split()  # extract only the ticker
            csvrow3.append(web_scrap(ticker[0], newcompany, value))  # function call web_scrap
    df2 = pd.DataFrame(csvrow3)
    df2.to_csv('stocks.csv', mode='a', header=False, index=False)  # content is appended to csv file


print("This is a program to scrape data from the https://money.cnn.com/data/hotstocks/ for a class project.")
print('Which stock are you interested in:\n')
most_activers()  # function call
Gainers()  # function call
Losers()  # function call
print('Most Actives:\n')
for i in display1:
    print(i)  # display most_activers
print('\n')
print('Gainers:\n')
for i in display2:  # display gainers
    print(i)
print('\n')
print('Losers:\n')
for i in display3:  # display losers
    print(i)
print('\n')

a = input('User inputs:')
with open('stocks.csv', 'rt') as csvFile:  # read csv file
    reader = csv.reader(csvFile)
    for row in reader:
        if a == row[1]:  # print the stck values
            print('The data for ' + row[1] + row[2] + ' is the following:\n')
            count = count + 1
            print(row[1], row[2])
            print('OPEN:', row[3])
            print('PREV CLOSE:', row[4])
            print('VOLUME:', row[5])
            print('MARKET CAP:', row[6])
            break
if count == 0:  # if the count is zero the entered input doesnt exist
    print('Entered User ticker doesnt exist!!!')

