def prime_to(n):
    primi = []
    numeri = list(range(2, n+1))
    while numeri:
        p = numeri[0]
        primi.append(p)
        numeri = [i for i in numeri if i % p != 0]
    return primi

def pr_fac_of(n):
    primes_to_n = prime_to(n)
    prime_factors = []
    for i in prime_to_n:
        if n%i == 0:
            prime_factors.append(i)
        else:
            pass
    return prime_factors
   
    
n = int(input("Numero da scomporre:"))
prime_to_n = prime_to(n)
prime_factors = pr_fac_of(n)
print("Primi minori di", n, ":", prime_to_n)
print("Fattori primi di", n, ":", prime_factors)
