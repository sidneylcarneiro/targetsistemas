import json
import xml.etree.ElementTree as ET

# Função para carregar dados do arquivo JSON
def carregar_dados_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        return json.load(file)

# Função para carregar dados do arquivo XML
def carregar_dados_xml(caminho_arquivo):
    tree = ET.parse(caminho_arquivo)
    root = tree.getroot()

    dados = []
    for row in root.findall('row'):
        dia = int(row.find('dia').text)
        valor = float(row.find('valor').text)
        dados.append({"dia": dia, "valor": valor})

    return dados

# Carregar os dados do arquivo adequado
try:
    # Tente carregar do arquivo JSON
    faturamento = carregar_dados_json('faturamento.json')
except json.JSONDecodeError:
    # Se falhar, tente carregar do arquivo XML
    faturamento = carregar_dados_xml('faturamento.xml')

# Filtrar os dias com faturamento maior que 0
valores = [dia["valor"] for dia in faturamento if dia["valor"] > 0]

# Calcular o menor e maior faturamento
menor_faturamento = min(valores)
maior_faturamento = max(valores)

# Calcular a média mensal
media_mensal = sum(valores) / len(valores)

# Contar os dias com faturamento acima da média mensal
dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

# Exibir os resultados
print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media} dias")
