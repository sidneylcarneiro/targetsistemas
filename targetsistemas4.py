# Função para calcular o percentual de cada estado
def calcular_percentuais(faturamentos):
    total = sum(faturamentos.values())
    percentuais = {estado: (valor / total) * 100 for estado, valor in faturamentos.items()}
    return percentuais

# Função para ler os dados do arquivo TXT
def ler_faturamentos(arquivo):
    faturamentos = {}
    with open(arquivo, 'r') as file:
        for linha in file:
            estado, valor = linha.split()
            faturamentos[estado] = float(valor)
    return faturamentos

# Caminho do arquivo TXT
arquivo = 'faturamento.txt'

# Ler os faturamentos do arquivo
faturamentos = ler_faturamentos(arquivo)

# Calcular os percentuais
percentuais = calcular_percentuais(faturamentos)

# Exibir os resultados
for estado, percentual in percentuais.items():
    print(f'{estado}: {percentual:.2f}%')

