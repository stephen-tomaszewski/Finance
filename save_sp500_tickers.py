import requests
import pickle
from bs4 import BeautifulSoup


def save_sp500_tickers():
    '''
    Pulls list of S&P 500 companies and ticker symbols.
    Returns: null
    '''
    source = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    # print(source.status_code)
    soup = BeautifulSoup(source.text, 'lxml')

    tickers = []
    companies = []
    table = soup.find('table', attrs={'class': 'wikitable sortable', 'id': 'constituents'})

    # skips the table header row
    for row in table.find_all('tr')[1:]:
        company = row.find_all('td')[0].text
        companies.append(company)
        ticker = row.find_all('td')[1].text
        tickers.append(ticker)
    #    print(company, ":", ticker)
    print(companies, tickers)

    with open('sp500tickers.pickle', mode='wb') as f:
        pickle.dump(tickers, f)

    return
