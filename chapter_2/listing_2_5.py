"""
Первое применение sleep
"""
import asyncio


async def hello_world_message() -> str:
    await asyncio.sleep(1)  # приостановить на 1 с.
    return 'Привет Бобылев'


async def main() -> None:
    message = await hello_world_message()

    print(f'{message=}')


if __name__ == '__main__':
    asyncio.run(main())
