import pandas as pd

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

poluicao_tabela.insert(1, "Dia", Dias)
poluicao_tabela.insert(2, "Mes", Meses)
poluicao_tabela.insert(3, "DiaSemana", DiaSemana[0:120], True)
poluicao_tabela = poluicao_tabela.drop(columns=['Data'])

# Médias
print(poluicao_tabela[['CO', 'O3', 'temp', 'umid']].mean())
print(poluicao_tabela[['CO', 'O3', 'temp', 'umid']].groupby(poluicao_tabela['Mes'], sort=False).mean())
print(poluicao_tabela[['CO', 'O3', 'temp', 'umid']].groupby(poluicao_tabela['DiaSemana'], sort=False).mean())
#print(poluicao_tabela['CO'].groupby(poluicao_tabela['DiaSemana']).mean())

#print(poluicao_tabela[['CO', 'O3', 'temp', 'umid']].std())
