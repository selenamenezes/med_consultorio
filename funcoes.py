import sqlite3

def tela():
    print("=-=- Consultorio Médico -=-=")
    print("[1] - Adicionar pacientes")
    print("[2] - Buscar pacientes")
    print("[3] - Atualizar dados do paciente")
    print("[4] - Remover pacientes")
    print("[5] - Sair")

def formatar_telefone(telefone):
    telefone = telefone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    
    if len(telefone) == 11:
        return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    elif len(telefone) == 10:
        return f"({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}"
    else:
        return "Telefone inválido"
    
def formatar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "").replace(" ", "")

    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    else:
        return "CPF inválido"

def cadastrar_paciente(conexao, nome, cpf, data_nascimento, telefone):
    cursor = conexao.cursor()

    cpf = formatar_cpf(cpf)
    telefone = formatar_telefone(telefone)

    # verifica se é valido o cpf e telefone
    if cpf and telefone: 
        # verifica se ja tem algum cpf ou telefone com o mesmo numero
        cursor.execute('SELECT cpf, telefone FROM paciente WHERE cpf = ? OR telefone = ?', (cpf, telefone,))
        registro = cursor.fetchone()

        if registro:
            print("O CPF ou telefone já está cadastrado.")
        else:
            cursor.execute('''
                INSERT INTO paciente (nome, cpf, data_nascimento, telefone)
                VALUES (?, ?, ?, ?)
            ''', (nome, cpf, data_nascimento, telefone))
            conexao.commit()
            print("Paciente cadastrado com sucesso!")
    else:
        print("Erro ao cadastrar o paciente, CPF ou telefone inválido!")

def ler_dados(conexao):
    cursor = conexao.cursor()
    # procura os pacientes 
    cursor.execute('SELECT * FROM paciente')
    registros = cursor.fetchall()
    if registros:
        for col in registros:
            telefone_formatado = formatar_telefone(col[3])  
            cpf_formatado = formatar_cpf(col[1]) 

            print(f"Nome: {col[0]}")
            print(f"CPF: {cpf_formatado}")
            print(f"Data de Nascimento: {col[2]}")
            print(f"Telefone: {telefone_formatado}")
             
    else:
        print("Não há pacientes cadastrados.")

def atualizar_paciente(conexao, nome, cpf, data_nascimento, telefone):
    cursor = conexao.cursor()

    cpf = formatar_cpf(cpf)
    telefone = formatar_telefone(telefone)

    # verifica se esta formatado o telefone e o cpf
    if not cpf and not telefone:  
        return "Erro ao tentar atualizar os dados do paciente, CPF ou telefone inválido!"

    # procura o paciente
    cursor.execute('SELECT * FROM paciente WHERE cpf = ?', (cpf,))
    registros = cursor.fetchone()

    if registros:  # verifica se ele esta no registro
        cursor.execute('''
        UPDATE paciente
        SET nome = ?, data_nascimento = ?, telefone = ?
        WHERE cpf = ?
        ''', (nome, data_nascimento, telefone, cpf))

        conexao.commit() 
        print("Atualização de registro concluída.")
    else:
        print("Paciente com CPF não encontrado.")

def remover_paciente(conexao, cpf):
    cursor = conexao.cursor()

    cpf = formatar_cpf(cpf)
    
    # verifica se o cpf é valido
    if not cpf:
        return "Erro ao tentar remover o paciente, CPF inválido."
       
    # procura o paciente
    cursor.execute('SELECT cpf FROM paciente WHERE cpf = ?', (cpf,))
    registros = cursor.fetchone()  
    
    if registros:  # verifica se ele esta no registro
        cursor.execute('DELETE FROM paciente WHERE cpf = ?', (cpf,))
        conexao.commit() 
        print(f"Paciente com CPF {cpf} foi removido com sucesso.")
    else:
        print(f"Paciente com CPF {cpf} não encontrado.")

    cursor.close()  
