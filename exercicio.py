import random 
import string

alunos_cadastrados = []

def cadastro_de_alunos():
    while True: 
        print("*** CADASTRAR ALUNO ***")
    
        nome = input("Nome do aluno: ")
        data_de_nascimento = input("Data de nascimento: ")
        genero_sexual = input("Gênero sexual: ")
        endereco = input("Endereço completo: ")
        telefone = input("Número de telefone: ")
        email = input("E-mail: ")
    
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
        
        cadastrar_outro_aluno = input("Deseja cadastrar outro aluno? (s/n): ")
        if cadastrar_outro_aluno.lower() != "s": 
            break
        
    return alunos_cadastrados

def gerar_numero_de_matricula():
    numero_matricula = ''.join(random.choices(string.digits, k = 6))
    letra_matricula = random.choice(string.ascii_uppercase)
    return f"{numero_matricula}-{letra_matricula}"
   

professores_cadastrados = []

def cadastro_de_professores():
    while True:
        
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
    
        cadastrar_outro_professor = input("Deseja cadastrar outro profeessor? (s/n): ")
        if cadastrar_outro_professor.lower() != "s":
            break
        
    return professores_cadastrados

def gerar_matricula_do_professor():
    numero_matricula_professor = ''.join(random.choices(string.digits, k = 5))
    letra_matricula_professor = random.choice(string.ascii_uppercase)
    return f"{numero_matricula_professor}.{letra_matricula_professor}"


disciplinas_cadastradas = []

def cadastro_de_disciplinas():
    while True:
        
        print("*** CADASTRAR DISCIPLINAS ***")
    
        nome_da_disciplina = input("Disciplina: ")
        carga_horaria = int(input("Carga horária: "))
        professor_da_disciplina = input("Discente: ")
    
        disciplina = {
            "Disciplina": nome_da_disciplina, 
            "Carga horária": carga_horaria,
            "Discente": professor_da_disciplina,
            "Código": gerar_codigo_disciplina()
        }
    
        disciplinas_cadastradas.append(disciplina)
        
        cadastrar_outra_disciplina = input("Deseja cadastrar outra disciplina? (s/n): ")
        if cadastrar_outra_disciplina.lower() != "s":
            break
        
    return disciplinas_cadastradas

def gerar_codigo_disciplina():
    numero_codigo_disciplina = ''.join(random.choices(string.digits, k = 4))
    letra_codigo_disciplina = random.choice(string.ascii_uppercase)
    return f"{letra_codigo_disciplina}{numero_codigo_disciplina}" 


turmas_cadastradas = []

def cadastro_de_turmas():
    while True:
        
        print("*** CADASTRAR TURMAS ***")
    
        nome_turma = input("Nome da turma: ")
        disciplinas_da_turma = input("Disciplinas lecionadas à turma: ")
        professor_da_turma = input("Discentes da turma: ")
        alunos_da_turma = input("Alunos matrículados na turma: ")
    
        turma = {
            "Nome da turma": nome_turma,
            "Disciplinas": disciplinas_da_turma,
            "Professores": professor_da_turma,
            "Alunos": alunos_da_turma,
            "Código": gerar_código_turma()
        }
    
        turmas_cadastradas.append(turma)
        
        cadastrar_outra_turma = input("Deseja cadastrar outra turma? (s/n): ")
        if cadastrar_outra_turma.lower() != "s":
            break
        
    return turmas_cadastradas

def gerar_código_turma():
    numero_codigo_turma = ''.join(random.choices(string.digits, k = 4))
    letra_codigo_turma = random.choice(string.ascii_uppercase)
    return f"{letra_codigo_turma}{numero_codigo_turma}" 


# filtragem de professores por disciplina
def filtrar_professores_por_disciplina(disciplina):
    professores_encontrados = []
    
    for professor in professores_cadastrados:
        #acessa a chave disciplina no dicionário
        if professor["Disciplina"].lower() == disciplina.lower():
            professores_encontrados.append(professor)
    
    if professores_encontrados: 
        print(f"Professor: {professor['Nome']}, Matrícula: {professor['Matrícula']}, Disciplina: {professor['Disciplina']}")
    else:
        print(f"Nenhum professor foi cadastrado para a disciplina {disciplina}.")
    
#página inicial
def pagina_inicial(): 
    while True:   
        print ("*** HOMEPAGE ***")

        print("\n*** OPÇÕES DE CADASTROS ***")

        print("1. Alunos")
        print("2. Professores")
        print("3. Disciplinas")
        print("4. Turmas")
        print("5. Opções de filtragem")
        print("6. Sair")

        opcao_cadastro = input("Escolha uma opção: ")

        if opcao_cadastro == "1":
            cadastro_de_alunos()
        elif opcao_cadastro == "2":
            cadastro_de_professores()  
        elif opcao_cadastro == "3":
            cadastro_de_disciplinas()
        elif opcao_cadastro == "4": 
            cadastro_de_turmas()
        elif opcao_cadastro == "5":
            print("1. Filtragem de professores por disciplina")
            opcao_filtragem = input("Confirma? s/n: ")
            if opcao_filtragem == "s":
                disciplina = input("Digite a disciplina para a filtragem de professores: ")
                filtrar_professores_por_disciplina(disciplina)
            elif opcao_filtragem == "n":
                print("Fechando programa.")
                break
            else:
                print("Opção inválida.")
        elif opcao_cadastro == "6":
            print("Fechando programa.")
            break
        else:
            print("Opção inválida. Digite 1, 2, 3, 4, ou 5.")
            
pagina_inicial()
