"""
Создание задачи
"""
import asyncio

from util.delay_functions import delay


async def main() -> None:
    sleep_for_three = asyncio.create_task(delay(3))
    print(f'type={type(sleep_for_three)}')  # выполнеяется сразу после запуска задачи

    result = await sleep_for_three
    print(f'{result=}')


if __name__ == '__main__':
    asyncio.run(main())
