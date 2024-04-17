import pandas as pd

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
#print(pnad.columns.values)

uf_siglas = {11:'RO', 12:'AC', 13:'AM', 14:'RR', 15:'PA', 16:'AP', 17:'TO', 21:'MA', 22:'PI', 23:'CE', 24:'RN', 25:'PB', 26:'PE', 27:'AL', 28:'SE', 29:'BA', 31:'MG', 32:'ES', 33:'RJ', 35:'SP', 41:'PR', 42:'SC', 43:'RS', 50:'MS', 51:'MT', 52:'GO', 53:'DF'}
sexo_cod = {0:'Masculino', 1:'Feminino'}
cor_codigo = {0:'Indígena', 2:'Branca', 4:'Preta', 6:'Amarela', 8:'Parda', 9:'Sem declaração'}
anos_estudo = {1:'Sem instrução ou menos de 1 ano', 2:'1 ano', 3:'2 anos', 4:'3 anos', 5:'4 anos', 6:'5 anos', 7:'6 anos', 8:'7 anos', 9:'8 anos', 10:'9 anos', 11:'10 anos', 12:'11 anos', 13:'12 anos', 14:'13 anos', 15:'14 anos', 16:'15 anos ou mais', 17:'Não determinados'}

uf = pnad['UF'].replace(uf_siglas)
sx = pnad['Sexo'].replace(sexo_cod)
id = pnad['Idade']
cr = pnad['Cor'].replace(cor_codigo)
ae = pnad['Anos de Estudo'].replace(anos_estudo)
rd = pnad['Renda']
at = pnad['Altura']

pnad_coluna = [uf, sx, id, cr, ae, rd, at]

print(' ')
print('==> Médias:')
print('    Idade: ' + str(round(id.mean(), 2)) + ' anos')
print('    Renda: R$ ' + str(round(rd.mean(), 2)))
print('    Altura: ' + str(round(at.mean(), 4)) + ' metros')

print(' ')
print('==> Modas:')
for coluna in range(0, len(pnad.columns.values)):
  print('    ' + pnad.columns.values[coluna] + ': ' + str(pnad_coluna[coluna].mode()[0]) + ', com ' + str(pnad_coluna[coluna].value_counts().max()) + ' indivíduos')

print

print(' ')
print('==> Medianas:')
print('    Idade: ' + str(round(id.median(), 4)) + ' anos')
print('    Renda: R$ ' + str(round(rd.median(), 4)))
print('    Altura: ' + str(round(at.median(), 4)) + ' metros')

print(' ')
print('==> Amplitudes:')
print('    Idade: ' + str(round(id.max()-id.min(),2)))
print('    Renda: ' + str(round(rd.max()-rd.min(),6)))
print('    Altura: ' + str(round(at.max()-at.min(), 4)))

print(' ')
print('==> Variâncias:')
print('    Idade: ' + str(round(id.var(), 2)) + ' anos²')
print('    Renda: R$² ' + str(round(rd.var(), 2)))
print('    Altura: ' + str(round(at.var(), 4)) + ' metros²')

print(' ')
print('==> Desvios padrão:')
print('    Idade: ' + str(round(id.std(), 2)) + ' anos')
print('    Renda: R$ ' + str(round(rd.std(), 2)))
print('    Altura: ' + str(round(at.std(), 4)) + ' metros')

print(' ')
print('==> Renda média')
renda_media = pnad['Renda'].groupby([uf, cr]).mean().round(2)
renda_cor = renda_media.unstack()
print(renda_cor)

abre_var('Renda média (por sexo)')
renda_media = pnad['Renda'].groupby([uf,sx]).mean().round(2)
renda_sexo = renda_media.unstack()
print(renda_sexo)

abre_var('Altura média por cor e por sexo')
altura_media = pnad['Altura'].groupby([cr, sx]).mean().round(4)
alturas = altura_media.unstack()
print(alturas)