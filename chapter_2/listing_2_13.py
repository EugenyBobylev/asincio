"""
Защита задачи от снятия
"""
import asyncio
from timeit import timeit

from util.delay_functions import delay


async def main() -> None:
    long_task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(asyncio.shield(long_task), timeout=5)
        print(f'{result=}')
    except asyncio.exceptions.TimeoutError:
        print('Задача заняла более 5 с, скоро она закончится!')
        is_canceled = long_task.cancelled()
        print(f'Задача была снята? {is_canceled}')
        result = await long_task
        print(f'{result=}')


if __name__ == '__main__':
    exec_result = timeit(stmt='asyncio.run(main())', globals=globals(), number=1)
    print(f'Execution time is {exec_result} seconds')
