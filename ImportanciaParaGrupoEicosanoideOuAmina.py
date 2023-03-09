lig1 = ['GLU109', 'TYR105', 'TRP8', 'PHE108', 'TRP67', 'GLN1', 'GLU5', 'GLU71', 'GLU12', 'ARG26', 'ASN4', 'ARG111', 'GLY9', 'ILE36', 'LEU30', 'SER32', 'THR31', 'TYR102']
lig2 = ['GLU109', 'ILE29', 'LEU30', 'TYR105', 'ARG111', 'GLN1', 'GLU5', 'GLU71', 'TRP67', 'TRP8', 'ASN4', 'PHE108', 'ILE36', 'TYR102', 'GLU2']
lig3 = ['GLN1', 'GLU109', 'GLU5', 'GLU71', 'TRP67', 'ASN4', 'PHE108', 'TRP8', 'TYR105', 'ARG26', 'GLU12', 'GLY9', 'ARG111', 'LEU30']
lig4 = ['ARG26', 'GLU109', 'GLU12', 'GLU5', 'GLY9', 'LEU30', 'LYS13', 'TRP67', 'TRP8', 'TYR105', 'GLU6', 'GLU71', 'LYS10', 'PHE108', 'ARG111', 'ASN4', 'GLN1', 'ILE29', 'TYR43', 'VAL44', 'GLN16', 'SER23']
lig5 = ['ARG26', 'GLU12', 'GLU5', 'GLY9', 'LEU30', 'LYS13', 'PHE108', 'TRP67', 'TRP8', 'TYR105', 'GLN16', 'GLU6', 'LYS10', 'GLU109', 'ARG111', 'ASN4', 'GLU71']
lig6 = ['ARG26', 'GLU12', 'GLY9', 'LYS13', 'TRP8', 'GLN16', 'SER23', 'GLU2', 'GLU5', 'GLU6', 'LYS10']

aminasB = []

eicosanoides = []

for i in lig1:
    aminasB.append(i)
for i2 in lig2:
    if not i2 in aminasB:
        aminasB.append(i2)
for i3 in lig3:
    if not i3 in aminasB:
        aminasB.append(i3)
print(f'aminoacidos que se ligam a aminas biogenicas {aminasB}')

for i4 in lig4:
    eicosanoides.append(i4)
for i5 in lig5:
    if not i5 in eicosanoides:
        eicosanoides.append(i5)

print(f'aminoacidos que se ligam a eicosanoides {eicosanoides}')

fixedAAinAB = []
fixedAAinEI = []

for i7 in lig3:
    if i7 in lig2 and lig1:
        fixedAAinAB.append(i7)

for i8 in lig5:
    if i8 in lig4:
        fixedAAinEI.append(i8)



print(f'aminoacidos presentes em todas interações com aminas B {fixedAAinAB}')
print(f'aminoacidos presentes em todas interações com eicosanoides {fixedAAinEI}')