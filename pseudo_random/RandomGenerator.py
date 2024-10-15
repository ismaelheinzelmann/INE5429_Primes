from datetime import datetime
from time import time_ns

from pseudo_random.BlumBlumShub import generateRandomBlumBlumShub
from pseudo_random.XORShift import generateRandomXORSHIFT

sizes = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
sampleSize = 1000
algorithms = [generateRandomBlumBlumShub, generateRandomXORSHIFT]
for algorithm in algorithms:
    for size in sizes:
        randomNumbers = []
        times = []
        for _ in range(sampleSize):
            startTime = time_ns()
            pseudoRandom = algorithm(size)
            randomNumbers.append(pseudoRandom)
            times.append((time_ns() - startTime)/1000)
        print(f"Algoritmo de geração: {algorithm.__name__}")
        print(f"Tamanho do número: {size}")
        print(f"Tempo de geração em microsegundos: {sum(times) / len(times)}")
        print(f"Valor: {randomNumbers[0]}")
        print()