from sqlalchemy import insert
from users.models import message
from users.schemas import ContactUs


class AsyncIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.index >= len(self.data):
            raise StopAsyncIteration
        value = self.data[self.index]
        self.index += 1
        return value


async def get_show_page_for_template(page: int, count_page: int, max_page: int):
    return {
        'prev_page': page - 1,
        'page_1': page,
        'page_2': page + 1,
        'page_3': page + 2,
        'next_page': page + count_page,
        'pages': max_page
    }


async def insert_message_to_db(new_message: ContactUs, session):
    stmt = insert(message).values(**new_message.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {"message": "inserted"}