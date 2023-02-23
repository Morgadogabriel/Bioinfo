def ContadorW(input):
    passo = 1
    W = 0
    Y = 0
    I = 0
    C = 0
    Wpos = []
    Ipos = []
    Cpos = []
    Ypos = []
    
    for i in input:
        if i == 'W':
            print(i, passo)
            Wpos.append(passo)
            W += 1
    
        if i == 'Y':
            print(i, passo)
            Ypos.append(passo)
            Y += 1
    
        if i == 'C':
            print(i, passo)
            Cpos.append(passo)
            C += 1
    
        if i == 'I':
            print(i, passo)
            Ipos.append(passo)
            I += 1
    
        passo += 1
    print('-' * 30)
    print(f'W = {W}\n'
          f'I = {I}\n'
          f'C = {C}\n'
          f'Y = {Y}')
    print(f'posições de W = {Wpos}')
    print(f'posições de I = {Ipos}')
    print(f'posições de C = {Cpos}')
    print(f'posições de Y = {Ypos}')