import pandas as pd

#%% exercicios em sala de aula

# lista 2, exercício 9
efeito_dedet = pd.DataFrame({'Menos de 4 meses':[64, 104, 27], 
                             'De 4 a 8 meses':[120, 175, 48], 
                             'Mais de 8 meses':[16,21,5]}, 
                             index = ["A", "B", "C"])
#print(efeito_dedet)

#%% exercicios para casa
bac_caminho = "/home/santiago/Programando/EstatisticaPython/bacterias.xlsx"
bac = pd.read_excel(bac_caminho)
print(bac.columns.values)
print(round(bac['Hugger_Antes_Escovacao'].mean(), 3))
print(round(bac['Hugger_Depois_Escovacao'].mean(), 3))
print(round(bac['Convencional_Antes_Escovacao'].mean(), 3))
print(round(bac['Convencional_Depois_Escovacao'].mean(), 3))
print(len(bac['Hugger_Antes_Escovacao']))
print(bac['Hugger_Antes_Escovacao'].groupby(bac['Sexo']).count())