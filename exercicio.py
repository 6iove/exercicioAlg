import random 
import string


# --- FUNÇÕES DE CADASTROS
alunos_cadastrados = []

def cadastro_de_alunos():
    while True: 
        print("*** CADASTRAR ALUNO ***")
        
    #recolhimento de dados
        nome = validar_nome()
        data_de_nascimento = validar_data_de_nascimento()
        genero = validar_genero()
        print("Endereço -")
        endereco_rua = input("Rua: ")
        endereco_numero = input("Número: ")
        telefone = validar_telefone()
        email = validar_email()
    
    #dicionário
        aluno = {
            "Nome": nome, 
            "Data de nascimento": data_de_nascimento, 
            "Gênero": genero, 
            "Endereço": endereco_rua and endereco_numero,
            "Telefone": telefone, 
            "E-mail": email,
            "Matrícula": gerar_numero_de_matricula() 
        }
    
    #inclusão do dicionário na lista
        alunos_cadastrados.append(aluno)
        #imprime informações necessárias para o uso de outras funções do sistema
        print(f"\nAluno {nome} cadastrado!")
        print (f"\n{nome}, {aluno['Matrícula']}")
        
        #opção de cadastrar mais alunos, que estarão alocados no mesmo dicionário, na mesma lista
        cadastrar_outro_aluno = input("Deseja cadastrar outro aluno? (s/n): ")
        if cadastrar_outro_aluno.lower() != "s": 
            break
    
    #retorna a lista, agora com o dicionário
    return alunos_cadastrados
    
professores_cadastrados = []

def cadastro_de_professores():
    while True:
        
        print("*** CADASTRAR PROFESSOR ***")
    
        nome = validar_nome()
        data_de_nascimento = validar_data_de_nascimento()
        genero = validar_genero()
        print("Endereço -")
        endereco_rua = input("Rua: ")
        endereco_numero = input("Número: ")
        telefone = validar_telefone()
        email = validar_email()
        disciplina_inicial = input("Disciplina inicial que será lecionada pelo professor: ")
    
        professor = {
            "Nome": nome, 
            "Data de nascimento": data_de_nascimento, 
            "Gênero": genero, 
            "Endereço": endereco_rua and endereco_numero, 
            "Telefone": telefone, 
            "E-mail": email, 
            "Disciplinas": [disciplina_inicial], 
            "Matrícula": gerar_matricula_do_professor()
        }
    
        professores_cadastrados.append(professor)
        print(f"\nProfessor {nome} cadastrado!")
        print (f"\n{nome}, {professor['Matrícula']}")
    
        cadastrar_outro_professor = input("Deseja cadastrar outro profeessor? (s/n): ")
        if cadastrar_outro_professor.lower() != "s":
            break
        
    return professores_cadastrados

disciplinas_cadastradas = []

def cadastro_de_disciplinas():
    while True:
        
        print("*** CADASTRAR DISCIPLINAS ***")
    
        nome_da_disciplina = input("Disciplina: ")
        carga_horaria = int(input("Carga horária: "))
        professor_da_disciplina = input("Professores: ")
    
        disciplina = {
            "Disciplina": nome_da_disciplina, 
            "Carga horária": carga_horaria,
            "Professores": professor_da_disciplina,
            "Código": gerar_codigo_disciplina()
        }
    
        disciplinas_cadastradas.append(disciplina)
        print(f"Disciplina {nome_da_disciplina} cadastrada com sucesso!")
        
        cadastrar_outra_disciplina = input("Deseja cadastrar outra disciplina? (s/n): ")
        if cadastrar_outra_disciplina.lower() != "s":
            break
        
    return disciplinas_cadastradas

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

# --- CAMPO DE VERIFICAÇÃO

#função para validar entradas que devem ser números. o uso do int ou float não permite o uso de len.
def validar_input(input, digitos):
    return input.isdigit() and len(input) == digitos

