import pandas as pd
from  datetime import date
import matplotlib.pyplot as plt

poluicao_caminho = "/home/santiago/Programando/EstatisticaPython/Poluicao-Sao-Paulo.xlsx"
poluicao_tabela = pd.read_excel(poluicao_caminho)
# Variaveis e suas unidades
# CO = monoxido de carbono (ppm)
# O3 = ozonio (ppm)
# temp = temperatura (°C)
# umid = umidade relativa (%)

# Campos para calculos com datas (meses e dias da semana)
Meses = poluicao_tabela['Data'].str.split(",", expand=True)[0]
Dias = poluicao_tabela['Data'].str.split(",", expand=True)[1]
DiaSemana = ["ter", "qua", "qui", "sex", "sab", "dom", "seg"] * 18
MesesDic = {'Jan':1, 'Fev':2, 'Mar':3, 'Abr':4, 'Mai':5, 'Jun':6, 'Jul':7, 'Ago':8, 'Set':9, 'Out':10, 'Nov':11, 'Dez':12}
MesesInt = (pd.Series(Meses)).map(MesesDic)
print(MesesInt)

Datas = []
for i in range(len(Meses)):
    Datas.append(date(1991, int(MesesInt.to_list()[i]), int(Dias.to_list()[i])).strftime("%m-%d"))

poluicao_tabela.insert(1, "Dia", Dias)
poluicao_tabela.insert(2, "Mes", Meses)
poluicao_tabela.insert(3, "DiaSemana", DiaSemana[0:120], True)
poluicao_tabela = poluicao_tabela.drop(columns=['Data'])

# Graficos de series temporais das variaveis
seriest = plt.figure(figsize=(15,9))
gs = seriest.add_gridspec(4, hspace=0)
eixos = gs.subplots(sharex=True)
seriest.suptitle('Variáveis base')
eixos[0].plot(Datas, poluicao_tabela['CO'])
eixos[0].set(ylabel='CO (ppm)')
eixos[0].annotate('a', xy=(0.005, 0.045), xycoords="axes fraction", bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
eixos[1].plot(Datas, poluicao_tabela['O3'])
eixos[1].set(ylabel='O3 (ppm)')
eixos[1].annotate('b', xy=(0.005, 0.045), xycoords="axes fraction", bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
eixos[2].plot(Datas, poluicao_tabela['temp'])
eixos[2].set(ylabel='Temp. (°C)')
eixos[2].annotate('c', xy=(0.005, 0.045), xycoords="axes fraction", bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
eixos[3].plot(Datas, poluicao_tabela['umid'])
eixos[3].set(ylabel='Umid. Rel. (%)')
eixos[3].annotate('d', xy=(0.005, 0.045), xycoords="axes fraction", bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
eixos[3].set_xticks(Datas[::10])
eixos[3].set_xlabel('Ano: 1991')
plt.tight_layout()
plt.savefig('seriest-painel.png')
plt.show()

# Médias
print(poluicao_tabela[['CO', 'O3', 'temp', 'umid']].mean())
print(poluicao_tabela[['CO', 'O3', 'temp', 'umid']].groupby(poluicao_tabela['Mes'], sort=False).mean())
print(poluicao_tabela[['CO', 'O3', 'temp', 'umid']].groupby(poluicao_tabela['DiaSemana'], sort=False).mean())
#print(poluicao_tabela['CO'].groupby(poluicao_tabela['DiaSemana']).mean())

#print(poluicao_tabela[['CO', 'O3', 'temp', 'umid']].std())
