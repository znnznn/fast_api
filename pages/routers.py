from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from database import User
from pages.utils import AsyncIterator
from tradier_api.tradier import get_list_of_stocks, get_stock_data
from users.mixins import current_user

router = APIRouter(prefix="/pages", tags=["pages"])

templates = Jinja2Templates(directory="templates")


@router.get("/{page}")
async def main_page(request: Request, data: dict = Depends(get_list_of_stocks)):
    async for stock in AsyncIterator(data['stocks']):
        data_symbol = await get_stock_data(stock['symbol'])
        print(1)
        if not data_symbol['quotes']['quote']['open']:
            data_symbol['quotes']['quote']['open'] = 'Біржа закрита'
            data_symbol['quotes']['quote']['close'] = 'Біржа закрита'
        if not data_symbol['quotes']['quote']['ask']:
            data_symbol['quotes']['quote']['ask'] = 'Біржа закрита'
        if None is not data_symbol['quotes']['quote']['change_percentage'] >= 0:
            stock['positive_change'] = True
        else:
            stock['positive_change'] = False
        stock['quote'] = data_symbol['quotes']['quote']
    return templates.TemplateResponse("index.html", {"request": request, 'current_user': current_user, 'data': data})


@router.get("/{stock}")
async def schedule(stock: str):
    return await get_stock_data(stock)

@router.post("/user-list")
async def user_list():
    user = await get_list_of_stocks()
    return user
