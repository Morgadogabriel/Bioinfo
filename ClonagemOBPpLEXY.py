
'''class sequencia:
    def __init__(self, seq):
        width.self = len(seq)'''




#sequencia da proteina sem o n-terminal, portanto sem o ATG

obpSeq = '''CAAGAAGTGAATGAAGAATTATGGGGAAAAGCAGAAAAGAAATGCCAACAACTTTCCAAATTGAGTTCAATTGAAAGAGCATCAATTCTTACAAGTTTAGGGAACATATCTCGTACAGCTAAGTGTTATGTAAATTGTTNNNNTGAAGAAGTTGGATTGATGATTGGAGCAGCTGTAAATAGTACATTGTTGCATTCATGGTTGAAGGAAGAAGCTGAAATTTCAGAAAACAAAGAAGAATTATATAACAGAATTAAAACCTGTGTTGATGCAATTACAGTTGAAGATAAATGTGATAAAGCTTATGAACTGTATATTTGCTTCGAAAATAGATAG'''
def primersEnd(seq,ini = 20,end = 20):
    contGC = 0
    contAT = 0
    contATrev = 0
    contGCrev = 0

    AT = ['A','T']
    GC = ['G','C']

    for i in seq[0:ini].upper():
        if i in AT:
            contAT += 1
        if i in GC:
            contGC += 1

    print(f'A quantidade de AT é {contAT} || a quantidade de GC é {contGC} || O TM é {contGC * 4+ contAT*2} || % de GC é {contGC/ini}')

    primerFW = seq[0:ini]
    print(f'{primerFW}, {len(primerFW)} bases')

    revOBP = seq[::-1].upper()

    listComplementObp = []
    revComplementOBP = ''
    for c in revOBP.upper():
        if c == 'A':
            listComplementObp.append('T')
        if c == 'T':
            listComplementObp.append('A')
        if c == 'G':
            listComplementObp.append('C')
        if c == 'C':
            listComplementObp.append('G')

    revComplementOBP = revComplementOBP.join(listComplementObp)

    for c in revComplementOBP[0:end].upper():
        if c in AT:
            contATrev += 1
        if c in GC:
            contGCrev += 1

    print(f'A quantidade de AT é {contATrev} || a quantidade de GC é {contGCrev} || O TM é {contGCrev * 4+ contATrev*2} || % de GC é {contGCrev/end}')

    primerREV = revComplementOBP[0:end]
    print(f'{primerREV}, {len(primerREV)} bases')

def complement(seq):
    listComplementSeq = []
    for c in seq:
        if c == 'A':
            listComplementSeq.append('T')
        if c == 'T':
            listComplementSeq.append('A')
        if c == 'G':
            listComplementSeq.append('C')
        if c == 'C':
            listComplementSeq.append('G')
    return (''.join(listComplementSeq))

def contGC(seq):
    cont = 0
    contGC = 0
    GC = ['G','C']
    seq = seq.upper()
    for i in seq:
        cont += 1
        if i in GC:
            contGC += 1
        if contGC/cont >= 0.4:
            print(f'O primer de {cont} Bases tem {contGC/cont} de GC ')

def GC(seq):
    cont = 0
    contGC = 0
    GC = ['G', 'C']
    seq = seq.upper()
    for i in seq:
        cont += 1
        if i in GC:
            contGC += 1
    return contGC

