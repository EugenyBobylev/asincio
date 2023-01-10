import asyncio


async def delay(delay_seconds: int) -> int:
    """
    Повторно используемая сопрограмма delay
    """
    print(f'засыпаю на {delay_seconds} сек.')
    await asyncio.sleep(delay_seconds)
    print(f'Проснулся через {delay_seconds} сек.\n')
    return delay_seconds
