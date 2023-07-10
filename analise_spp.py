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
plt.xlabel('Samples por pixel')
plt.ylabel('Tempo de renderização (segundos)')
plt.title('Desempenho do Ray Tracing')
plt.grid(True)

# Exibindo o gráfico
plt.show()
