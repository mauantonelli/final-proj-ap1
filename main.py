import sys

mecanicos = {}
veiculos = {}
consertos = {}

def listar_mecanicos():
    print("\n=== Lista de Mecânicos ===")
    if mecanicos:
        for cpf, dados in mecanicos.items():
            print(f"CPF: {cpf}")
            print("Nome:", dados['nome'])
            print("Data de Nascimento:", dados['data_nascimento'])
            print("Sexo:", dados['sexo'])
            print("Salário:", dados['salario'])
            print("E-mails:", ', '.join(dados['emails']))
            print("Telefones:", ', '.join(dados['telefones']))
            print("-----------------------")
    else:
        print("Não há mecânicos cadastrados.")

def buscar_mecanico():
    cpf = input("CPF do Mecânico: ")
    if cpf in mecanicos:
        dados = mecanicos[cpf]
        print("\nMecânico encontrado:")
        print("CPF:", cpf)
        print("Nome:", dados['nome'])
        print("Data de Nascimento:", dados['data_nascimento'])
        print("Sexo:", dados['sexo'])
        print("Salário:", dados['salario'])
        print("E-mails:", ', '.join(dados['emails']))
        print("Telefones:", ', '.join(dados['telefones']))
    else:
        print("Mecânico não encontrado.")

def incluir_mecanico():
    cpf = input("CPF do Mecânico: ")
    if cpf in mecanicos:
        print("Mecânico já cadastrado.")
        return
    nome = input("Nome do Mecânico: ")
    data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
    sexo = input("Sexo: ")
    salario = float(input("Salário: "))
    emails = []
    while True:
        email = input("E-mail do Mecânico (ou deixe em branco para encerrar): ")
        if email == "":
            break
        emails.append(email)
    telefones = []
    while True:
        telefone = input("Telefone do Mecânico (ou deixe em branco para encerrar): ")
        if telefone == "":
            break
        telefones.append(telefone)
    mecanico = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'sexo': sexo,
        'salario': salario,
        'emails': emails,
        'telefones': telefones
    }
    mecanicos[cpf] = mecanico
    print("Mecânico cadastrado com sucesso.")

def alterar_mecanico():
    cpf = input("CPF do Mecânico: ")
    if cpf in mecanicos:
        mecanico = mecanicos[cpf]
        print("\nMecânico encontrado:")
        print("CPF:", cpf)
        print("Nome:", mecanico['nome'])
        print("Data de Nascimento:", mecanico['data_nascimento'])
        print("Sexo:", mecanico['sexo'])
        print("Salário:", mecanico['salario'])
        print("E-mails:", ', '.join(mecanico['emails']))
        print("Telefones:", ', '.join(mecanico['telefones']))
        print("\nDigite os novos dados:")
        nome = input("Nome do Mecânico: ")
        data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
        sexo = input("Sexo: ")
        salario = float(input("Salário: "))
        emails = []
        while True:
            email = input("E-mail do Mecânico (ou deixe em branco para encerrar): ")
            if email == "":
                break
            emails.append(email)
        telefones = []
        while True:
            telefone = input("Telefone do Mecânico (ou deixe em branco para encerrar): ")
            if telefone == "":
                break
            telefones.append(telefone)
        mecanico['nome'] = nome
        mecanico['data_nascimento'] = data_nascimento
        mecanico['sexo'] = sexo
        mecanico['salario'] = salario
        mecanico['emails'] = emails
        mecanico['telefones'] = telefones
        print("Mecânico alterado com sucesso.")
    else:
        print("Mecânico não encontrado.")

def excluir_mecanico():
    cpf = input("CPF do Mecânico: ")
    if cpf in mecanicos:
        confirmacao = input("Tem certeza que deseja excluir o mecânico? (s/n): ")
        if confirmacao.lower() == "s":
            del mecanicos[cpf]
            print("Mecânico excluído com sucesso.")
        else:
            print("Mecânico não encontrado.")

