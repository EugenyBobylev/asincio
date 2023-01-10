"""
 Неправильное использование блокирующего API как сопрограммы
 библиотека requests блокирующая
"""
import asyncio

import requests as requests

from util.async_timer import async_timed
from util.delay_functions import delay


@async_timed()
async def get_example_status() -> int:
    return requests.get('http://www.example.com').status_code


@async_timed()
async def main() -> None:
    task_1 = asyncio.create_task(get_example_status())
    task_2 = asyncio.create_task(get_example_status())
    task_3 = asyncio.create_task(get_example_status())
    task_4 = asyncio.create_task(get_example_status())
    await task_1
    await task_2
    await task_3
    await task_4


if __name__ == '__main__':
    asyncio.run(main())
