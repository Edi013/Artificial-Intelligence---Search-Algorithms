import numpy as np

orase = np.array(
    ["Oradea", "Zerind", "Arad", "Timisoara", "Lugoj", "Mehadia", "Drobeta", "Craiova", "Ramnicu Valcea", "Sibiu",
     "Fagaras", "Pitesti", "Bucuresti", "Giurgiu", "Urziceni", "Hirsova", "Eforie", "Vaslui", "Iasi", "Neamt"])
'''
Oradea - 0 Zerind - 1 Arad - 2 Timisoara - 3 Lugoj - 4
Mehadia - 5 Drobeta - 6 Craiova - 7 Ramnicu Valcea - 8 
Sibiu - 9 Fagaras - 10 Pitesti - 11 Bucuresti - 12 Giurgiu - 13
Urziceni - 14 Hirsova - 15 Eforie - 16 Vaslui - 17
Iasi - 18 Neamt - 19
'''
# matrice_adiacenta
m = np.zeros([20, 20], int)

# oradea
m[0][1] = 1
m[0][9] = 1
# zerind
m[1][2] = 1
# arad
m[2][3] = 1
m[2][9] = 1
# timisoara
m[3][4] = 1
# lugoj
m[4][5] = 1
# mehadia
m[5][6] = 1
# drobeta
m[6][7] = 1
# craiova
m[7][8] = 1
m[7][11] = 1
# rm valcea
m[8][9] = 1
m[8][11] = 1
# pitesti
m[11, 12] = 1
# sibiu
m[9][10] = 1
# fagarasi
m[10][12] = 1
# bucuresti
m[12][13] = 1
m[12][14] = 1
# urziceni
m[14][15] = 1
m[14][17] = 1
# hirsova
m[15][16] = 1
# vaslui
m[17][18] = 1
# iasi
m[18][19] = 1

'''

#listare orase ca sa le ai in Run , sa lucrezi mai usor
n = 0
for i in orase:
    print(f"{i} - {n} |")
    n += 1
'''
# facem matricea simetrica
for i in range(20):
    for j in range(20):
        if m[i, j] == 1:
            m[j, i] = 1

for k in range(20):
    oras_cautat = k
    for i in range(20):
        if m[oras_cautat, i] == 1:
            print(f"Orasul {oras_cautat} legat de orasul {i} ")

''' # legam un string de un numar , trebuie si invers
city_numer={'Oradea' : 0, 'Zerind' : 1, 'Arad' : 2, 'Timisoara' : 3}
print(city_numer[0])
'''

plecare = 9
sosire = 14

viz = np.zeros([20], int)
noduri = np.array([plecare], int)

viz[plecare] = 1
gasit_sol = False
parinte = np.full([20],-1,int)

while not gasit_sol and len(noduri) > 0:
    nod = noduri[0]
    noduri = np.delete(noduri,0)
    if nod==sosire:
        gasit_sol = True
    else:
        for i in range(20):
            if m[nod,i] > 0 and viz[i] == 0:
                noduri = np.append(noduri,i)
                viz[i] = 1
                parinte[i] = nod
if gasit_sol:
    print("Drum gasit")
else:
    print("NU exista drum pasibil")

sol = []
curent = sosire

while curent != plecare:
    sol.append(curent)
    curent = parinte[curent]

sol.append(plecare)
sol=sol[::-1]

for i in sol:
    print(orase[i])
