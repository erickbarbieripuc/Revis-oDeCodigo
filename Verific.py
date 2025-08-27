def is_prime(n):
    """
    Verifica se um número é primo.
    
    Args:
        n (int): Número inteiro a ser verificado
    
    Returns:
        bool: True se o número for primo, False caso contrário
    """
    # Números menores ou iguais a 1 não são primos
    if n <= 1:
        return False
    
    # 2 e 3 são primos
    if n <= 3:
        return True
        
    # Números pares maiores que 2 não são primos
    if n % 2 == 0:
        return False
    
    # Verificar divisibilidade apenas por números ímpares até a raiz quadrada de n
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True


# Testes para verificar se a função está correta
print("is_prime(7) =", is_prime(7))    # Deve retornar True
print("is_prime(10) =", is_prime(10))  # Deve retornar False
print("is_prime(1) =", is_prime(1))    # Deve retornar False