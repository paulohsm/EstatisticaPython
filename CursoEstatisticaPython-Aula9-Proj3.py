import pandas as pd
import numpy as np
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
plt.savefig('seriest-painel.eps')
plt.clf()
plt.close('all')

print('Médias')
print(poluicao_tabela[['CO', 'O3', 'temp', 'umid']].mean().round(3))
print(poluicao_tabela[['CO', 'O3', 'temp', 'umid']].groupby(poluicao_tabela['Mes'], sort=False).mean().round(3))
print(poluicao_tabela[['CO', 'O3', 'temp', 'umid']].groupby(poluicao_tabela['DiaSemana'], sort=False).mean().round(3))

print('Desvios padrão')
print(poluicao_tabela[['CO', 'O3', 'temp', 'umid']].std().round(3))
print(poluicao_tabela[['CO', 'O3', 'temp', 'umid']].groupby(poluicao_tabela['Mes'], sort=False).std().round(3))
print(poluicao_tabela[['CO', 'O3', 'temp', 'umid']].groupby(poluicao_tabela['DiaSemana'], sort=False).std().round(3))

# Graficos de medias - geral, mensal, ciclo semanal
titulos_mensal = ["Geral", "Janeiro", "Fevereiro", "Março", "Abril"]
co_media_mensal = np.append(poluicao_tabela['CO'].mean(), poluicao_tabela['CO'].groupby(poluicao_tabela['Mes'], sort=False).mean())
o3_media_mensal = np.append(poluicao_tabela['O3'].mean(), poluicao_tabela['O3'].groupby(poluicao_tabela['Mes'], sort=False).mean())
tp_media_mensal = np.append(poluicao_tabela['temp'].mean(), poluicao_tabela['temp'].groupby(poluicao_tabela['Mes'], sort=False).mean())
ur_media_mensal = np.append(poluicao_tabela['umid'].mean(), poluicao_tabela['umid'].groupby(poluicao_tabela['Mes'], sort=False).mean())
#print(co_media_mensal)

titulos_semanal = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
co_media_semanal = poluicao_tabela['CO'].groupby(poluicao_tabela['DiaSemana'], sort=False).mean()
o3_media_semanal = poluicao_tabela['O3'].groupby(poluicao_tabela['DiaSemana'], sort=False).mean()
tp_media_semanal = poluicao_tabela['temp'].groupby(poluicao_tabela['DiaSemana'], sort=False).mean()
ur_media_semanal = poluicao_tabela['umid'].groupby(poluicao_tabela['DiaSemana'], sort=False).mean()

#print(np.append(co_media_semanal, co_media_semanal)[5:12])

#medias = plt.figure(figsize=(9,15))
#gs = seriest.add_gridspec([4, 2], hspace=0)
#medias_co = plt.figure(figsize=(3,15))
#gs = medias_co.add_gridspec([1,2], vspace=0)
#eixos = gs.subplots(sharey=True)
#plt.bar(titulos_mensal, co_media_mensal)
#plt.show()

#plt.bar(titulos_semanal, np.append(co_media_semanal, co_media_semanal)[5:12])
#plt.show()

co_medias = plt.figure(figsize=(15,5))
co_gs = co_medias.add_gridspec(1,2, wspace=0)
co_eixos = co_gs.subplots(sharey=True)
co_eixos[0].bar(titulos_mensal, co_media_mensal)
co_eixos[1].bar(titulos_semanal, np.append(co_media_semanal, co_media_semanal)[5:12])
plt.suptitle('Concentração média de CO (ppm)')
plt.tight_layout()
plt.savefig('medias-co.eps')

o3_medias = plt.figure(figsize=(15,5))
o3_gs = o3_medias.add_gridspec(1,2, wspace=0)
o3_eixos = o3_gs.subplots(sharey=True)
o3_eixos[0].bar(titulos_mensal, o3_media_mensal)
o3_eixos[1].bar(titulos_semanal, np.append(o3_media_semanal, o3_media_semanal)[5:12])
plt.suptitle('Concentração média de O₃ (ppm)')
plt.tight_layout()
plt.savefig('medias-o3.eps')

tp_medias = plt.figure(figsize=(15,5))
tp_gs = tp_medias.add_gridspec(1,2, wspace=0)
tp_eixos = tp_gs.subplots(sharey=True)
tp_eixos[0].bar(titulos_mensal, tp_media_mensal)
tp_eixos[1].bar(titulos_semanal, np.append(tp_media_semanal, tp_media_semanal)[5:12])
plt.suptitle('Temperatura média (°C)')
plt.tight_layout()
plt.savefig('medias-tp.eps')

