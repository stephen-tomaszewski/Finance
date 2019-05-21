import requests
import pickle
from bs4 import BeautifulSoup


def Save500():
    '''
    Pulls list of S&P 500 companies and ticker symbols from wikipedia.
    Arguements:
    Returns:
    '''
    source = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = BeautifulSoup(source.text, 'lxml')

    tickers = []
    companies = []
    sectors = []
    table = soup.find('table', attrs={'class': 'wikitable sortable', 'id': 'constituents'})

    # iterates through rows in table skipping header
    for row in table.find_all('tr')[1:]:
        ticker = row.find_all('td')[0].text
        if ticker.find('.'):
            ticker = ticker.replace('.', '-').strip()
        company = row.find_all('td')[1].text
        sector = row.find_all('td')[3].text
        tickers.append(ticker)
        companies.append(company)
        sectors.append(sector)
        combined = list(zip(tickers, companies, sectors))

    with open('sp500tickers.pickle', mode='wb') as f:
        pickle.dump(tickers, f)
    with open('sp500companies.pickle', mode='wb') as f:
        pickle.dump(companies, f)
    with open('sp500sectors.pickle', mode='wb') as f:
        pickle.dump(sectors, f)

    return None
