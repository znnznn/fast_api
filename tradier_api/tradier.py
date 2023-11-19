import datetime

import aiohttp
# import requests
import json
import time

from settings import TRADIER_TOKEN


#  url = 'https://sandbox.tradier.com/v1/markets/etb'   /beta/markets/fundamentals/corporate_actions


async def get_tradier_response(url: str = 'https://sandbox.tradier.com/v1/markets/etb', params=None) -> dict:
    headers = {"Accept": "application/json", "Authorization": f"Bearer {TRADIER_TOKEN}"}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url, params=params) as resp:
            print(resp.url)
            return await resp.json()


async def download_all_stocks_symbols() -> dict:
    url = 'https://sandbox.tradier.com/v1/markets/etb'
    resp_data = await get_tradier_response(url)
    if resp_data:
        with open('./tradier_api/stocks_all.json', 'w') as stocks:
            json.dump(resp_data, stocks, indent=4)
        return {"stocks": "downloaded"}
    return {"stocks": "not downloaded"}


async def get_stock_data(symbol: str) -> dict:
    url = f'https://sandbox.tradier.com/v1/markets/quotes?symbols={symbol}'
    return await get_tradier_response(url)


async def get_history_data_by_symbol(symbol: str, start_date: str, end_date: str, interval: str) -> dict:
    url = f'https://sandbox.tradier.com/v1/markets/history'
    possible_interval = ('daily', 'weekly', 'monthly')
    params = {'symbol': symbol, 'interval': interval, 'start': start_date, 'end': end_date}
    return await get_tradier_response(url, params)


async def get_list_of_stocks(page: int = 1, amount_stock: int = 10) -> dict:
    count_page = 3
    if amount_stock < 1:
        amount_stock = 10
    with open('tradier_api/stocks_all.json', 'r') as file_stocks:
        list_data = json.load(file_stocks)
        stocks = list_data['securities']['security']
        stocks = sorted(stocks, key=lambda symbol: symbol['symbol'])
        pages = round(len(stocks) // amount_stock)
        pages = pages if len(stocks) % amount_stock == 0 else pages + 1
    if page > pages:
        page = pages
    elif page < 1:
        page = 1
    show_page = {
        'prev_page': page - 1,
        'page_1': page,
        'page_2': page + 1,
        'page_3': page + 2,
        'next_page': page + count_page,
        'pages': pages
    }
    return {
        'stocks': stocks[page * amount_stock: (page + 1) * amount_stock],
        'page': show_page
    }


""" A	NYSE MKT
B	NASDAQ OMX BX
C.	Національна фондова біржа
D	FINRA ADF
Е	Незалежний від ринку (Створено Nasdaq SIP)
F	Взаємні фонди / грошові ринки (NASDAQ)
Я	Міжнародна біржа цінних паперів
J	Прямий край A
К	Direct Edge X
М	Чиказька фондова біржа
N	NYSE
P	NYSE Arca
Питання	NASDAQ OMX
S	NASDAQ Маленька кришка
Т	NASDAQ Int
U	OTCBB
V	Позабіржове інше
W	CBOE
X	NASDAQ OMX PSX
G	GLOBEX
Y	BATS Y-обмін
Z	ЛУПИЦИ
Потоки OPRA (опції)
A	Параметри NYSE Amex
B	Біржа опцій BOX
C.	Чиказька біржа опціонів (CBOE)
H	ISE Близнюки
Я	Міжнародна біржа цінних паперів (ISE)
М	Обмін опціонами MIAX
N	Параметри NYSE Arca
О	Орган, що звітує за опціонами (OPRA)
P	МІАКС ПЕРЛИНА
Питання	Ринок опціонів NASDAQ
Т	NASDAQ OMX BX
W	C2 Обмін опціями
X	NASDAQ OMX PHLX
Z	Ринок опціонів BATS

© Tradier Inc. Всі права захищені.

 """