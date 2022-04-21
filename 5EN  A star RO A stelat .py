import numpy as np

orase = np.array(
    ["Arad", "Zerind", "Oradea", "Sibiu", "Timisoara", "Fagaras", "Rm. Valcea", "Lugoj", "Mehadia", "Drobeta",
     "Pitesti", "Craiova", "Bucuresti", "Giurgiu", "Urziceni", "Vaslui", "Iasi", "Neamt", "Hirsova", "Eforie"])
h = np.array([366, 374, 380, 253, 329, 176, 193, 244, 241, 242, 101, 160, 0, 77, 80, 199, 226, 234, 151, 161])
n = 20
a = np.zeros([n, n], int)
a[0][1] = 75
a[0][3] = 140
a[0][4] = 118
a[1][2] = 71
a[2][3] = 151
a[3][5] = 99
a[3][6] = 80
a[4][7] = 111
a[5][12] = 211
a[6][10] = 97
a[6][11] = 146
a[7][8] = 70
a[8][9] = 75
a[9][11] = 120
a[10][11] = 138
a[10][12] = 101
a[12][13] = 90
a[12][14] = 85
a[14][18] = 98
a[14][15] = 142
a[15][16] = 92
a[16][17] = 87
a[18][19] = 86
for i in range(n):
    for j in range(n):
        if a[i][j] != 0:
            a[j][i] = a[i][j]

# cautare A*
oras_plecare = 0
oras_destinatie = 12
viz = np.zeros([n], int)  # toate orasele sunt nevizitate - viz este 0 peste tot
noduri = np.array([oras_plecare], int)  # Adaugam in lista noduri orasul de plecare.
viz[oras_plecare] = 1  # Marcam orasul de plecare ca vizitat.
gasit = False  # solutia negasita inca
parinte = np.full([20], -1, int)
cost = np.full([20], -1, int)
cost[oras_plecare] = 0
while not gasit and len(noduri) > 0:
    print(orase[noduri])
    # print([i for i in zip(cost[noduri], h[noduri])])
    print(cost[noduri]+h[noduri])
    nod = noduri[0]  # stocam primul element din noduri in variabila nod
    noduri = np.delete(noduri, 0)  # Eliminam primul element din noduri
    if nod == oras_destinatie:  # orasul curent este destinatia
        gasit = True
    else:
        # Adaugam sortat dupa nr de km + distanta h in noduri orasele care sunt conectate de nod
        for i in range(n):
            if a[i][nod] != 0 and (viz[i] == 0 or (viz[i] == 1 and cost[i] > cost[nod] + a[i][nod])):
                viz[i] = 1  # Orasele adaugate sunt marcate ca vizitate
                cost[i] = cost[nod] + a[i][nod]  # calculeaza noul cost
                parinte[i] = nod  # Se retine pentru oricare din orasele adaugate nodul parinte ca fiind nod
                noduri = np.append(noduri, i)  # adaugam nodul la sfarsit in lista de noduri
                # sortam crescator lista de noduri in functie de cost + aproximarea 
		# distantei in linie dreapta pana la Bucuresti folosind programare functionala:
                noduri = [j[0] for j in sorted(zip(noduri, cost[noduri] + h[noduri]), key=lambda p: p[1])]

if gasit:
    print("Drumul gasit este:")
    solutie = []
    oras_curent = oras_destinatie
    while oras_curent != oras_plecare:
        solutie.append(oras_curent)
        oras_curent = parinte[oras_curent]
    solutie.append(oras_plecare)
    solutie = solutie[::-1]
    for i in solutie:
        print(orase[i], end=" - ")
    print(f"\nDistanta parcursa este: {cost[oras_destinatie]}")
else:
    print("Nu am gasit drum")
