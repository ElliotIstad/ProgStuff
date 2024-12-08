import time
start_time = time.time()
WritingFile = open("Primes.txt", "a")

def prime_numba_checka(testnumba):
    for x in range(1,testnumba):
        testresult = testnumba/x
        if testresult == int(testresult):
            if x>1:
                if x!=testnumba:
                    print(f"{testnumba} is not a prime")
                    break
        elif testnumba == x+1:
            print(f"{testnumba} is a certified prime")
            WritingFile.write(str(testnumba))
            WritingFile.write("\n")

# while True:
#     TeNumbre = int(input("Que es tu numbre? - "))
#     prime_numba_checka(TeNumbre)
#     YesOrNo = int(input("0 for no, 1 for yes: - "))
#     if YesOrNo == 0:
#         break
#     else:
#         print("")


# PotentialExplosion = int(input("max number of calculations - "))
# for x in range(PotentialExplosion):
#     prime_numba_checka(x)

#WritingFile.close()
#end_time = time.time()
#elapsed_time = end_time - start_time
#print(elapsed_time)

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    
    p = 2
    
    while p * p <= limit:
        
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        
        p += 1
    
    primes = [p for p in range(2, limit + 1) if is_prime[p]]
    
    return primes


primes_up_to_50 = sieve_of_eratosthenes(1000000)

file = open("SievePrimes.txt", "a")
file.write(str(primes_up_to_50))
file.close
print(primes_up_to_50)

end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)