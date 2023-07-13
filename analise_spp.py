import matplotlib.pyplot as plt

# Lendo os dados do arquivo de texto
with open('analise_spp.txt', 'r') as file:
    lines = file.readlines()

samples = []
times = []

# Organizando os dados
for line in lines:
    sample, time = line.split(',')
    samples.append(int(sample))
    times.append(float(time))

# Plotando o gráfico
plt.plot(samples, times, marker='o')
plt.xlabel('Amostras por Pixel (SPP)')
plt.ylabel('Tempo de renderização (segundos)')
plt.title('Amostras Por Pixel (SPP) - 50 de Profundidade, 640 x 360')
plt.grid(True)

# Adicionando os valores ao lado das bolinhas
for i in range(len(samples)):
    plt.annotate(f'{times[i]}', (samples[i], times[i]), textcoords="offset points", xytext=(6,-6), ha='left', fontsize=12)

# Exibindo o gráfico
plt.show()
