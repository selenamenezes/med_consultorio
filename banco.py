import sqlite3

banco = sqlite3.connect('cadastro_paciente_consultorio.db')
cursor = banco.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS paciente (
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL PRIMARY KEY,
    data_nascimento DATE NOT NULL,
    telefone TEXT NOT NULL UNIQUE
)
''')

banco.commit()
banco.close()