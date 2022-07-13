import random as rn
cifre = [0,1,2,3,4,5,6,7,8,9]
n = len(cifre)
litere = ['T','R','E','I','D','O','C','N']
cv1 = "TREI"
cv2 = "DOI"
cv3 = "CINCI"
#litere = list(set(cv1 + cv2 + cv3))
print(litere)

def initializare():
    configuratie = rn.sample(cifre, k=n)  # rn.sample - le amesteca , din M ia n elemente si le amesteca
    return configuratie


def evaluare(config):
    nr1 = nr2 = nr3 = 0
    for i in range(len(cv1)):
        poz = litere.index(cv1[i]) # cautam indexul literei din cuvantul 1, pentru array ul de litere
        nr1 = nr1*10 + config[poz]
    for i in range(len(cv2)):
        poz = litere.index(cv2[i])
        nr2 = nr2*10 + config[poz]
    for i in range(len(cv3)):
        poz = litere.index(cv3[i])
        nr3 = nr3*10 + config[poz]
    diferenta = nr3 - nr2 - nr1
    if diferenta == 0:
        print(cv1, ' = ', nr1)
        print(cv2, ' = ', nr2)
        print(cv3, ' = ', nr3)
    return diferenta

def perturbare(config):
    x = rn.randrange(n)
    y = rn.randrange(n)
    while x == y :
        y = rn.randrange(n)
    config[x], config[y] = config[y], config[x]
    return config

def simulated_annealing():
    config = initializare()
    print(config)
    eval = evaluare(config)
    print(eval)
    k = 0
    for i in range(9999999):
        if k % 400 == 0:
            config = initializare()
        #print("Pasul " , i)
        #print(config)
        #print(eval)
        if eval == 0:
            print("FELICITARI")
            print(config)
            break
        k += 1
        cpy_cfg = [j for j in config]
        new_config = perturbare(cpy_cfg)
        eval1 = evaluare(new_config)
        if abs(eval1) < abs(eval):
            config = new_config
            eval = eval1
    print(eval)



simulated_annealing()



