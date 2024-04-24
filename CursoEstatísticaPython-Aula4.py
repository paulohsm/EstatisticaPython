# Aula realizada dia 12/04/2024
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#pnad_caminho = '/content/drive/MyDrive/Cursos/IFCE-EstatisticaPython/Pesquisa Nacional por Amostra de Domicílios.csv'
#pnad_caminho = '/home/santiago/Documentos/CursoEstatisticaPython/Pesquisa Nacional por Amostra de Domicílios.csv'
#pnad_caminho = '/home/santiago/Programming/CursoEstatisticaPython/Pesquisa Nacional por Amostra de Domicílios.csv'
pnad_caminho = 'Pesquisa Nacional por Amostra de Domicílios.csv'
pnad = pd.read_csv(pnad_caminho)

def abre_var(variavel):
  print(' ')
  print('==> ' + variavel + ':')

print('==> Variáveis PNAD:')
for coluna in pnad.columns.values:
  print('    ' + coluna)

uf_siglas = {11:'RO', 12:'AC', 13:'AM', 14:'RR', 15:'PA', 16:'AP', 17:'TO', 21:'MA', 22:'PI', 23:'CE', 24:'RN', 25:'PB', 26:'PE', 27:'AL', 28:'SE', 29:'BA', 31:'MG', 32:'ES', 33:'RJ', 35:'SP', 41:'PR', 42:'SC', 43:'RS', 50:'MS', 51:'MT', 52:'GO', 53:'DF'}
sexo_cod = {0:'Masculino', 1:'Feminino'}
cor_codigo = {0:'Indígena', 2:'Branca', 4:'Preta', 6:'Amarela', 8:'Parda', 9:'Sem declaração'}
anos_estudo = {1:'Sem instrução ou menos de 1 ano', 2:'1 ano', 3:'2 anos', 4:'3 anos', 5:'4 anos', 6:'5 anos', 7:'6 anos', 8:'7 anos', 9:'8 anos', 10:'9 anos', 11:'10 anos', 12:'11 anos', 13:'12 anos', 14:'13 anos', 15:'14 anos', 16:'15 anos ou mais', 17:'Não determinados'}

# substuicao de variaveis categoricas
pnad['UF'] = pnad['UF'].replace(uf_siglas)
pnad['Sexo'] = pnad['Sexo'].replace(sexo_cod)
pnad['Cor'] = pnad['Cor'].replace(cor_codigo)
pnad['Anos de Estudo'] = pnad['Anos de Estudo'].replace(anos_estudo)

#%% começando os trabalhos
print(' ')
print('==> Médias:')
print('    Idade: ' + str(round(pnad['Idade'].mean(), 2)) + ' anos')
print('    Renda: R$ ' + str(round(pnad['Renda'].mean(), 2)))
print('    Altura: ' + str(round(pnad['Altura'].mean(), 4)) + ' metros')

print(' ')
print('==> Modas:')
for coluna in pnad.columns.values:
  print('    ' + str(coluna) + ': ' + str(pnad[coluna].mode()[0]) + ', com ' + str(pnad[coluna].value_counts().max()) + ' individuos')

print(' ')
print('==> Medianas:')
print('    Idade: ' + str(round(pnad['Idade'].median(), 4)) + ' anos')
print('    Renda: R$ ' + str(round(pnad['Renda'].median(), 4)))
print('    Altura: ' + str(round(pnad['Altura'].median(), 4)) + ' metros')

print(' ')
print('==> Amplitudes:')
print('    Idade: ' + str(round(pnad['Idade'].max()-pnad['Idade'].min(),2)))
print('    Renda: ' + str(round(pnad['Renda'].max()-pnad['Renda'].min(),6)))
print('    Altura: ' + str(round(pnad['Altura'].max()-pnad['Altura'].min(), 4)))

print(' ')
print('==> Variâncias:')
print('    Idade: ' + str(round(pnad['Idade'].var(), 2)) + ' anos²')
print('    Renda: R$² ' + str(round(pnad['Renda'].var(), 2)))
print('    Altura: ' + str(round(pnad['Altura'].var(), 4)) + ' metros²')

print(' ')
print('==> Desvios padrão:')
print('    Idade: ' + str(round(pnad['Idade'].std(), 2)) + ' anos')
print('    Renda: R$ ' + str(round(pnad['Renda'].std(), 2)))
print('    Altura: ' + str(round(pnad['Altura'].std(), 4)) + ' metros')

print(' ')
print('==> Renda média')
renda_media = pnad['Renda'].groupby([pnad['UF'], pnad['Cor']]).mean().round(2)
renda_cor = renda_media.unstack()
print(renda_cor)

abre_var('Renda média (por sexo)')
renda_media = pnad['Renda'].groupby([pnad['UF'],pnad['Sexo']]).mean().round(2)
renda_sexo = renda_media.unstack()
print(renda_sexo)

#%% Gráficos
abre_var('Gráfico da renda média por cor e por sexo')
pnad_agrupado = pnad.groupby(['Cor', 'Sexo'])['Renda'].mean().unstack()
# Criando bar plots
bar_width = 0.4
x = np.arange(len(pnad_agrupado.axes[0]))
print(x)
plt.bar(x-0.2, pnad_agrupado['Feminino'], bar_width)
plt.bar(x+0.2, pnad_agrupado['Masculino'], bar_width)
plt.xticks(x, pnad_agrupado.axes[0].values)
plt.legend(['Mulheres', 'Homens'])
plt.title('Renda Média PNAD')
plt.xlabel('Cor')
plt.ylabel('Renda (R$)')
plt.show()

abre_var('Gráfico do espalhamento Altura vs Idade')
plt.scatter(pnad['Idade'], pnad['Altura'])
plt.show()