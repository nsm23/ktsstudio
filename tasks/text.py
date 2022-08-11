import re
from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    short_word = None
    long_word = None
    tmp_text = re.split('[\\s+,.]', text.strip())

    for i in tmp_text:
        if not i:
            continue

        if not short_word:
            short_word = i
        elif len(i) < len(short_word):
            short_word = i

        if not long_word:
            long_word = i
        elif len(i) > len(long_word):
            long_word = i

    return short_word, long_word
