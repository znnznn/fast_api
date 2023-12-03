import json
from pprint import pprint

from aiohttp import FormData
from googleapiclient.discovery import build

from settings import GOOGLE_API_DEVELOPER_KEY, GOOGLE_API_CX


def get_list_images(form_data: FormData):
    q = form_data['symbol']
    service = build("customsearch", "v1", developerKey=GOOGLE_API_DEVELOPER_KEY)
    response = service.cse().list(
        q=form_data['symbol'],
        cx=GOOGLE_API_CX,
        searchType='image',
        exactTerms=q,
        num=form_data.get('num', 10),
        imgType=form_data.get('type', 'clipart'),
        imgSize=str(form_data.get('period', 'clipart')).upper(),
        fileType='png',
        safe='off'
    ).execute()
    return response