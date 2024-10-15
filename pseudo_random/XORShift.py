from time import time_ns

def XORSHIFT(seed):
    mask = 0xFFFFFFFF
    # Formata a entrada de seed em 32 bits
    randomNumber = seed & mask

    # Realiza operações de deslocamento em cima da entrada
    randomNumber ^= (randomNumber << 13) & mask
    randomNumber ^= (randomNumber >> 7) & mask
    randomNumber ^= (randomNumber << 17) & mask

    # Retorna o valor aleatório em 32 bits
    return randomNumber & mask


def generateRandomXORSHIFT(nBits, seed=None):
    # Define uma máscara de tamanho nBits composta de FF....FF
    mask = (1 << nBits) - 1

    # Gera uma seed de tamanho máximo 2^32
    if seed is None:
        seed = time_ns() & 0xFFFFFFFF

    result = 0
    bitsCollected = 0

    # Enquanto o valor for menor que o tamanho desejado em bits
    while bitsCollected < nBits:
        # Realiza operação de bits
        randomValue = XORSHIFT(seed)  # Usa o seed diretamente
        newBits = randomValue & 0xFFFFFFFF

        # Concatena o valor novo
        result = (result << 32) | newBits
        bitsCollected += 32
        seed = randomValue  # Usa o novo valor aleatório como o seed para a próxima iteração

    # Retorna o valor formatado em nBits
    return result & mask