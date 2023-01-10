"""
Создание цикла событий вручную
"""
import asyncio

from util.delay_functions import delay


async def main() -> None:
    await delay(1)

if __name__ == '__main__':
    loop = asyncio.new_event_loop()

    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
