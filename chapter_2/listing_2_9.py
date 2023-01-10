"""
Конкурентное выполнение нескольких задач
"""
import asyncio
from timeit import timeit

from util.delay_functions import delay


async def main() -> None:
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_more = asyncio.create_task(delay(3))
    print(f'type={type(sleep_for_three)}')  # выполнеяется сразу после запуска задачи

    await sleep_for_three
    await sleep_again
    await sleep_more


if __name__ == '__main__':
    result = timeit(stmt='asyncio.run(main())', globals=globals(), number=1)
    print(f'Execution time is {result} seconds')
    # asyncio.run(main())
