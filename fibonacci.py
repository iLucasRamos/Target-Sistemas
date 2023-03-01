def verifica_fibonacci(num):
    a = 0
    b = 1
    while b <= num:
        if b == num:
            return True
        a, b = b, a+b
    return False


num = int(input("Digite um número: "))
if verifica_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
