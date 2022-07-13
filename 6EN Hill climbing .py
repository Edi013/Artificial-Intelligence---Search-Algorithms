import random as rn

n = 8

def initializare():
    M = [i for i in range(1, n + 1)]
    configuratie = rn.sample(M, k=n)  # rn.sample - le amesteca , din M ia n elemente si le amesteca
    return configuratie


def evaluare(config):
    erori = 0               # 0 1 2 3 4 5 6 7  n = 8
    for i in range(n - 1):
        for j in range(i + 1, n):
            if abs(config[i] - config[j] == abs(i - j)):
                erori += 1
    return erori

def perturbare(config):
    x = rn.randrange(n)
    y = rn.randrange(n)
    while x == y :
        y = rn.randrange(n)
    config[x], config[y] = config[y], config[x]
    return config

def hill_climbing():
    configuratie = initializare()
    print(configuratie)
    print(evaluare(configuratie))
    for i in range(1000):
        eval = evaluare(configuratie)
        if eval == 0:
            break
        config_new= perturbare(configuratie)
        if(evaluare(config_new) < eval):
            configuratie = config_new
    print("pasi executati: " , i)
    print(configuratie)
    print(eval)

hill_climbing()