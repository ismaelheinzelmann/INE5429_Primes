from random import randint
def fermat(n, k=10):
    # Casos base
    if n <= 3:
        return n > 1

    # Pares não são primos
    if n % 2 == 0:
        return False

    # Testa k vezes se a^(n - 1) ≡ 1, caso não seja, falha o teste
    # Se n for primo, então para qualquer valor menor que n, a^(n-1) ≡ 1 deve ser verdade
    for _ in range(k):
        a = randint(2, n - 1)
        if pow(a, n - 1, n) != 1:
            # Achou um valor cujo a^(n-1) ≡ 1 é falso, portanto o valor não é primo
            return False
    # Todos os valores de a aleatórios passaram nos k testes, portanto o valor provavelmente é primo.
    return True
# while True:
#     if fermat(561): break
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
#           109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
#           233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
#           367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
#           499, 503, 509, 521, 523, 541]
# for prime in primes:
#     print(fermat(prime))


# falsosPrimos = [1105, 1729, 2465, 2821, 6601, 8911, 10585]
#
# for prime in falsosPrimos:
#     i = 0
#     while True:
#         i += 1
#         if fermat(prime, k=100):
#             print(f"{prime} is probably prime with {i} iterations")
#             break
