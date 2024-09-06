# String previamente definida
string_original = input("Digite um texto aqui: ")

# Inicializa a string invertida como uma string vazia
string_invertida = ""

# Percorre a string original de trás para frente
for i in range(len(string_original) - 1, -1, -1):
    string_invertida += string_original[i]

print("String Original:", string_original)
print("String Invertida:", string_invertida)
