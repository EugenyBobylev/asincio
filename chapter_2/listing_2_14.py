"""
Основы будущих объектов
Мы не вызываем метод result, прежде чем результат установлен, потому что тогда он возбудил бы исключение InvalidState.
"""
from asyncio import Future


if __name__ == '__main__':
    my_future = Future()
    is_done = my_future.done()
    print(f'my_future готов? {is_done}')

    my_future.set_result(42)
    is_done = my_future.done()
    print(f'my_future готов? {is_done}')
    if is_done:
        result = my_future.result()
    print(f'Какой результат хранится в my_future? {result}')