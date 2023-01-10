"""
Выполнение кода, пока другие операции работают в фоне
"""
import asyncio
from timeit import timeit

from util.delay_functions import delay


async def hello_every_second():
    for i in range(4):
        await asyncio.sleep(1)
        print("пока я жду, исполняется другой код!")


async def main() -> None:
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(5))

    await hello_every_second()
    await first_delay
    await second_delay


if __name__ == '__main__':
    result = timeit(stmt='asyncio.run(main())', globals=globals(), number=1)
    print(f'Execution time is {result} seconds')
