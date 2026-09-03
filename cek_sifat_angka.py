import math

def pemeriksa_prima(n):
    if n <= 1:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def pemeriksa_genap_ganjil(bilangan):
    if bilangan % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"
