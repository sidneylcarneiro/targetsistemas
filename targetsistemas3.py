import json

# Carregar os dados do JSON
with open('faturamento.json', 'r') as file:
    faturamento = json.load(file)

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
