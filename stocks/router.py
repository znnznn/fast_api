from fastapi import APIRouter, Depends

from database import User
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

