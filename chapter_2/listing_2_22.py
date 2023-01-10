"""
Получение доступа к циклу событий
 В качестве примера рассмотрим метод call_soon, который планирует выполнение функции на следующей итерации цикла со-
 бытий.
"""
import asyncio

from util.delay_functions import delay


def call_later() -> None:
    print('I will be runned soon')


def call_later_too() -> None:
    print('Я буду вызван в ближайшем будущем')


async def main() -> None:
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    loop.call_soon(call_later_too)
    await delay(1)
    print('End of work')


if __name__ == '__main__':
    asyncio.run(main())
