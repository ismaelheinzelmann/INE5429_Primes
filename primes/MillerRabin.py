from random import randint

def millerRabin(n, k=20):
    # Primeiros primos
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Escrever n na forma d * 2^r + 1 com d ímpar (fatoração por potências de 2)
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # Testa o valor k vezes, quanto maior o valor maior a precisão
    # Cada execução possui um parâmetro a aleatório
    for _ in range(k):
        # Escolhe um valor aleatório entre 2 e n - 1 exclusivo [2, n − 2]
        a = randint(2, n - 2)

        # Calcula x = a^d % n
        x = pow(a, d, n)

        # A idéia é que se um n não primo e ímpar é definido, o valor n - 1 (ou -1 mod n) pode ser escrito por d * 2^r
        # Caso esta propriedade seja alcançada, o valor provavelmente é primo
        # Sendo assim, se inicialmente atingimos x = 1 mod n ou x = -1 mod n, não encontraremos evidência de composição
        # Nesta iteração
        if x == 1 or x == n - 1:
            continue

        # Verifica para todas as potências de 2 fatoradas inicialmente se x se torna n - 1

        for _ in range(r - 1):
            # A partir do valor anterior de x, calcula x² % n
            x = pow(x, 2, n)
            # x = -1 mod n
            if x == n - 1:
                return True
        return False

    # Nenhuma evidência de que n é um número composto, então provavelmente é primo
    return True