def automaticPrimerDesigner(seq = '', comprimentoMinimo = 18,comprimentoMaximo = 28):
    seq = seq.upper().strip()
    complementSeq = complement(seq).upper()
    reverseComplementSeq = complementSeq[::-1].upper()

    ATGCN = ['A','T','G','C','N']

    #if not (seq in ATGCN):
        #print('Sua sequencia não está de acordo com o esperado para DNA')


    AT = ['A','T']
    GC = ['G','C']
    tmPrimerSenso = 0
    contadorGCPrimerSenso = 0
    contadorPrimerSenso = 0
    primerSenso = []
    primerReverso = []
    listaPrimersSenso = []
    for i in seq[:comprimentoMaximo].upper():
        primerSenso.append(i)
        if i in GC:
            tmPrimerSenso += 4
            contadorPrimerSenso += 1
            contadorGCPrimerSenso += 1
        elif i in AT:
            tmPrimerSenso += 2
            contadorPrimerSenso += 1
        else:
            print('tem uma base não identificada no primer SENSO')
        stringPrimerSenso = "".join(primerSenso)
        if contadorPrimerSenso>= comprimentoMinimo:
            listaPrimersSenso.append([contadorPrimerSenso, stringPrimerSenso, tmPrimerSenso])
            #print(f'primer Senso{contadorPrimerSenso} = {stringPrimerSenso}\nBases = {contadorPrimerSenso} TM = {tmPrimerSenso}')

    tempPrimerReverso = 0
    contadorGCPrimerReverso = 0
    contadorPrimerReverso = 0
    listaPrimersReversos = []
    for i in reverseComplementSeq[:comprimentoMaximo].upper():
        primerReverso.append(i)
        if i in GC:
            tempPrimerReverso += 4
            contadorPrimerReverso += 1
            contadorGCPrimerReverso += 1
        elif i in AT:
            tempPrimerReverso += 2
            contadorPrimerReverso += 1
        else:
            print('tem uma base não identificada no primer REVERSO')
        stringPrimerReverso = "".join(primerReverso)
        if contadorPrimerReverso >= comprimentoMinimo:
            listaPrimersReversos.append([contadorPrimerReverso,stringPrimerReverso, tempPrimerReverso])
            #print(f'primer REV{contadorPrimerReverso} = {stringPrimerReverso}\nBases = {contadorPrimerReverso}\nTM = {tempPrimerReverso} ')
    listaPrimersCompativeis = []
    for i in listaPrimersSenso:
        for n in listaPrimersReversos:
            if 70 >= i[2] >= 60  and i[1][-1] in GC and 70 >= n[2] >= 60  and n[1][-1] in GC:
                print(f'Primer FW ({len(i[1])} bases):{i[1]}, TM={i[2]} | Primer REV ({len(n[1])} bases) :{n[1]},TM={n[2]}')
                listaPrimersCompativeis.append([i[0],i[1],i[2],n[0],n[1],n[2]])
    return listaPrimersCompativeis

def where60(seq):
    seq = seq.upper()
    temp = 0
    GC = ['G','C']
    Cont = 0
    for i in seq:
        if temp > 65 and i in GC:
            break
        if i in GC:
            Cont += 1
            temp += 4
        else:
            Cont += 1
            temp += 2
    print(f'temperatura {temp},numero de bases {Cont}')
    return [temp, Cont]

def TM(primer):
    GC = ['G','C']
    AT = ['A','T']
    temp = 0
    primer = primer.upper().strip()
    for i in primer:
        if i in GC:
            temp += 4
        if i in AT:
            temp += 2
    print(temp)


'''def isIntegral(seq, includeN = True):
    seq = seq.upper().strip()
    elementosAceitos = ['A','T','C','G','N']
    elementosAceitosIntegros = ['A','C','T','G']
    counter = 0
    Ns = []
    if includeN == False:
        for i in seq:
            counter += 1
            Ns.append(i,counter)
            if not(i in elementosAceitos):
                print(f'Sua sequencia possui um elemento diferente de {elementosAceitos}, substitua {i} na posição  {Ns[counter][1]}')
    if includeN == True:
        for i in seq:
            if not (i in elementosAceitosIntegros):
                print(f'Sua sequencia possui um elemento diferente de {elementosAceitosIntegros}, substitua em {counter}')'''





