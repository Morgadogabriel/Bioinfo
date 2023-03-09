def read_list_file(filename):
    variables = {}
    with open(filename, 'r') as f:
        lines = f.readlines()

    for line in lines:
        name, values = line.strip().split('=')
        values = eval(values)
        variables[name] = values

    return variables

variables = read_list_file('DockingsClusterizacao/DockingsDM2/D2_2pql.txt')
first_key = next(iter(variables))
names = first_key.split('_')
ligant = names[1]
ClusterizationDinamicInformation = names[0]
count = 0
tot = []
for i, keys in enumerate(variables):
    for i in variables[keys]:
        if i not in tot:
            tot.append(i)
    count += 1
separador = '|'
with open(f'PocketsD2{ligant}test.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write(f'Os aminoácidos da clusterização que interagem com o ligante de {ligant} nas diversas poses\n{tot}\n\n')
    arquivo.write('Aminoácido | Cluster\n')
    for a in tot:
        for keys, values in variables.items():
            if a in values:
                arquivo.write(f'{a.ljust(10)}{separador.center(3)}{keys.rjust(10)}\n')
