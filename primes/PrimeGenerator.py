from time import time_ns

from primes.Fermat import fermat
from primes.MillerRabin import millerRabin
from pseudo_random.BlumBlumShub import generateRandomBlumBlumShub

primalityAlgorithms = [fermat, millerRabin]
sizes = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

with open('results.txt', 'a+') as file:  # Open the file in append mode
    for primalityAlgorithm in primalityAlgorithms:
            for size in sizes:
                numbers = []
                times = []
                for _ in range(100 if size < 2048 else 5):
                    randomNumber = 0
                    startTime = time_ns()
                    while True:
                        randomNumber = generateRandomBlumBlumShub(size)
                        if primalityAlgorithm(randomNumber):
                            numbers.append(randomNumber)
                            times.append((time_ns() - startTime)/1000)
                            break
                print(f"Algoritmo de geração: {generateRandomBlumBlumShub.__name__}")
                print(f"Algoritmo de primalidade: {primalityAlgorithm.__name__}")
                print(f"Tamanho do número: {size}")
                print(f"Tempo de geração em microsegundos: {sum(times)/len(times)}")
                print(f"Valor: {numbers[0]}")
                print()
                file.write(f"Algoritmo de geração: {generateRandomBlumBlumShub.__name__}\n")
                file.write(f"Algoritmo de primalidade: {primalityAlgorithm.__name__}\n")
                file.write(f"Tamanho do número: {size}\n")
                file.write(f"Tempo de geração em microsegundos: {(time_ns() - startTime) / 1000}\n")
                file.write(f"Valor: {randomNumber}\n\n")