def is_prime(n):
    if n <= 1:
        return False
    for i in range (2,n):
        if n % i == 0:
            return False
    return True 
print(is_prime(2))
print(is_prime(4))
print(is_prime(1))
print(is_prime(7))
print(is_prime(3))
print(is_prime(8))
print(is_prime(5))
print(is_prime(9))
print(is_prime(22))
print(is_prime(11))