def validar_nome():
    while True:
        nome = input("Nome completo: ")
        
        # o uso do len mais o split irá verificar se existem ao menos duas 'palavras' no nome, para ser considerado completo
        if len(nome.split()) < 2:
            print("Certifique-se de inserir primeiro nome e sobrenome.")
        else:
            # return é a condição de parada do loop while
            return nome
        
def validar_data_de_nascimento():
    while True:
        data_de_nascimento = input("Data de nascimento (DDMMAAAA): ")
        
        # o replace irá substituir espaços por nenhum espaço, ou seja, quaisquer espaços que possam ser adicionados pelo usuário serão ignorados
        data = data_de_nascimento.replace(" ", "")
        
        # são colocadas duas condições para validar a entrada, data, que é a data_de_nascimento sem espaços adicionais e 8, a quantidade máxima (e aqui obrigatória) de números numa data
        if validar_input(data, 8):
        # condição de parada
            return data
        else:
            print("\nA data de nascimento informada é inválida. Certifique-se de informar dia, mês e ano, respectivamente.")
            
def validar_genero():
    while True:
        # lower irá transformar as letras em minuscula, caso o usuário a insira como maiúscula 
        genero = input("Gênero (F/M): ").lower()
        
        # uma lista atribuída a validos, que será usada no if, para que apenas o que esta na lista seja aceito
        validos = ['m', 'f']
        
        if genero in validos:
            return genero
        else:
            print("\nO gênero informado é inválido. Certifique-se de digitar 'f' para feminino ou 'm' para masculino.")
            
def validar_telefone():
    while True:
        telefone = input("Telefone (móvel): ")
        
        numero = telefone.replace(" ", "")
        
        if validar_input(numero, 11):
            return numero 
        else:
            print("\nO número de telefone informado é inválido. Certifique-se de que informou o ddd.") 

def validar_email():
    while True:
        email = input("E-mail: ")
        
        # elementos obrigatórios para a consideração de um email
        if "@" and "." in email:
            return email
        else:
            print("\nO E-mail informado é inválido.")

# --- FUNÇÕES DE GERAR CÓDIGOS

# ''.join(random.choice(string.digits, k = 6)), --> randomicamente escolhe 6 digitos (definido pelo k) que serão retirados da biblioteca string.digits (0 - 9); .join irá pegar os 6 digitos e adicionar a uma string, o '' é onde deveria estar o separador, que esta vazio. 

# random.choice(string.ascii_uppercase) --> randomicamente escolhe uma letra do alfabeto da biblioteca string. Na biblioteca string 'ascii_uppercase' possui letras de A-Z maiúsculas.

# o return de cada função irá retornar o numero de matricula o código num padrão definido (123456-A)/(12345.A)...

def gerar_numero_de_matricula():
    numero_matricula = ''.join(random.choices(string.digits, k = 6))
    letra_matricula = random.choice(string.ascii_uppercase)
    return f"{numero_matricula}-{letra_matricula}"

def gerar_matricula_do_professor():
    numero_matricula_professor = ''.join(random.choices(string.digits, k = 5))
    letra_matricula_professor = random.choice(string.ascii_uppercase)
    return f"{numero_matricula_professor}.{letra_matricula_professor}"

def gerar_codigo_disciplina():
    numero_codigo_disciplina = ''.join(random.choices(string.digits, k = 4))
    letra_codigo_disciplina = random.choice(string.ascii_uppercase)
    return f"{letra_codigo_disciplina}{numero_codigo_disciplina}" 

def gerar_código_turma():
    numero_codigo_turma = ''.join(random.choices(string.digits, k = 4))
    letra_codigo_turma = random.choice(string.ascii_uppercase)
    return f"{letra_codigo_turma}{numero_codigo_turma}"

