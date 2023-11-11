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