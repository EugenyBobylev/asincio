"""
Задание тайм-аута для задачи с помощью wait_for
"""
import asyncio
from timeit import timeit

from util.delay_functions import delay


async def main() -> None:
    long_task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(long_task, timeout=5)
        print(f'{result=}')
    except asyncio.exceptions.TimeoutError:
        print('Тайм-аут!')
        is_canceled = long_task.cancelled()
        print(f'Задача была снята? {is_canceled}')


if __name__ == '__main__':
    exec_result = timeit(stmt='asyncio.run(main())', globals=globals(), number=1)
    print(f'Execution time is {exec_result} seconds')