ur_medias = plt.figure(figsize=(15,5))
ur_gs = ur_medias.add_gridspec(1,2, wspace=0)
ur_eixos = ur_gs.subplots(sharey=True)
ur_eixos[0].bar(titulos_mensal, ur_media_mensal)
ur_eixos[1].bar(titulos_semanal, np.append(ur_media_semanal, ur_media_semanal)[5:12])
plt.suptitle('Umidade Relativa média (%)')
plt.tight_layout()
plt.savefig('medias-ur.eps')

plt.clf()
plt.close('all')


'''
fig, (axs1, axs2) = plt.subplots(1,2)
fig.set_size_inches(15, 4)
gs = fig.add_gridspec(1, 2, wspace=0)
(axs1, axs2) = gs.subplots(sharey=True)
axs1.bar(titulos_mensal, co_media_mensal)
axs2.bar(titulos_semanal, np.append(co_media_semanal, co_media_semanal)[5:12])
plt.suptitle('Concentração média de CO (ppm)')
plt.tight_layout()
plt.savefig('medias-co.png')
#plt.show()
'''


# Graficos de nuvem / dispersao-xy entre as variaveis
m, b = np.polyfit(poluicao_tabela['CO'], poluicao_tabela['O3'], 1)
plt.scatter(poluicao_tabela['CO'], poluicao_tabela['O3'])
plt.plot(poluicao_tabela['CO'], m*poluicao_tabela['CO']+b, color='red')
plt.title('Espalhamento O3(CO)')
plt.xlabel('CO (ppm)')
plt.ylabel('O3 (ppm)')
plt.text(9.5, 230, 'inclinação = ' + str(round(m,4)), fontsize=10, )
plt.tight_layout()
x0,x1 = plt.gca().get_xlim()
y0,y1 = plt.gca().get_ylim()
plt.gca().set_aspect((x1-x0)/(y1-y0))
plt.savefig('xy-co-o3.eps')
plt.clf()
plt.close('all')

m, b = np.polyfit(poluicao_tabela['O3'], poluicao_tabela['temp'], 1)
plt.scatter(poluicao_tabela['O3'], poluicao_tabela['temp'])
plt.plot(poluicao_tabela['O3'], m*poluicao_tabela['O3']+b, color='red')
plt.title('Espalhamento Temperatura(O3)')
plt.xlabel('O3 (ppm)')
plt.ylabel('Temperatura (°C)')
plt.text(0, 21, 'inclinação = ' + str(round(m,4)), fontsize=10, )
plt.tight_layout()
x0,x1 = plt.gca().get_xlim()
y0,y1 = plt.gca().get_ylim()
plt.gca().set_aspect((x1-x0)/(y1-y0))
plt.savefig('xy-o3-tp.eps')
plt.clf()
plt.close('all')

m, b = np.polyfit(poluicao_tabela['temp'], poluicao_tabela['umid'], 1)
plt.scatter(poluicao_tabela['temp'], poluicao_tabela['umid'])
plt.plot(poluicao_tabela['temp'], m*poluicao_tabela['temp']+b, color='red')
plt.title('Espalhamento Umidade Relativa(Temperatura)')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Umidade Relativa (%)')
plt.text(12, 99, 'inclinação = ' + str(round(m,4)), fontsize=10, )
plt.tight_layout()
x0,x1 = plt.gca().get_xlim()
y0,y1 = plt.gca().get_ylim()
plt.gca().set_aspect((x1-x0)/(y1-y0))
plt.savefig('xy-tp-ur.eps')
plt.clf()
plt.close('all')

m, b = np.polyfit(poluicao_tabela['umid'], poluicao_tabela['CO'], 1)
plt.scatter(poluicao_tabela['umid'], poluicao_tabela['CO'])
plt.plot(poluicao_tabela['umid'], m*poluicao_tabela['umid']+b, color='red')
plt.title('Espalhamento CO(Umidade Relativa)')
plt.xlabel('Umidade Relativa (%)')
plt.ylabel('CO (ppm)')
plt.text(48.5, 12.5, 'inclinação = ' + str(round(m,4)), fontsize=10, )
plt.tight_layout()
x0,x1 = plt.gca().get_xlim()
y0,y1 = plt.gca().get_ylim()
plt.gca().set_aspect((x1-x0)/(y1-y0))
plt.savefig('xy-ur-co.eps')
plt.clf()
plt.close('all')



