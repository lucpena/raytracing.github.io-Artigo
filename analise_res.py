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
plt.title('Desempenho do Ray Tracing')
plt.grid(True)


# Exibindo o gráfico
plt.show()
