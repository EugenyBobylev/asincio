"""
Выполнение двух сопрограмм
В данном случае код ведет себя как последовательный
"""
import asyncio

from util.delay_functions import delay


async def add_one(number: int) -> int:
    return number + 1


async def hello_world_message() -> str:
    await delay(1)  # приостановить на 1 с.
    return 'Привет Бобылев'


async def main() -> None:
    message = await hello_world_message()  # приостановить выполнениен до возврата из hello_world_message
    one_plus_one = await add_one(1)        # приостановить выполнениен до возврата из add_one

    print(f'{one_plus_one=}')
    print(f'{message=}')


if __name__ == '__main__':
    asyncio.run(main())