# --- FUNÇÕES DE ALOCAÇÃO
def matricular_aluno_em_turma():
    print("\n*** MATRICULAR ALUNO EM TURMA ***")
    
    matricula_do_aluno = input("Digite a matrícula do aluno: ")  # mais de um aluno pode ter o mesmo nome completo
    aluno_encontrado = None # cria variável vazia
    
    # percorre array alunos_cadastrados (percorre por cada aluno alocado no array)
    for aluno in alunos_cadastrados:
    # procura o aluno a partir do número de matrícula armazenado percorrendo o dicionário 'aluno'
        if aluno["Matrícula"] == matricula_do_aluno:
        # variável, antes vazia, recebe as informações do aluno contidas no dicionário
            aluno_encontrado = aluno
            # termina loop for
            break
        
    # quando aluno_encontrado não for mais variável vazia
    if aluno_encontrado:
        print(f"Aluno: {aluno_encontrado['Nome']}")
        nome_da_turma = input("Em qual turma o aluno será matrículado? ") 
        # variável vazia
        turma_encontrada = None
        
        # percorre array turmas_cadastradas 
        for turma in turmas_cadastradas:
            # verifica se o nome da turma está no dicionário
            if turma["Nome da turma"].lower() == nome_da_turma.lower():
            #variável, antes vazia, recebe informações de turma encontradas no dicionário
                turma_encontrada = turma
                break
        
        # quando variável vazia recebe valor
        if turma_encontrada: 
            # a lista aluno_encontrado está sendo adicionada à lista turma_encontrada, na chave 'Alunos', ou seja, o aluno encontrado esta sendo registrado na turma
            turma_encontrada["Alunos"].append(aluno_encontrado)
            print(f"\nO aluno {aluno_encontrado['Nome']} foi matriculado com sucesso na turma {nome_da_turma}.")
        else:
            print(f"\nNão foi possível encontrar a turma informada. Tente novamente.")
    else:
        print(f"\nNão foi possível encontrar nenhum aluno correspondente ao número de matrícula informado. Tente novamente.")
    
def alocar_professor_em_disciplina():
    print("\n*** ALOCAR PROFESSOR EM DISCIPLINA ***")
    
    matricula_do_professor = input("Digite a matrícula do professor: ")  # mais de um professor pode ter o mesmo nome completo
    professor_encontrado = None # cria variável vazia
    
    # percorre array professores_cadastrados 
    for professor in professores_cadastrados:
    # procura o professor a partir do número de matrícula armazenado percorrendo o dicionário 'professor'
        if professor["Matrícula"] == matricula_do_professor:
        # variável, antes vazia, recebe as informações do professor contidas no dicionário
            professor_encontrado = professor
            break
        
    if professor_encontrado:
        print(f"Professor registrado: {professor_encontrado['Nome']}")
        
    else:
        print("\nNenhum professor registrado com essa matrícula. Tente novamente.")
        return
    
    nome_nova_disciplina = input("Digite o nome da disciplina em que o professor será alocado: ") 

    if nome_nova_disciplina not in professor_encontrado['Disciplinas']:
        professor_encontrado['Disciplinas'].append(nome_nova_disciplina)
        print(f"\nDisciplina {nome_nova_disciplina} alocada ao professor {professor_encontrado['Nome']}.")
    else:
        print("\nO professor já está associado a essa disciplina.")
        
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
          
# --- CONSULTAS
def consultar_alunos_em_turmas():
    print("\n*** CONSULTAR ALUNOS EM TURMAS ***")
    
    nome_turma = input("Digite o nome da turma que deseja consultar: ") 
    turma_encontrada = None
    
    # percorre o array
    for turma in turmas_cadastradas:
        # se o nome dado no input corresponde à chave no dicionário turma_encontrada receberá a lista turma
        if turma['Nome da turma'].lower() == nome_turma.lower():
            turma_encontrada = turma
            break
    if turma_encontrada:
        # no dicionário consultará a chave alunos, onde foram alocados os alunos matriculados na turma
        if turma_encontrada['Alunos']:
            # mostrará os alunos e numero de matricula
            print(f"\nAlunos matrículados na turma {nome_turma}: ")
            for aluno in turma_encontrada['Alunos']:
                    print(f"{aluno['Nome']}, Matrícula: {aluno['Matrícula']}")
        else:
            print(f"\nNão há alunos matriculados na turma {nome_turma} ainda.")
    else: 
        print(f"\nNenhuma turma encontrada com o nome {nome_turma}.")
    
