from fastapi import APIRouter, Depends
from pydantic import json

from database import User
from pages.utils import get_show_page_for_template
from tradier_api.tradier import download_all_stocks_symbols, get_stock_data, get_history_data_by_symbol
from users.mixins import current_user

router = APIRouter(
    prefix="/stocks",
    tags=["stocks"],
)


@router.get("/download-all-symbols")
async def download_possible_stocks():
    resp_data = await download_all_stocks_symbols()
    return resp_data


@router.get("/{symbol}")
async def get_stock_data_by_symbol(symbol: str):
    return await get_stock_data(symbol)


@router.get("/{symbol}/history")
async def get_stock_data_by_symbol(
        symbol: str, start_date: str, end_date: str, interval: str = 'daily', user: User = Depends(current_user)
):
    return await get_history_data_by_symbol(symbol, start_date, end_date, interval)


@router.get("/stocks")
async def get_stocks(page: int = 1, amount_stock: int = 10):
    page = page
    count_page = 3
    with open('stocks/stocks_all.json', 'r') as file_stocks:
        list_stocks = json.load(file_stocks)
        stocks = list_stocks['securities']['security']
        stocks = sorted(stocks, key=lambda symbol: symbol['symbol'])
        max_pos = len(stocks)
        pages = round(max_pos // amount_stock)
        pages = pages if max_pos % amount_stock == 0 else pages + 1
    if page < 1:
        page = 1
    elif page > pages:
        page = pages
    else:
        page = page

    start_pos = 0 if page == 1 else (page - 1) * amount_stock
    start_pos = start_pos if start_pos < max_pos else max_pos
    end_pos = start_pos + amount_stock
    end_pos = end_pos if end_pos < max_pos else max_pos
    qs_stocks = stocks[start_pos:end_pos]
    for stock in qs_stocks:
        data_symbol = await get_stock_data(stock['symbol'])
        if None is not data_symbol['quotes']['quote']['change_percentage'] >= 0:
            stock['positive_change'] = True
        else:
            stock['positive_change'] = False
        stock['quote'] = data_symbol['quotes']['quote']
    return {
        'results': qs_stocks,
        'show_page': await get_show_page_for_template(page, count_page, pages),
    }
