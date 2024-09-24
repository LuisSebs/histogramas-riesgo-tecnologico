import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('transacciones.csv')

# Filtrar para obtener solo transacciones fraudulentas y nuevos usuarios
fraudulent_transactions = data[(data['status'] == 'fraudulent')]

# Formato para extraer solo la hora de la columna 'time'
fraudulent_transactions['hour'] = pd.to_datetime(fraudulent_transactions['time'], format='%H:%M').dt.hour

#Se define y se crea la gráfica
plt.figure(figsize=(12, 6))  # Ajusta el tamaño de la figura
sns.histplot(data=fraudulent_transactions, x='hour', weights='amount', bins=24, kde=True, color='red', label='fraudulent')

#Titulos
plt.title('Distribución del monto de transacciones fraudulentas por hora del día')
plt.xlabel('Hora del día')
plt.ylabel('Monto')
#cuadrícula en la gráfica 
plt.grid(True)  

#Mostramos la gráfica
plt.legend()
plt.show()