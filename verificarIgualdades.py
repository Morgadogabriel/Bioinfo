C1_6v4c = ['ARG26', 'GLU12', 'GLY9', 'LYS13', 'TRP8']
C2_6v4c = ['ARG26', 'GLN16', 'GLY9', 'LYS13', 'SER23']
C3_6v4c = ['GLU2', 'GLU5', 'GLU6', 'LYS10', 'LYS13']
C4_6v4c = ['ARG26', 'GLU12', 'GLU5', 'GLU6', 'GLY9', 'LYS13', 'TRP8']
C5_6v4c = ['ARG26', 'GLN16', 'GLU12', 'GLU5', 'GLY9', 'LYS13', 'SER23']
C6_6v4c = ['GLU2', 'GLU5', 'GLU6', 'GLY9', 'LYS10', 'LYS13']

tot = []
for itens1 in C1_6v4c:
    tot.append(itens1)
for itens2 in C2_6v4c:
    if itens2 not in tot:
        tot.append(itens2)
for itens3 in C3_6v4c:
    if itens3 not in tot:
        tot.append(itens3)
for itens4 in C4_6v4c:
    if itens4 not in tot:
        tot.append(itens4)
for itens5 in C5_6v4c:
    if itens5 not in tot:
        tot.append(itens5)
for itens6 in C6_6v4c:
    if itens6 not in tot:
        tot.append(itens6)

print(tot)
with open('Estruturas/Pockets6v4c.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write(f'Os aminoácidos da clusterização que interagem com o ligante de 6v4c nas diversas poses\n{tot}\n\n')
    for a in tot:
        for c in C1_6v4c:
            if a == c:
                arquivo.write(f'{a}, C1\n')
        for b in C2_6v4c:
            if a == b:
                arquivo.write(f'{a}, C2\n')
        for g in C3_6v4c:
            if a == g:
                arquivo.write(f'{a}, C3\n')
        for d in C4_6v4c:
            if a == d:
                arquivo.write(f'{a}, C4\n')
        for e in C5_6v4c:
            if a == e:
                arquivo.write(f'{a}, C5\n')
        for f in C6_6v4c:
            if a == f:
                arquivo.write(f'{a}, C6\n')
        arquivo.write('----------------------------------------------------\n')