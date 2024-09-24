import pandas as pd
import matplotlib.pyplot as plt

# Método do Pandas para ler o arquivo txt
df = pd.read_table('alunos.txt', sep=';')

dados_2024 = df[df['Ano'] == 2024]

# Separando os alunos com e sem nota vermelha
alunos_com_nota_vermelha = dados_2024[dados_2024['Possui Nota Vermelha'] == 'Sim']
alunos_sem_nota_vermelha = dados_2024[dados_2024['Possui Nota Vermelha'] == 'Não']

# Contador
contador_notas = {
    'Possuem Nota Vermelha': len(alunos_com_nota_vermelha),
    'Não Possuem Nota Vermelha': len(alunos_sem_nota_vermelha)
}

#Maneira encontrada para definir as cores vermelhas e verdes no gráfico.
cores = ['red', 'green']

labels = [
    f"Possuem Nota Vermelha: {'\n '.join(alunos_com_nota_vermelha['Nome'])}" if contador_notas['Possuem Nota Vermelha'] > 0 else "Possuem Nota Vermelha: Ninguém",
    f"Não Possuem Nota Vermelha: {'\n '.join(alunos_sem_nota_vermelha['Nome'])}" if contador_notas['Não Possuem Nota Vermelha'] > 0 else "Não Possuem Nota Vermelha: Ninguém"
]

# Criando um gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(contador_notas.values(), labels=labels, colors=cores, autopct='%1.1f%%', startangle=90)
plt.title('Alunos da escolinha do Curió com notas vermelhas em 2024')
plt.axis('equal') 
plt.show()