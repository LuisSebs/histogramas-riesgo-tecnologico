import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def histograma_ejemplo():
    """
    Histograma de la distribución del monto de transacciones fraudulentas por día
    """
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

def histograma_1():
    """
    Histograma del monto de las transacciones por hora del día 
    con estado fraudulento de nuevos usuarios (Cuanto dinero
    históricamente se ha perdido más en las 24 horas del día)
    """

    data = pd.read_csv('transacciones.csv')

    # Filtrar para obtener solo transacciones fraudulentas de nuevos usuarios
    fraudulent_transactions = data[
        (data['status'] == 'fraudulent') & 
        (data['new_user'] == True)
    ].copy()

    # Formato para extraer solo la hora del día
    fraudulent_transactions['hour'] = pd.to_datetime(fraudulent_transactions['time'], format='%H:%M').dt.hour

    # Definimos y creamos la gráfica
    plt.figure(figsize=(12,6)) # Ajusta el tamaño de la figura
    sns.histplot(data=fraudulent_transactions, x='hour', weights='amount', bins=24, kde=True, color='pink', label='fraudulent')

    # Titulos 
    plt.title("Distribución del monto de transacciones fraudulentas por hora del día de nuevos usuarios")
    plt.xlabel('Hora del día')
    plt.ylabel('Monto')
    # cuadrícula de la gráfica
    plt.grid(True)

    # Mostramos la gráfica
    plt.legend()
    plt.show()

def histograma_2():
    """
    Histograma de la distribución de nuevos usuarios con una transacción fraudulenta
    (Cuantos usuario nuevos tuvieron una transacción fraudulenta vs los usuarios que
    no son nuevos)
    """

    data = pd.read_csv('transacciones.csv')

    # Filtrar solo las transacciones fraudulentas de nuevos usuarios
    fraudulent_transactions = data[data['status'] == 'fraudulent']

    # Agrupar por 'new_user' y contar la cantidad de usuarios únicos ('user_id')
    user_distribution = fraudulent_transactions.groupby('new_user')['user_id'].nunique().reset_index()

    # Renombrarmos los valores True y False
    user_distribution['user_type'] = user_distribution['new_user'].replace({True: 'New User', False: 'Old User'})

    # Definimos y creamos la grafica
    plt.figure(figsize=(8, 6))
    sns.barplot(x='user_type', y='user_id', data=user_distribution, palette='Blues')

    # Titulos
    plt.title('Distribución de usuarios nuevos vs usuarios viejos con transacciones fraudulentas')
    plt.xlabel('Tipo de Usuario')
    plt.ylabel('Cantidad de Usuarios')

    # Mostramos la grafica    
    plt.show()

def histograma_3():

    """
    Histograma del tipo de transaccion y el estado de la transaccion fraudulenta
    (Cuantos estados de transacciones fraudulentas tuvieron las transacciones
    purchase y transfer)
    """

    data = pd.read_csv('transacciones.csv')

    # Filtrar solo por las transacciones fraudulentas
    fraudulent_transactions = data[(data['status'] == 'fraudulent')]

    # Contamos las transacciones fraudulentas por tipo de transaccion
    transaction_type_count = fraudulent_transactions['transaction_type'].value_counts().reset_index()
    # Nombramos las columnas
    transaction_type_count.columns = ['transaction_type', 'count']

    # Definimos y creamos la grafica
    plt.figure(figsize=(8, 6))
    sns.barplot(x='transaction_type', y='count', data=transaction_type_count, palette='Reds')

    # # Titulos
    plt.title('Distribucion del tipo de transacción de transacciones fraudulentas')    
    plt.xlabel('Tipo de transaccion')
    plt.ylabel('Cantidad de transacciones')

    # Mostramos la grafica
    plt.show()

# histograma_ejemplo()
histograma_1()
# histograma_2()
# histograma_3()



