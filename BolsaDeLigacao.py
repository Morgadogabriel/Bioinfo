import math

def lerArquivo(nomeArquivo):
    with open(nomeArquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    return linhas

def imprimeArquivo(linhas):
    for l in linhas:
        l = l.rstrip('\n')
    return l
def obtemCadeia(cadeia,linhas):
    atoms = {}
    for l in linhas:
        l = l.rstrip('\n')
        if l[0:4] == 'ATOM' and l[21] == cadeia:
            #COLUMNS        DATA  TYPE    FIELD        DEFINITION
            #-------------------------------------------------------------------------------------

            # 7 - 11        Integer       serial       Atom  serial number.
            serial = int(l[6:11])
            #18 - 20        Residue name  resName      Residue name.
            resName = l[17:20]
            #23 - 26        Integer       resSeq       Residue sequence number.
            resSeq = int(l[22:26])
            #31 - 38        Real(8.3)     x            Orthogonal coordinates for X in Angstroms.
            x = float(l[30:38])
            #39 - 46        Real(8.3)     y            Orthogonal coordinates for Y in Angstroms.
            y = float(l[38:46])
            #47 - 54        Real(8.3)     z            Orthogonal coordinates for Z in Angstroms.
            z = float(l[46:54])

            atoms[serial] = (x,y,z,resName,resSeq)
    return atoms

def obtemMolecula(id,linhas):
    atoms = {}
    for l in linhas:
        l = l.rstrip('\n')
        if l[0:6] == 'HETATM' and l[17:20] == id:
            serial = int(l[6:11])
            name = l[12:16].strip()
            x = float(l[30:38])
            y = float(l[38:46])
            z = float(l[46:54])

            atoms[serial] = (x,y,z,name)
    return atoms

def dist(x1,y1,z1,x2,y2,z2):
    d = math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
    return d

def obtemSitioLigacao(molecula,cadeia,limiar = 4):
    x=0
    y=1
    z=2
    resName = 3
    resSeq = 4
    name = 3
    sitio = []
    for m in molecula:
        for c in cadeia:
            d = dist(molecula[m][x], molecula [m][y], molecula[m][z], cadeia[c][x], cadeia[c][y], cadeia[c][z])
            if d <= limiar:
                #print(d, cadeia[c][resName], cadeia[c][resSeq], molecula[m][name])
                if not cadeia[c][resName] + str(cadeia[c][resSeq]) in sitio:
                    sitio.append(cadeia[c][resName]+str(cadeia[c][resSeq]))
    return sorted(sitio)

def gravarBolsa(arquivo, estrutura, aminoacidos):
    with open(arquivo, 'a') as file:
        file.write(f'{estrutura} {aminoacidos}\n')

#linhas = lerArquivo('Estruturas/c6_6v4c.pdb')
#imprimeArquivo(linhas)
#obtemCadeia("A", linhas)
#cadeia = obtemCadeia('A', linhas)
#molecula = obtemMolecula("LIG", linhas)
#print(obtemSitioLigacao(molecula,cadeia,4))

#gravarBolsa('Estruturas/AAdosPockets.txt', 'C6_6v4c', obtemSitioLigacao(molecula,cadeia,4))

def contarAminoacidos()