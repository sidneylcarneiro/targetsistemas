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
