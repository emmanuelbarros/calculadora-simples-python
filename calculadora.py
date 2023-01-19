while True:
    n_1 = input ('Digite o primeiro número: ')
    op = input ('Digite o operador: ')
    n_2 = input ('Digite o segundo número número: ')

    numeros_validos = None
    try:

        n_1_float = float(n_1)
        n_2_float = float(n_2)
        numeros_validos = True

    except:
        numeros_validos = None


    if numeros_validos is None:
        print("Um dos números digitados é invalido.")
        continue

    op_permitidos = '+-/*'

    if op not in op_permitidos:
        print('Operador inválido.')
        continue

    if len(op) > 1:
        print('Digite apenas um operador.')
        continue

    if op ==  '+':
        print(f'Resposta: {n_1_float} + {n_2_float} = {n_1_float+n_2_float}')
    elif op ==  '-':
        print(f'Resposta: {n_1_float} - {n_2_float} = {n_1_float-n_2_float}')
    elif op ==  '/':
        print(f'Resposta: {n_1_float} / {n_2_float} = {n_1_float/n_2_float}')
    elif op ==  '*':            
        print(f'Resposta: {n_1_float} * {n_2_float} = {n_1_float*n_2_float}')

    sair = input ('Deseja sair? [s]im:  ').lower().startswith('s')
    
    if sair is True:
        break
    