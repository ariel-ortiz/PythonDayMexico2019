# Combinaciones, permutaciones y otras diversiones
# © 2019 por Ariel Ortiz Ramírez


def ordena(c):
    return sorted(c, key=lambda x: (len(x), x))


def potencia(c):
    if not c:
        return [[]]
    s = potencia(c[1:])
    return s + [[c[0]] + x for x in s]


def combinaciones(c, n):
    return [x for x in potencia(c)
            if len(x) == n]


def inserta(x, c, n):
    return c[:n] + [x] + c[n:]


def omninserta(x, c):
    return [inserta(x, c, i)
            for i in range(len(c) + 1)]


def concatena(c):
    return sum(c, [])


def permuta(c):
    if not c:
        return [[]]
    return concatena(
            [omninserta(c[0], x)
             for x in permuta(c[1:])])


def permutaciones(c, n):
    return concatena(
            [permuta(x)
             for x in combinaciones(c, n)])
