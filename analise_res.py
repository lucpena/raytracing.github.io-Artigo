import matplotlib.pyplot as plt

# Lendo os dados do arquivo de texto
with open('analise_res.txt', 'r') as file:
    lines = file.readlines()

resolutions = []
times = []

# Organizando os dados
for line in lines:
    width, height, time = line.split(',')
    resolutions.append(f"{width}x{height}")
    times.append(float(time))

# Plotando o gráfico de dispersão
plt.plot(resolutions, times, marker='o')
plt.xlabel('Resolução')
plt.ylabel('Tempo de renderização (segundos)')
plt.title('Resolução - 1SPP, 1 Profundidade')
plt.grid(True)

# Adicionando os valores ao lado das bolinhas
for i in range(len(resolutions)):
    plt.annotate(f'{times[i]}', (resolutions[i], times[i]), textcoords="offset points", xytext=(6,-10), ha='left', fontsize=12)


# Exibindo o gráfico
plt.show()
