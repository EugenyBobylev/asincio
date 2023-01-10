async def corutine_add_one(number: int) -> int:
    return number + 1


def add_one(number: int) -> int:
    return number + 1


if __name__ == '__main__':
    function_result = add_one(1)
    corutine_result = corutine_add_one(1)

    print(f'funcion_result={function_result}, type={type(function_result)}')
    print(f'corutine_result={corutine_result}, type={type(corutine_result)}')
