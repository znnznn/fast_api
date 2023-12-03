import json
from pprint import pprint

from aiohttp import FormData
from googleapiclient.discovery import build

# with open('logo-api-key.json', 'r') as file:
#     developerKey = json.load(file)

service = build("customsearch", "v1",
                developerKey="AIzaSyAxVvoaWEGJ29eWOn-EN7U4mBwFD6-b5Vw")

res = service.cse().list(
    q='футбол',
    cx='93c986e996090400f',
    searchType='image',
    # num=10,
    # start=21,
    imgType='clipart',
    fileType='png',
    safe='off',
    imgSize='HUGE',
    lr='lang_pl',
).execute()
if not 'items' in res:
    print('No result !!\nres is: {}'.format(res))
else:
    print(res['items'])
    for item in res['items']:
        pprint(item.items())
        pprint('{}:\n\t{}'.format(item['title'], item['link']))



def get_list_images(form_data: FormData):
    q = form_data['symbol']
    service = build("customsearch", "v1",
                    developerKey="AIzaSyAxVvoaWEGJ29eWOn-EN7U4mBwFD6-b5Vw")
    response = service.cse().list(
        q=form_data['symbol'],
        cx='93c986e996090400f',
        searchType='image',
        exactTerms=q,
        num=form_data.get('num', 10),
        imgType=form_data.get('type', 'clipart'),
        imgSize=str(form_data.get('period', 'clipart')).upper(),
        fileType='png',
        safe='off'
    ).execute()
    return response