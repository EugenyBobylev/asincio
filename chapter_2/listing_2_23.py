"""
Выполнение счетного кода в отладочном режиме
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
    loop = asyncio.get_running_loop()
    loop.slow_callback_duration = 0.5  # сообщение печатается, если сопрограмма работает дольше 500 мс.

    task_one = asyncio.create_task(cpu_bound_work())
    await task_one


if __name__ == '__main__':
    asyncio.run(main(), debug=True)
