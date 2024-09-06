
```markdown
# Target Sistemas - Desafios em Python

Este repositório contém cinco scripts em Python que resolvem diferentes desafios de programação propostos. Além dos scripts, há também dois arquivos de dados (`faturamento.txt` e `faturamento.json`) utilizados por alguns dos desafios.

## Índice

1. [targetsistemas1.py](#targetsistemas1py)
2. [targetsistemas2.py](#targetsistemas2py)
3. [targetsistemas3.py](#targetsistemas3py)
4. [targetsistemas4.py](#targetsistemas4py)
5. [targetsistemas5.py](#targetsistemas5py)

## targetsistemas1.py

### Descrição

Este script realiza uma soma simples utilizando uma estrutura de repetição. A variável `SOMA` acumula a soma dos valores de 1 até o `INDICE` especificado.

### Código

```python
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA += K
    
print(SOMA)
```

### Saída Esperada

```
91
```

## targetsistemas2.py

### Descrição

Este script contém duas funções principais: uma que gera uma sequência de Fibonacci até um determinado número `n` e outra que verifica se um número pertence à sequência de Fibonacci.

### Código

```python
def fibonacci(n):
    sequencia = [0, 1]
    while sequencia[-1] < n:
        next_value = sequencia[-1] + sequencia[-2]
        sequencia.append(next_value)
    return sequencia

def pertence_a_fibonacci(n):
    sequencia = fibonacci(n)
    if n in sequencia:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

numero = int(input("Informe um número: "))
mensagem = pertence_a_fibonacci(numero)
print(mensagem)
```

### Exemplo de Uso

```
Informe um número: 8
O número 8 pertence à sequência de Fibonacci.
```

## targetsistemas3.py

### Descrição

Este script carrega dados de faturamento diário a partir de arquivos JSON ou XML, calcula o menor e maior valor de faturamento, e o número de dias em que o faturamento foi superior à média mensal.

### Código

```python
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
```

### Exemplo de Uso

O script lê os dados dos arquivos `faturamento.json` ou `faturamento.xml` e imprime os resultados:

```
Menor valor de faturamento: R$373.78
Maior valor de faturamento: R$48924.24
Dias com faturamento acima da média: 10 dias
```

### Arquivos de Dados

- `faturamento.json`: Contém os dados de faturamento diário em formato JSON.
- `faturamento.xml`: Contém os dados de faturamento diário em formato XML.

## targetsistemas4.py

### Descrição

Este script lê os dados de faturamento por estado a partir de um arquivo TXT e calcula o percentual de contribuição de cada estado em relação ao total.

### Código

```python
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
```

### Exemplo de Uso

O script lê os dados de `faturamento.txt` e exibe o percentual de cada estado:

```
SP: 37.53%
RJ: 20.29%
MG: 16.17%
ES: 15.03%
Outros: 11.00%
```

### Arquivo de Dados

- `faturamento.txt`: Contém os dados de faturamento por estado.

## targetsistemas5.py

### Descrição

Este script inverte uma string fornecida pelo usuário.

### Código

```python
# String previamente definida
string_original = input("Digite um texto aqui: ")

# Inicializa a string invertida como uma string vazia
string_invertida = ""

# Percorre a string original de trás para frente
for i in range(len(string_original) - 1, -1, -1):
    string_invertida += string_original[i]

print("String Original:", string_original)
print("String Invertida:", string_invertida)
```

### Exemplo de Uso

```
Digite um texto aqui: Python
String Original: Python
String Invertida: nohtyP
```
