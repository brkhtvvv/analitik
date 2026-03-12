#1 задание
def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    mapping_st = {}
    mapping_ts = {}

    for cs, ct in zip(s, t):
        # проверка соответствия s -> t
        if cs in mapping_st and mapping_st[cs] != ct:
            return False
        mapping_st[cs] = ct

        # проверка соответствия t -> s (чтобы два разных символа s не заменялись одним t)
        if ct in mapping_ts and mapping_ts[ct] != cs:
            return False
        mapping_ts[ct] = cs

    return True

# Пример использования
s = 'paper'
t = 'title'
print(is_isomorphic(s, t))  # True