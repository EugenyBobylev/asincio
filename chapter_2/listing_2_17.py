"""
Хронометраж двух конкурентных задач с помощью декоратора
"""
from asyncio import Future
import asyncio
from timeit import timeit

from util.async_timer import async_timed
from util.delay_functions import delay


@async_timed()
async def delay(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds


async def main() -> None:
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))
    await task_one
    await task_two


if __name__ == '__main__':
    asyncio.run(main())
    # exec_result = timeit(stmt='asyncio.run(main())', globals=globals(), number=1)
    # print(f'Execution time is {exec_result} seconds')