seqOBPPepSinal = 'ATGTGTAAATTAGTGATTTTACTCACTGTTTTTGTTCTGCAGATGTATTTAATTTCTGCCCAAGAAGTGAATGAAGAATTATGGGGAAAAGCAGAAAAGAAATGCCAACAACTTTCCAAATTGAGTTCAATTGAAAGAGCATCAATTCTTACAAGTTTAGGGAACATATCTCGTACAGCTAAGTGTTATGTAAATTGTTNNNNTGAAGAAGTTGGATTGATGATTGGAGCAGCTGTAAATAGTACATTGTTGCATTCATGGTTGAAGGAAGAAGCTGAAATTTCAGAAAACAAAGAAGAATTATATAACAGAATTAAAACCTGTGTTGATGCAATTACAGTTGAAGATAAATGTGATAAAGCTTATGAACTGTATATTTGCTTCGAAAATAGATAG'
seqOBP = 'CAAGAAGTGAATGAAGAATTATGGGGAAAAGCAGAAAAGAAATGCCAACAACTTTCCAAATTGAGTTCAATTGAAAGAGCATCAATTCTTACAAGTTTAGGGAACATATCTCGTACAGCTAAGTGTTATGTAAATTGTTNNNNTGAAGAAGTTGGATTGATGATTGGAGCAGCTGTAAATAGTACATTGTTGCATTCATGGTTGAAGGAAGAAGCTGAAATTTCAGAAAACAAAGAAGAATTATATAACAGAATTAAAACCTGTGTTGATGCAATTACAGTTGAAGATAAATGTGATAAAGCTTATGAACTGTATATTTGCTTCGAAAATAGATAG'
seqOBPOtimizada = 'CAAGAGGTGAATGAAGAACTGTGGGGTAAAGCAGAGAAAAAATGTCAGCAGCTGAGCAAACTGAGCAGCATTGAACGTGCAAGCATTCTGACCAGCCTGGGTAATATCAGCCGTACCGCAAAATGTTATGTTAATTGTGCAACCGAAGAGGTGGGTCTGATGATTGGTGCAGCAGTTAATAGCACCCTGCTGCATAGCTGGCTGAAAGAAGAAGCAGAAATTAGCGAAAACAAAGAGGAACTGTACAACCGCATTAAAACCTGTGTTGATGCAATTACCGTGGAAGATAAATGCGATAAAGCCTACGAACTGTATATCTGCTTTGAAAACCGTTAA'
seqTrypsPepSinal = 'ATGAGAACAATATATAGCATAGCAATCGCTTTATTGCTTGGAAAAATTTGGGTAAATCCTCAAAGTTATGTTAACATAAAATCTGAAGAAATAGATTTAACTCAACAAGAACAAAAATATGGAGAAAAAGTAACAAATTGTTCTTGTGGCTGGACTAACAAGGCAAGAATTGTTGGTGGACGTGAAACCTTGAAAAATGAATTTCCATTAATGGCCGGAATTATAGATATGGAAAAGAAATTTTTATTCTGTGGTGCAACAATAGTAACCCAAAATCACGCAATAACAGCATCCCATTGTACCACACCAAATAAAAAAAAGAAATTAGGCCTAGTAGTTGGTGCTCATGATGTTACTAAACCTGATGAAAAGGCAGACGTTGTTGAAATTAAAGAAACAGTAGAACATGAAAATTATAGTTCTAAATCTTATCATAACGATGTTGCCTTGTTGGTTCTTTCAAGATCAATCAAGTTCACCCAAGAAGTTGGTCCAGCTTGTCTGCCTACTGGCAAAGCTGATTTGGTTAATGAATACATCAAAGTACTTGGTTGGGGAAGATTGAAAACTAAAGGAAAAACATCTTCAGTTCTGATGAAAGTTAATTTAAGGGTAATTTCAATTAAAGAGTGTGCTAAAAATTATTTAAAGAAAATACCAACTGATTCTCCAAACCAACTTTGTACTTATGGACATGAAAAGGATTCTTGTCAGGTCAGTATAATAGTTTTCTAA'
seqTrypsOtimizada = 'AAATATTCCGGATTATTCATACCGTCCCACCATCGGGCGCGGATCCATGAGAACAATATATAGCATAGCAATCGCTTTATTGCTTGGAAAAATTTGGGTAAATCCTCAAAGTTATGTTAACATAAAATCTGAAGAAATAGATTTAACTCAACAAGAACAAAAATATGGAGAAAAAGTAACAAATTGTTCTTGTGGCTGGACTAACAAGGCAAGAATTGTTGGTGGACGTGAAACCTTGAAAAATGAATTTCCATTAATGGCCGGAATTATAGATATGGAAAAGAAATTTTTATTCTGTGGTGCAACAATAGTAACCCAAAATCACGCAATAACAGCATCCCATTGTACCACACCAAATAAAAAAAAGAAATTAGGCCTAGTAGTTGGTGCTCATGATGTTACTAAACCTGATGAAAAGGCAGACGTTGTTGAAATTAAAGAAACAGTAGAACATGAAAATTATAGTTCTAAATCTTATCATAACGATGTTGCCTTGTTGGTTCTTTCAAGATCAATCAAGTTCACCCAAGAAGTTGGTCCAGCTTGTCTGCCTACTGGCAAAGCTGATTTGGTTAATGAATACATCAAAGTACTTGGTTGGGGAAGATTGAAAACTAAAGGAAAAACATCTTCAGTTCTGATGAAAGTTAATTTAAGGGTAATTTCAATTAAAGAGTGTGCTAAAAATTATTTAAAGAAAATACCAACTGATTCTCCAAACCAACTTTGTACTTATGGACATGAAAAGGATTCTTGTCAGGTCAGTATAATAGTTTTCCACCACCACCACCACCACCACCACGACTACAAAGACGATGACGACAAGTAAGGTACCAAGCTTGTCGAGAAGTACTAGAGGATCATAATCAGCCATA'
realTrypsin = 'ATGAGAACAATATATAGCATAGCAATCGCTTTATTGCTTGGAAAAATTTGGGTAAATCCTCAAAGTTATGTTAACATAAAATCTGAAGAAATAGATTTAACTCAACAAGAACAAAAATATGGAGAAAAAGTAACAAATTGTTCTTGTGGCTGGACTAACAAGGCAAGAATTGTTGGTGGACGTGAAACCTTGAAAAATGAATTTCCATTAATGGCCGGAATTATAGATATGGAAAAGAAATTTTTATTCTGTGGTGCAACAATAGTAACCCAAAATCACGCAATAACAGCATCCCATTGTACCACACCAAATAAAAAAAAGAAATTAGGCCTAGTAGTTGGTGCTCATGATGTTACTAAACCTGATGAAAAGGCAGACGTTGTTGAAATTAAAGAAACAGTAGAACATGAAAATTATAGTTCTAAATCTTATCATAACGATGTTGCCTTGTTGGTTCTTTCAAGATCAATCAAGTTCACCCAAGAAGTTGGTCCAGCTTGTCTGCCTACTGGCAAAGCTGATTTGGTTAATGAATACATCAAAGTACTTGGTTGGGGAAGATTGAAAACTAAAGGAAAAACATCTTCAGTTCTGATGAAAGTTAATTTAAGGGTAATTTCAATTAAAGAGTGTGCTAAAAATTATTTAAAGAAAATACCAACTGATTCTCCAAACCAACTTTGTACTTATGGACATGAAAAGGATTCTTGTCAGGTCAGTATAATAGTTTTCC'
SeqSemPepSinalTrypsina = 'aatcctcaaagttatgttaacataaaatctgaagaaatagatttaactcaacaagaacaaaaatatggagaaaaagtaacaaattgttcttgtggctggactaacaaggcaagaattgttggtggacgtgaaaccttgaaaaatgaatttccattaatggccggaattatagatatggaaaagaaatttttattctgtggtgcaacaatagtaacccaaaatcacgcaataacagcatcccattgtaccacaccaaataaaaaaaagaaattaggcctagtagttggtgctcatgatgttactaaacctgatgaaaaggcagacgttgttgaaattaaagaaacagtagaacatgaaaattatagttctaaatcttatcataacgatgttgccttgttggttctttcaagatcaatcaagttcacccaagaagttggtccagcttgtctgcctactggcaaagctgatttggttaatgaatacatcaaagtacttggttggggaagattgaaaactaaaggaaaaacatcttcagttctgatgaaagttaatttaagggtaatttcaattaaagagtgtgctaaaaattatttaaagaaaataccaactgattctccaaaccaactttgtacttatggacatgaaaaggattcttgtcaggtcagtataatagttttcc'
y = seqTrypsPepSinal
l = seqOBPPepSinal
m = seqOBP
z = seqOBPOtimizada
x = seqTrypsOtimizada
primerREVOver = 'GATGGTGGTGGGTAC'
primerFWOver = 'GACGCTGGCGCCTCT'
seqaaa = 'GGTGATGGTGGTGGGTAC'
ooo = 'aatcctcaaagttatgttaacataaaatctgaagaaatagatttaactcaacaagaacaaaaatatggagaaaaagtaacaaattgttcttgtggctggactaacaaggcaagaattgttggtggacgtgaaaccttgaaaaatgaatttccattaatggccggaattatagatatggaaaagaaatttttattctgtggtgcaacaatagtaacccaaaatcacgcaataacagcatcccattgtaccacaccaaataaaaaaaagaaattaggcctagtagttggtgctcatgatgttactaaacctgatgaaaaggcagacgttgttgaaattaaagaaacagtagaacatgaaaattatagttctaaatcttatcataacgatgttgccttgttggttctttcaagatcaatcaagttcacccaagaagttggtccagcttgtctgcctactggcaaagctgatttggttaatgaatacatcaaagtacttggttggggaagattgaaaactaaaggaaaaacatcttcagttctgatgaaagttaatttaagggtaatttcaattaaagagtgtgctaaaaattatttaaagaaaataccaactgattctccaaaccaactttgtacttatggacatgaaaaggattcttgtcaggtcagtataatagttttcc'


'''
where60(z)
where60(complement(z)[::-1])
primersEnd(z, 23,26)'''
automaticPrimerDesigner(ooo)




''''''

'''
revSeq = ooo[::-1]
print('-'*50)
print('Contando a % de GC da sequência do primerFW'.center(50))
print('-'*50)
contGC(ooo)
print('-'*50)
print('Contando a % de GC da sequência do primerREV'.center(50))
print('-'*50)
contGC(complement(revSeq))
print('-'*50)
print('Dados dos primers FW e REV'.center(50))
print('-'*50)
primersEnd(ooo,29,27)
'''

print(GC('ggaaaactattatactgacctgacaag'.upper()), GC('ggaaaactattatactgacctgacaag')/len('ggaaaactattatactgacctgacaag'))


TM('ggaaaactattatactgacctgacaag'.upper())
'''CTAGTGGTGGTGATGGTGGTGGGTACggaaaactattatactgacctgacaagaatccttt'''