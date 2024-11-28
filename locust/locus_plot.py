import pandas as pd
import matplotlib.pyplot as plt

# Leer el CSV
df = pd.read_csv('./locust/stats_stats.csv')

# Crear gráfico de latencias
plt.figure(figsize=(12, 6))

# Graficar diferentes percentiles de latencia
plt.plot(df['Average Response Time'], label='Promedio')
plt.plot(df['50%'], label='Mediana (P50)')
plt.plot(df['90%'], label='P90')
plt.plot(df['99%'], label='P99')

plt.xlabel('Muestras')
plt.ylabel('Latencia (ms)')
plt.title('Prueba de Carga - Distribución de Latencias')
plt.grid(True)
plt.legend()

# Agregar información adicional
plt.text(0.02, 0.98, 
         f'Total Requests: {df["Request Count"].sum()}\n'
         f'Errors: {df["Failure Count"].sum()}\n'
         f'Max Latency: {df["Max Response Time"].max():.2f}ms', 
         transform=plt.gca().transAxes,
         verticalalignment='top',
         bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()
plt.savefig('locust/latency_distribution.png')
plt.close()