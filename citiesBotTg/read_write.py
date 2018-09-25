import config
import pandas as pd


# from bs4 import BeautifulSoup as BS
# import requests


def read_html(url):
    df = pd.read_html(url)
    return df[0]


def write_table(df):
    # df = pd.DataFrame(df[0])
    # print(df)
    # print(df.columns)

    df.to_excel('Cities.xlsx', sheet_name='Cities', index=False, header=None, columns=[0, 2, 3, 4, 5, 6])  # header=None
    return None


def main():
    try:
        url = config.url_wiki

        df = read_html(url=url)
        write_table(df)
    except RuntimeError:
        pass


if __name__ == '__main__':
    main()

"""
def get_html(url):
    return requests.get(url).text


# print(get_html('https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%BE%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8'))

def parse(html):
    soup = BS(html, 'lxml')
    table = soup.select('body div#mw-content-text div.mw-parser-output table tbody tr')
    # print(table[2])
    i = 0
    while i < len(table):
        print(table[i].next.next.next.next.next.next.next.next.next.next)
        i += 1


parse(get_html(
    'https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%BE%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8'))
"""
