import time

def kron_mynt():
    import random
    kron = 0
    mynt = 0
    start_time = time.time()
    for x in range(100000):
        numba = random.randint(1, 2)
        if numba == 1:
            kron += 1
        elif numba == 2:
            mynt += 1
    end_time = time.time()
    elapsed_time = end_time - start_time
    print('kron =', kron, 'mynt =', mynt)
    print(elapsed_time)


def terningkast():
    import random
    en = 0
    to = 0
    tre = 0
    fire = 0
    fem = 0
    seks = 0
    start_time = time.time()
    for x in range(100000):
        numba = random.randint(1, 6)
        if numba == 1:
            en += 1
        elif numba == 2:
            to += 1
        elif numba == 3:
            tre += 1
        elif numba == 4:
            fire += 1
        elif numba == 5:
            fem += 1
        elif numba == 6:
            seks += 1
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'en = {en}, to = {to}, tre = {tre}, fire = {fire}, fem = {fem}, seks = {seks}')
    print(elapsed_time)

for x in range(50):
    kron_mynt()