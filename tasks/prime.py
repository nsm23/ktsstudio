__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    count = 0
    if number in (0, 1):
        return False
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    if count > 2:
        return False
    return True
