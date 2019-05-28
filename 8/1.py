# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.

import hashlib


def get_q_substrings(string):
    result = []
    string_hash = hashlib.sha1(string.encode('utf-8')).hexdigest()

    for pos in range(0, len(string)):
        for j in range(1, len(string) + 1):
            sub_string = string[pos:j]
            sub_string_hash = hashlib.sha1(sub_string.encode('utf-8')).hexdigest()
            if sub_string_hash not in result and sub_string != '' and sub_string_hash != string_hash:
                result.append(sub_string_hash)

    return len(result)


print(get_q_substrings('Отличная задача!'))
