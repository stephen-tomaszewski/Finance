import requests
import pickle
from bs4 import BeautifulSoup


def save_sp500_tickers():
    '''
    Pulls list of S&P 500 companies and ticker symbols from wikipedia.
    Arguements:
    Returns:
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

# TODO: replace . in source ticker file so don't have to convert it later on in the get_data function
        if ticker.find('.'):
            ticker = ticker.replace('.', '-')

        tickers.append(ticker)
    print(tickers)
    with open('sp500tickers.pickle', mode='wb') as f:
        pickle.dump(tickers, f)

# how to write to a text file instead of using pickle
    with open('sp500tickers.text', mode='w') as f:
        s = str(tickers)
        f.write(s)

    return tickers
