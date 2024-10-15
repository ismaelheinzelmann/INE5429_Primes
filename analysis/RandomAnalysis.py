from datetime import datetime

from matplotlib import pyplot as plt

from pseudo_random.BlumBlumShub import generateRandomBlumBlumShub
from pseudo_random.XORShift import generateRandomXORSHIFT

sizes = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
sampleSize = 2000
algorithms = [generateRandomBlumBlumShub, generateRandomXORSHIFT]
for algorithm in algorithms:
    for size in sizes:
        randomNumbers = []
        times = []
        for _ in range(sampleSize):
            startTime = datetime.now()
            pseudoRandom = algorithm(size)
            randomNumbers.append(pseudoRandom)
            times.append((datetime.now() - startTime).microseconds)
        print(
            f'Tempo médio em microsegundos para geração de {sampleSize} números pseudoaleatórios de tamanho {size} com o algoritmo {algorithm.__name__}: {sum(times) / len(times)}')
        try:
            plt.figure(figsize=(8,6))
            plt.hist(randomNumbers, bins=30, color='skyblue', edgecolor='black')
            plt.title(f'Histograma de {sampleSize} Números Pseudo-Aleatórios de tamanho {size} bit')
            plt.xlabel('Número Pseudo-Aleatório')
            plt.ylabel('Frequência')
            plt.grid(axis='y', alpha=0.75)
            plt.savefig(f'{algorithm.__name__}_{size}_histogram.png')
            plt.close()

            plt.figure(figsize=(8,6))
            plt.scatter(range(sampleSize), randomNumbers, color='purple', alpha=0.5)
            plt.title(f'Gráfico de Dispersão geração de {sampleSize} Números Pseudo-Aleatórios de tamanho {size} bit')
            plt.xlabel('Índice')
            plt.ylabel('Número Aleatório')
            plt.grid(axis='y', alpha=0.75)
            plt.savefig(f'{algorithm.__name__}_{size}_scatter.png')
            plt.close()
        except Exception as e:
            continue

