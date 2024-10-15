from time import time_ns
# BlumBlumShub is a random number generator with the formula
# x[n+1] = x[n]² mod m
# Onde m = pq | p e q são primos com o menor divisor comum possível
def generateRandomBlumBlumShub(nBits, seed=None):
    # Define a máscara de tamanho nBits com valor FF...FF
    mask = (1 << nBits) - 1
    # Módulo
    n = 5651 * 5653

    # Caso nenhuma seed tenha sido informada, gera uma seed mod n
    if seed is None:
        seed = time_ns() % n
    randomValue = (seed * seed) % n

    result = 0
    bitsCollected = 0
    # Enquanto o valor for menor que o desejado
    while bitsCollected < nBits:
        # Executa a operação x[n+1] = x[n]² mod m
        randomValue = (randomValue * randomValue) % n
        # Formata o valor em 32 bits
        newBits = randomValue & ((1 << 32) - 1)
        # Concatena o valor ao resultado anterior
        result = (result << 32) | newBits
        # Incrementa o tamanho do número
        bitsCollected += 32
    # Formata a saída no formato definido utilizando uma máscara
    return result & mask

