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
        print(f"\nAluno {nome} cadastrado!")
        print (f"\n{nome}, {aluno['Matrícula']}")
        
        cadastrar_outro_aluno = input("Deseja cadastrar outro aluno? (s/n): ")
        if cadastrar_outro_aluno.lower() != "s": 
            break
        
    return alunos_cadastrados
    

def gerar_numero_de_matricula():
    numero_matricula = ''.join(random.choices(string.digits, k = 6))
    letra_matricula = random.choice(string.ascii_uppercase)
    return f"{numero_matricula}-{letra_matricula}"

def matricular_aluno_em_turma():
    print("\n*** MATRICULAR ALUNO EM TURMA ***")
    
    matricula_do_aluno = input("Digite a matrícula do aluno: ") # mais de um aluno pode ter o mesmo nome completo
    aluno_encontrado = None # cria variável vazia
    
    # percorre array alunos_cadastrados 
    for aluno in alunos_cadastrados:
    # procura o aluno a partir do número de matrícula armazenado percorrendo o dicionário 'aluno'
        if aluno["Matrícula"] == matricula_do_aluno:
        # variável, antes vazia, recebe as informações do aluno contidas no dicionário
            aluno_encontrado = aluno
            break
        
    if aluno_encontrado:
        print(f"Aluno: {aluno_encontrado['Nome']}")
        nome_da_turma = input("Em qual turma o aluno será matrículado? ")
        turma_encontrada = None
        
        for turma in turmas_cadastradas:
            if turma["Nome da turma"].lower() == nome_da_turma.lower():
                turma_encontrada = turma
                break
        
        if turma_encontrada:
            turma_encontrada["Alunos"].append(aluno_encontrado)
            print(f"\nO aluno {aluno_encontrado['Nome']} foi matriculado com sucesso na turma {nome_da_turma}.")
        else:
            print(f"\nNão foi possível encontrar a turma informada. Tente novamente.")
    else:
        print(f"\nNão foi possível encontrar nenhum aluno correspondente ao número de matrícula informado. Tente novamente.")
    

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
        disciplina_inicial = input("Disciplina inicial que será lecionada pelo professor: ")
    
        professores = {
            "Nome": nome, 
            "Data de nascimento": data_de_nascimento, 
            "Gênero sexual": genero_sexual, 
            "Endereço": endereco, 
            "Telefone": telefone, 
            "E-mail": email, 
            "Disciplinas": [disciplina_inicial], 
            "Matrícula": gerar_matricula_do_professor()
        }
    
        professores_cadastrados.append(professores)
        print(f"\nProfessor {nome} cadastrado!")
        print (f"\n{nome}, {professores['Matrícula']}")
    
        cadastrar_outro_professor = input("Deseja cadastrar outro profeessor? (s/n): ")
        if cadastrar_outro_professor.lower() != "s":
            break
        
    return professores_cadastrados

def gerar_matricula_do_professor():
    numero_matricula_professor = ''.join(random.choices(string.digits, k = 5))
    letra_matricula_professor = random.choice(string.ascii_uppercase)
    return f"{numero_matricula_professor}.{letra_matricula_professor}"

def alocar_professor_em_disciplina():
    print("\n*** ALOCAR PROFESSOR EM DISCIPLINA ***")
    
    matricula_do_professor = input("Digite a matrícula do professor: ") # mais de um professor pode ter o mesmo nome completo
    professor_encontrado = None # cria variável vazia
    
    # percorre array professores_cadastrados 
    for professor in professores_cadastrados:
    # procura o professor a partir do número de matrícula armazenado percorrendo o dicionário 'professor'
        if professor["Matrícula"] == matricula_do_professor:
        # variável, antes vazia, recebe as informações do professor contidas no dicionário
            professor_encontrado = professor
            break
        
    if not professor_encontrado:
        print("\nNenhum professor registrado com essa matrícula. Tente novamente.")
        return
    
    print(f"Professor registrado: {professor_encontrado['Nome']}")
    
    nome_nova_disciplina = input("Digite o nome da disciplina em que o professor será alocado: ")

    if nome_nova_disciplina not in professor_encontrado['Disciplinas']:
        professor_encontrado['Disciplinas'].append(nome_nova_disciplina)
        print(f"\nDisciplina {nome_nova_disciplina} alocada ao professor {professor_encontrado['Nome']}.")
    else:
        print("\nO professor já está associado a essa disciplina.")
          
            
