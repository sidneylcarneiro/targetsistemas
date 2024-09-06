
```markdown
# Target Sistemas - Desafios em Python

Este repositório contém cinco scripts em Python que resolvem diferentes desafios de programação propostos. Além dos scripts, há também dois arquivos de dados (`faturamento.txt` e `faturamento.json`) utilizados por alguns dos desafios.

## Índice

1. [targetsistemas1.py](#targetsistemas1py)
2. [targetsistemas2.py](#targetsistemas2py)
3. [targetsistemas3.py](#targetsistemas3py)
4. [targetsistemas4.py](#targetsistemas4py)
5. [targetsistemas5.py](#targetsistemas5py)
6. [faturamento.txt](#faturamentotxt)
7. [faturamento.json](#faturamentojson)

## targetsistemas1.py

Este script calcula a soma dos números inteiros de 1 a 13. A variável `INDICE` é definida como 13, e o loop soma cada valor de 1 até `INDICE`.

**Execução:**
```bash
python targetsistemas1.py
```

**Saída esperada:**
```
91
```

## targetsistemas2.py

Este script contém duas funções principais:
- `fibonacci(n)`: Gera uma sequência de Fibonacci até um número `n` especificado.
- `pertence_a_fibonacci(n)`: Verifica se um número `n` pertence à sequência de Fibonacci.

**Execução:**
```bash
python targetsistemas2.py
```

**Entrada esperada:**
```
Informe um número: 21
```

**Saída esperada:**
```
O número 21 pertence à sequência de Fibonacci.
```

## targetsistemas3.py

Este script lê os dados de faturamento diário de um arquivo JSON e realiza as seguintes operações:
- Calcula o menor e maior valor de faturamento.
- Calcula a média mensal de faturamento.
- Conta quantos dias tiveram faturamento acima da média mensal.

**Execução:**
```bash
python targetsistemas3.py
```

**Saída esperada:**
```
Menor valor de faturamento: R$22174.17
Maior valor de faturamento: R$42889.23
Dias com faturamento acima da média: 5 dias
```

## targetsistemas4.py

Este script lê um arquivo de texto com os valores de faturamento por estado e calcula o percentual que cada estado representa do total.

**Execução:**
```bash
python targetsistemas4.py
```

**Saída esperada:**
```
SP: 37.53%
RJ: 20.29%
MG: 16.18%
ES: 15.05%
Outros: 10.96%
```

## targetsistemas5.py

Este script inverte uma string fornecida pelo usuário.

**Execução:**
```bash
python targetsistemas5.py
```

**Entrada esperada:**
```
Digite um texto aqui: Target Sistemas
```

**Saída esperada:**
```
String Original: Target Sistemas
String Invertida: sametsiS tegraT
```

## faturamento.txt

Contém os valores de faturamento por estado. Este arquivo é utilizado no script `targetsistemas4.py`.

**Formato:**
```
SP 67836.43
RJ 36678.66
MG 29229.88
ES 27165.48
Outros 19849.53
```

## faturamento.json

Contém os valores de faturamento diário. Este arquivo é utilizado no script `targetsistemas3.py`.

**Formato:**
```json
[
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.6612},
    {"dia": 7, "valor": 0.0},
    {"dia": 8, "valor": 42889.2258}
]
```

## Licença

Este projeto é licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
```