def consultar_professores_em_disciplina():
    print("\n*** CONSULTAR PROFESSORES EM DISCIPLINAS ***")
    
    nome_disciplina = input("Digite o nome da disciplina que deseja consultar: ") 
    disciplina_encontrada = None
    
    for disciplina in disciplinas_cadastradas:
        if disciplina['Disciplina'].lower() == nome_disciplina.lower():
            disciplina_encontrada = disciplina
            break
        
    if disciplina_encontrada:
        if disciplina_encontrada['Professores']:
            print(f"\nProfessores alocados na disciplina {nome_disciplina}: ")
            for professor in disciplina_encontrada['Professores']:
                print(f"{disciplina_encontrada['Professores']}")
        else:
            print(f"\nNão há professores alocados na disciplina {nome_disciplina} ainda.")
    else:
        print(f"\nNenhuma disciplina encontrada com o nome {nome_disciplina}.")
        
def consultar_disciplinas_em_turmas():
    print("\n*** CONSULTAR DISCIPLINAS EM TURMAS ***")
    
    nome_turma = input("Digite o nome da turma que deseja consultar: ")
    turma_encontrada = None
    
    for turma in turmas_cadastradas:
        if turma['Nome da turma'].lower() == nome_turma.lower():
            turma_encontrada = turma
            break
        
    if turma_encontrada:
        if turma_encontrada['Disciplinas']:
            print(f"\nDisciplinas alocadas na turma {nome_turma}: ")
            for disciplina in turma_encontrada['Disciplinas']:
                print(f"\n{turma_encontrada['Disciplinas']}")
        else:
            print(f"\nNão há disciplinas alocadas na turma {nome_turma} ainda.")
    else:
        print(f"\nNenhuma turma encontrada com o nome{nome_turma}.")
        
# ---- filtragem de professores por disciplina
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

# --- PÁGINA INICIAL
def pagina_inicial(): 
    while True:   
        print ("\n*** HOMEPAGE ***")

        print("\n*** OPÇÕES DE MENU ***")

        print("1. Cadastrar alunos")
        print("2. Cadastrar professores")
        print("3. Cadastrar disciplinas")
        print("4. Cadastrar turmas")
        print("5. Opções de filtragem")
        print("6. Matrícula de alunos em turmas")
        print("7. Opções de alocação")
        print("8. Opções de consulta")
        print("9. Sair")

        opcao_menu = input("Escolha uma opção (1-9): ")

        if opcao_menu == "1":
            cadastro_de_alunos()
        elif opcao_menu == "2":
            cadastro_de_professores()  
        elif opcao_menu == "3":
            cadastro_de_disciplinas()
        elif opcao_menu == "4": 
            cadastro_de_turmas()
        elif opcao_menu == "5":
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
        elif opcao_menu == "6":
            matricular_aluno_em_turma()
        elif opcao_menu == "7":
            print("1. Alocação de professores em disciplia")
            print("2. Alocação de disciplinas em turmas")
            opcao_alocacao = input("Escolha uma opção de alocação (1-2): ")
            if opcao_alocacao == "1":
                alocar_professor_em_disciplina()
            if opcao_alocacao == "2":
                alocar_disciplina_em_turmas()
        elif opcao_menu == "8":
            print("1. Consulta de alunos matriculados em turmas")
            print("2. Consulta de professores alocados em disciplinas")
            print("3. Consultar disciplinas alocadas em turmas")
            opcao_consulta = input("Escolha uma opção de consulta (1-3): ")
            if opcao_consulta == "1":
                consultar_alunos_em_turmas()
            elif opcao_consulta == "2":
                consultar_professores_em_disciplina()
            elif opcao_consulta == "3":
                consultar_disciplinas_em_turmas()
        elif opcao_menu == "9":
            print("Fechando o sistema.")
            break
        else:
            print("Opção inválida. Digite 1, 2, 3, 4, 5, 6, 7, 8 ou 9.")
            
pagina_inicial()
