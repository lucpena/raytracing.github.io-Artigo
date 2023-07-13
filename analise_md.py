import matplotlib.pyplot as plt

# Lendo os dados do arquivo de texto
with open('analise_md.txt', 'r') as file:
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
plt.xlabel('Profundidade Máxima')
plt.ylabel('Tempo de renderização (segundos)')
plt.title('Profundidade Máxima - 5 SPP, 300 x 168')
plt.grid(True)

# Adicionando os valores ao lado das bolinhas
for i in range(len(samples)):
    plt.annotate(f'{times[i]}', (samples[i], times[i]), textcoords="offset points", xytext=(2, 7), ha='left', fontsize=12)

# Exibindo o gráfico
plt.show()
