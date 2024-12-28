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
        "Disciplina": disciplina
    }
    
    professores_cadastrados.append(professores)
    return professores_cadastrados

print(cadastro_de_professores())
