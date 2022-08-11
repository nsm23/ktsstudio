__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    even_sum = 0
    try:
        odd_sum = 0
        for i in arr:
            if i % 2 == 0:
                even_sum += i
            else:
                odd_sum += i
        return even_sum / odd_sum
    except ZeroDivisionError:
        return 0
