# Aula realizada dia 19/04/2024

import pandas as pd

pnad_caminho = '/home/santiago/Programming/EstatisticaPython/Pesquisa Nacional por Amostra de Domicílios.csv'
pnad = pd.read_csv(pnad_caminho)

escorezrenda = (pnad['Renda'] - pnad['Renda'].mean()) / pnad['Renda'].std()
print(escorezrenda)

# Exercicios em aula (vide slide 21):
def escorez(valor, media, desvp):
    # z = ( x - xm ) / s
    return round((valor - media) / desvp, 2)

# exercício 1
h_media = 69.00
h_desvp = 2.80
h_mugsy = 63.00
h_oneal = 85.00
h_autor = 69.72

for alturas in [h_mugsy, h_oneal, h_autor]:
    print(escorez(alturas, h_media, h_desvp))

# exercicio 2
idade_media = 7.90
idade_desvp = 3.67
idade_corvette = 12.00
idade_ferrari = 2.00
idade_porsche = 0.00

for idade in [idade_corvette, idade_ferrari, idade_porsche]:
    print(escorez(idade, idade_media, idade_desvp))

# exercicio 3
# deixa pra depois

# exercício 5: idades atores e atrizes 
import seaborn as sns
idades_atores = [32, 37, 36, 32, 51, 53, 33, 61, 35, 45, 55, 39, 76, 37, 42, 40, 32, 60, 38, 56, 48, 48, 40, 43, 62, 43, 42, 44, 41, 56, 39, 46, 31, 47]
idades_atrizes = [50, 44, 35, 80, 26, 28, 41, 21, 61, 38, 49, 33, 74, 30, 33, 41, 31, 35, 41, 42, 37, 26, 34, 34, 35, 26, 61, 60, 34, 24, 30, 37, 31, 27]
sns.boxplot(idades_atores)