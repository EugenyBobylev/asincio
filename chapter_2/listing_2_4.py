"""
Использование await для ожидание результата сопрограммы
"""
import asyncio


async def add_one(number: int) -> int:
    return number + 1


async def main() -> None:
    one_plus_one = await add_one(1)
    two_plus_one = await add_one(2)
    three_plus_one = await add_one(two_plus_one)

    print(f'{one_plus_one=}')
    print(f'{two_plus_one=}')
    print(f'{three_plus_one=}')


if __name__ == '__main__':
    asyncio.run(main())
