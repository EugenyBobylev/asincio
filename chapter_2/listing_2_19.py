"""
 Счетный код и длительная задача
"""
import asyncio

from util.async_timer import async_timed
from util.delay_functions import delay


@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(100000000):
        counter = counter + 1
    return counter


@async_timed()
async def main() -> None:
    task_one = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(cpu_bound_work())
    delay_task = asyncio.create_task(delay(4))

    await delay_task
    await task_one
    await task_two


if __name__ == '__main__':
    asyncio.run(main())
