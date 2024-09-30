import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
csv_file_path = 'transacciones.csv'
df = pd.read_csv(csv_file_path)

# Convertir la columna 'date' a un formato de fecha
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')

# Filtrar solo las transacciones fraudulentas de tipo 'transfer'
fraudulent_transfers = df[(df['transaction_type'] == 'transfer') & (df['status'] == 'fraudulent')]

# Extraer el mes de la columna 'date'
fraudulent_transfers['month'] = fraudulent_transfers['date'].dt.month

# Crear el histograma del monto perdido por mes para transacciones fraudulentas de tipo 'transfer'
plt.figure(figsize=(10, 6))
plt.hist(fraudulent_transfers['month'], weights=fraudulent_transfers['amount'], bins=12, color='red', alpha=0.7, edgecolor='black')

# Configurar etiquetas y títulos
plt.title('Monto perdido por mes en transacciones fraudulentas de tipo transfer')
plt.xlabel('Mes')
plt.ylabel('Monto perdido')
plt.grid(True)

# Mostrar el histograma
plt.show()
