alunos_cadastrados = []

def cadastro_de_alunos():
    nome = input("Nome do aluno: ")
    data_de_nascimento = input("Data de nascimento: ")
    genero_sexual = input("Gênero sexual: ")
    endereço = input("Endereço completo: ")
    telefone = input("Número de telefone: ")
    email = input("E-mail: ")
    
    aluno = {
        "Nome": nome, 
        "Data de nascimento": data_de_nascimento, 
        "Gênero sexual": genero_sexual, 
        "Endereço": endereço, 
        "Telefone": telefone, 
        "E-mail": email
    }
    
    alunos_cadastrados.append(aluno)
    return alunos_cadastrados

print(cadastro_de_alunos())