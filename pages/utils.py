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