# filtragem de professores por disciplina
def filtrar_professores_por_disciplina(disciplina):
    professores_encontrados = []
    
    for professor in professores_cadastrados:
        #acessa a chave 'disciplina' no dicionário
        if professor["Disciplina"].lower() == disciplina.lower():
            professores_encontrados.append(professor)
    
    if professores_encontrados: 
        print(f"Professor: {professor['Nome']}, Matrícula: {professor['Matrícula']}, Disciplina: {professor['Disciplina']}")
    else:
        print(f"Nenhum professor foi cadastrado para a disciplina {disciplina}.")

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
        print(f"Disciplina {nome_da_disciplina} cadastrada com sucesso!")
        
        cadastrar_outra_disciplina = input("Deseja cadastrar outra disciplina? (s/n): ")
        if cadastrar_outra_disciplina.lower() != "s":
            break
        
    return disciplinas_cadastradas

def gerar_codigo_disciplina():
    numero_codigo_disciplina = ''.join(random.choices(string.digits, k = 4))
    letra_codigo_disciplina = random.choice(string.ascii_uppercase)
    return f"{letra_codigo_disciplina}{numero_codigo_disciplina}" 

def alocar_disciplina_em_turmas():
    print("\n*** ALOCAR PROFESSOR EM DISCIPLINA ***")
   
    nome_disciplina = input("Digite o nome da disciplina: ")
    disciplina_encontrada = None # cria variável vazia
   
    for disciplina in disciplinas_cadastradas:
        if disciplina['Disciplina'].lower() == nome_disciplina.lower():
            disciplina_encontrada = disciplina
            break
       
    if not disciplina_encontrada:
        print("\nNenhuma disciplina encontrada com esse nome. Tente novamente.")
        return
   
    nome_turma = input("Digite o nome da turma: ")
    turma_encontrada = None
   
    for turma in turmas_cadastradas:
        if turma['Nome da turma'].lower() == nome_turma.lower():
            turma_encontrada = turma
            break
    if not turma_encontrada:
        print("\nNenhuma turma encontrada com esse nome. Tente novamente.")
        return
   
    if nome_disciplina not in turma_encontrada['Disciplinas']:
        turma_encontrada['Disciplinas'].append(nome_disciplina)
        print(f"\nA disciplina {nome_disciplina} foi alocada com sucesso a turma {nome_turma}.")
    else:
        print(f"\nA disciplina {nome_disciplina} já está alocada na turma {nome_turma}.")

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
            "Disciplinas": [],
            "Professores": professor_da_turma,
            "Alunos": [],
            "Código": gerar_código_turma()
        }
    
        turmas_cadastradas.append(turma)
        print(f"Turma {nome_turma} cadastrada com sucesso!")
        
        cadastrar_outra_turma = input("Deseja cadastrar outra turma? (s/n): ")
        if cadastrar_outra_turma.lower() != "s":
            break
        
    return turmas_cadastradas

def gerar_código_turma():
    numero_codigo_turma = ''.join(random.choices(string.digits, k = 4))
    letra_codigo_turma = random.choice(string.ascii_uppercase)
    return f"{letra_codigo_turma}{numero_codigo_turma}" 

#página inicial
def pagina_inicial(): 
    while True:   
        print ("\n*** HOMEPAGE ***")

        print("\n*** OPÇÕES DE CADASTROS ***")

        print("1. Alunos")
        print("2. Professores")
        print("3. Disciplinas")
        print("4. Turmas")
        print("5. Opções de filtragem")
        print("6. Matrícula de alunos em turmas")
        print("7. Alocar professor em disciplina")
        print("8. Alocar disciplina em turmas")
        print("Sair")

        opcao_cadastro = input("Escolha uma opção (1-6): ")

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
            matricular_aluno_em_turma()
        elif opcao_cadastro == "7":
            alocar_professor_em_disciplina()
        elif opcao_cadastro == "8":
            alocar_disciplina_em_turmas()
        else:
            print("Opção inválida. Digite 1, 2, 3, 4, ou 5.")
            
pagina_inicial()
