__all__ = (
    'seconds_to_str',
)

from time import strftime, gmtime


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    if seconds < 60:
        return strftime("%Ss", gmtime(seconds))
    if 60 <= seconds < 3600:
        return strftime("%Mm%Ss", gmtime(seconds))
    if 3600 <= seconds < 86400:
        return strftime("%Hh%Mm%Ss", gmtime(seconds))
    if seconds >= 86400:
        day = seconds // (60 * 60 * 24)
        time_now = strftime("%Hh%Mm%Ss", gmtime(seconds))
        return f'{day:02d}d{time_now}'