def listar_veiculos():
    print("\n=== Lista de Veículos ===")
    if veiculos:
        for placa, dados in veiculos.items():
            print(f"Placa: {placa}")
            print("Tipo:", dados['tipo'])
            print("Marca:", dados['marca'])
            print("Modelo:", dados['modelo'])
            print("Ano:", dados['ano'])
            print("Portas:", dados['portas'])
            print("Combustível:", dados['combustivel'])
            print("Cor:", dados['cor'])
            print("-----------------------")
    else:
        print("Não há veículos cadastrados.")

def buscar_veiculo():
    placa = input("Placa do Veículo: ")
    if placa in veiculos:
        dados = veiculos[placa]
        print("\nVeículo encontrado:")
        print("Placa:", placa)
        print("Tipo:", dados['tipo'])
        print("Marca:", dados['marca'])
        print("Modelo:", dados['modelo'])
        print("Ano:", dados['ano'])
        print("Portas:", dados['portas'])
        print("Combustível:", dados['combustivel'])
        print("Cor:", dados['cor'])
    else:
        print("Veículo não encontrado.")

def incluir_veiculo():
    placa = input("Placa do Veículo: ")
    if placa in veiculos:
        print("Veículo já cadastrado.")
        return
    tipo = input("Tipo do Veículo: ")
    marca = input("Marca do Veículo: ")
    modelo = input("Modelo do Veículo: ")
    ano = input("Ano do Veículo: ")
    portas = int(input("Quantidade de Portas: "))
    combustivel = input("Combustível do Veículo: ")
    cor = input("Cor do Veículo: ")
    veiculo = {
        'tipo': tipo,
        'marca': marca,
        'modelo': modelo,
        'ano': ano,
        'portas': portas,
        'combustivel': combustivel,
        'cor': cor
    }
    veiculos[placa] = veiculo
    print("Veículo cadastrado com sucesso.")

def alterar_veiculo():
    placa = input("Placa do Veículo: ")
    if placa in veiculos:
        veiculo = veiculos[placa]
        print("\nVeículo encontrado:")
        print("Placa:", placa)
        print("Tipo:", veiculo['tipo'])
        print("Marca:", veiculo['marca'])
        print("Modelo:", veiculo['modelo'])
        print("Ano:", veiculo['ano'])
        print("Portas:", veiculo['portas'])
        print("Combustível:", veiculo['combustivel'])
        print("Cor:", veiculo['cor'])
        print("\nDigite os novos dados:")
        tipo = input("Tipo do Veículo: ")
        marca = input("Marca do Veículo: ")
        modelo = input("Modelo do Veículo: ")
        ano = input("Ano do Veículo: ")
        portas = int(input("Quantidade de Portas: "))
        combustivel = input("Combustível do Veículo: ")
        cor = input("Cor do Veículo: ")
        veiculo['tipo'] = tipo
        veiculo['marca'] = marca
        veiculo['modelo'] = modelo
        veiculo['ano'] = ano
        veiculo['portas'] = portas
        veiculo['combustivel'] = combustivel
        veiculo['cor'] = cor
        print("Veículo alterado com sucesso.")
    else:
        print("Veículo não encontrado.")

def excluir_veiculo():
    placa = input("Placa do Veículo: ")
    if placa in veiculos:
        confirmacao = input("Tem certeza que deseja excluir o veículo? (s/n): ")
        if confirmacao.lower() == "s":
            del veiculos[placa]
            print("Veículo excluído com sucesso.")
        else:
            print("Veículo não encontrado.")

def listar_consertos():
    print("\n=== Lista de Consertos ===")
    if consertos:
        for codigo, dados in consertos.items():
            print(f"Código: {codigo}")
            print("CPF do Mecânico:", dados['cpf'])
            print("Placa do Veículo:", dados['placa'])
            print("Data de Entrada:", dados['data_entrada'])
            print("Data de Saída:", dados['data_saida'])
            print("Descrição dos Problemas:", dados['descricao'])
            print("Valor do Conserto:", dados['valor'])
            print("-----------------------")
    else:
        print("Não há consertos cadastrados.")

def buscar_conserto():
    codigo = input("Código do Conserto: ")
    if codigo in consertos:
        dados = consertos[codigo]