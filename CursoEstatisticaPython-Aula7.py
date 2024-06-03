# Aula 7 - Projeto 1

#Você é um cientista de dados altamente requisitado e foi contratado pela renomada Empresa Floricultura S/A para desenvolver um algoritmo de machine learning capaz de classificar diferentes espécies de flores com base em suas características. No entanto, há um desafio: a quantidade de dados disponíveis é limitada devido a restrições de hardware.
#O conjunto de dados fornecido pela empresa contém as seguintes variáveis:

#    Comprimento da sépala (sepal length)
#    Largura da sépala (sepal width)
#    Comprimento da pétala (petal length)
#    Largura da pétala (petal width)
#    Variável alvo (Target), que consiste nas seguintes classes de espécies de íris: Iris-setosa, Iris-versicolor, Iris-virginica.

#Cada uma dessas variáveis descreve características específicas das flores, como o tamanho das sépalas e pétalas, fundamentais para a classificação das espécies.
#No entanto, devido às limitações técnicas, a Empresa Floricultura S/A decidiu que é necessário eliminar uma das variáveis do conjunto de dados antes de implementar o algoritmo de machine learning. Sua tarefa é justificar qual variável deve ser removida e por quê.
#Você deve considerar cuidadosamente os seguintes pontos ao fazer sua recomendação:

#    Qual variável é menos relevante para distinguir entre as diferentes espécies de flores?
#    Qual variável possui alta correlação com outras variáveis no conjunto de dados?
#    Qual variável, se removida, teria o menor impacto na capacidade do algoritmo de classificar corretamente as flores?

#Com base nessas considerações, elabore uma explicação clara e fundamentada sobre qual variável você recomendaria eliminar e por que essa decisão é a mais apropriada para o problema em questão.

from ucimlrepo import fetch_ucirepo

iris = fetch_ucirepo(id=53)
x = iris.data.features
y = iris.data.targets

x['Target']=y
print(x.info())

