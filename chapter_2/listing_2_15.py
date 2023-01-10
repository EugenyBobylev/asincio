"""
Ожидание будущего объекта (Future)
"""
from asyncio import Future
import asyncio
from timeit import timeit

from util.delay_functions import delay


def make_request() -> Future:
    future = Future()
    asyncio.create_task(set_future_value(future))  # Создать задачу, которая асинхронно установит значение future
    return future


async def set_future_value(future) -> None:
    await delay(2)  # Ждать 2 с, прежде чем установить значение
    future.set_result(42)


async def main() -> None:
    future = make_request()
    is_done = future.done()
    print(f'Будущий объект готов? {is_done}')

    result = await future  # Приостановить main, пока значение future не установлено
    is_done = future.done()
    print(f'Будущий объект готов? {is_done}')
    if is_done:
        print(f'{result=}')


if __name__ == '__main__':
    exec_result = timeit(stmt='asyncio.run(main())', globals=globals(), number=1)
    print(f'Execution time is {exec_result} seconds')
