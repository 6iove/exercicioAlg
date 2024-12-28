import random 
import string

alunos_cadastrados = []

def cadastro_de_alunos():
    print("*** CADASTRAR ALUNO ***")
    
    nome = input("Nome do aluno: ")
    data_de_nascimento = input("Data de nascimento: ")
    genero_sexual = input("Gênero sexual: ")
    endereco = input("Endereço completo: ")
    telefone = input("Número de telefone: ")
    email = input("E-mail: ")
    
    gerar_numero_de_matricula()
    
    aluno = {
        "Nome": nome, 
        "Data de nascimento": data_de_nascimento, 
        "Gênero sexual": genero_sexual, 
        "Endereço": endereco, 
        "Telefone": telefone, 
        "E-mail": email,
        "Matrícula": gerar_numero_de_matricula() 
    }
    
    alunos_cadastrados.append(aluno)
    return alunos_cadastrados

def gerar_numero_de_matricula():
    numero_matricula = ''.join(random.choices(string.digits, k = 6))
    letra_matricula = random.choice(string.ascii_uppercase)
    return f"{numero_matricula}-{letra_matricula}"
  
print(cadastro_de_alunos()) 

professores_cadastrados = []

def cadastro_de_professores():
    print("*** CADASTRAR PROFESSOR ***")
    
    nome = input("Nome completo: ")
    data_de_nascimento = input("Data de nascimento: ")
    genero_sexual = input("Gênero sexuaL: ")
    endereco = input("Endereço completo: ")
    telefone = input("Número de telefone: ")
    email = input("E-mail: ")
    disciplina = input("Disciplina: ")
    
    professores = {
        "Nome": nome, 
        "Data de nascimento": data_de_nascimento, 
        "Gênero sexual": genero_sexual, 
        "Endereço": endereco, 
        "Telefone": telefone, 
        "E-mail": email, 
        "Disciplina": disciplina, 
        "Matrícula": gerar_matricula_do_professor()
    }
    
    professores_cadastrados.append(professores)
    return professores_cadastrados

def gerar_matricula_do_professor():
    numero_matricula_professor = ''.join(random.choices(string.digits, k = 5))
    letra_matricula_professor = random.choice(string.ascii_uppercase)
    return f"{numero_matricula_professor}.{letra_matricula_professor}"

print(cadastro_de_professores())

disciplinas_cadastradas = []

def cadastro_de_disciplinas():
    nome_da_disciplina = input("Disciplina: ")
    carga_horaria = int(input("Carga horária: "))
    professor_da_disciplina = input("Discente: ")
    
    disciplina = {
        "Disciplina": nome_da_disciplina, 
        "Carga horária": carga_horaria,
        "Discente": professor_da_disciplina
    }
    
    disciplinas_cadastradas.append(disciplina)
    return disciplinas_cadastradas

print(cadastro_de_disciplinas())
