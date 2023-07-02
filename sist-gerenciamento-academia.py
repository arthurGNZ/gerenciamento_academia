import os
from platform import system #Para limpar o terminal
import re #utilizando regex para validar email
import smtplib #bibliotecas para enviar email
from email.mime.text import MIMEText
class Aluno:
  nome = None
  cpf = None
  peso = 0
  altura = 0
  status = False
  email = None
  #construtor
  def __init__(self, nome, cpf, peso, altura, email):
    self.nome = nome
    self.cpf = cpf
    self.peso = peso
    self.altura = altura
    self.email = email

class Exercicio:
  nomeExercicio = None
  numRepeticoes = 0
  pesoExercicio = 0 
  #construtor
  def __init__(self, nomeExercicio, numRepeticoes, pesoExercicio):
    self.nomeExercicio = nomeExercicio
    self.numRepeticoes = numRepeticoes
    self.pesoExercicio = pesoExercicio

# variáveis globais:
cadAlunos = [] # lista de alunos
treinoAlunos = [] #matriz de treinos
barra = "--------------------------------------------------------------------------------------------------------"
#Funções:
def limpar_terminal(): # Função para limpar o terminal
    sistema_operacional = system()
    if sistema_operacional == 'Windows':
        os.system('cls')  # Comando para limpar o terminal no Windows
    else:
        os.system('clear')  # Comando para limpar o terminal em sistemas Unix (Linux, macOS)

def mostrarAlunosID(): # Função para exibir todos os alunos com seu id e nome
    print("Lista dos alunos:")
    for i in range(len(cadAlunos)):
        print(f"ID: {i} -- Nome: {cadAlunos[i].nome}")

def verificaEmail(email):#função para verificar o formato do email
   padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$' #padrão de expressão regular r'^[\w\.-]+@[\w\.-]+\.\w+$' para verificar o formato básico de um endereço de email
   corresponde_padrao = re.match(padrao_email, email)
   return(corresponde_padrao)

def enviarEmail(email):
    # Configurações do servidor SMTP e das credenciais do Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'arthur.h12@aluno.ifsc.edu.br' # Email que irá ser utilizado para enviar (tive que utilizar o meu email institucional do ifsc, pois estava com problemas de permissão no gmail)
    smtp_password = 'Arthur12'

    # Configurações do email
    remetente = 'arthur.h12@aluno.ifsc.edu.br'
    destinatario = email
    assunto = 'Inscrição Na Academia da UFFS'
    corpo_email = 'Olá, seja bem-vindo a academia da UFFS'

    # Criando a mensagem do email
    mensagem = MIMEText(corpo_email)
    mensagem['From'] = remetente
    mensagem['To'] = destinatario
    mensagem['Subject'] = assunto

    # Inicialização da conexão SMTP
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.starttls()
    smtp.login(smtp_username, smtp_password)

    # Envio do email
    smtp.sendmail(remetente, destinatario, mensagem.as_string())

    # Encerramento da conexão SMTP
    smtp.quit()

def cadastroAluno():
    limpar_terminal()
    nome = input("Insira o nome do aluno: ")
    nome = nome.upper()
    cpf = input("Inisira o CPF do aluno (sem pontuação): ")
    peso = input("Insira o peso do aluno em quilogramas: ")
    altura = input("Insira a altura do aluno em centímetros: ")
    email = input("Insira o email do aluno: ")
    #Verificar se o formato dos dados é válido, isso inclui a tipagem das variáveis e formatos como peso, altura e cpf:
    if(verificaEmail(email)):
        try: # Try e except para verificar o tipo da variável, caso não seja int irá dar erro então vai ir no except
          print("enviado")
        except ValueError:
           print("Houve um problema ao cadastrar o email!")
    else:
       limpar_terminal()
       print("Email inválido, verfique se está certo!")
       print(barra)
       gerenciadorAlunos()
    try:
       cpf_int = int(cpf)
    except ValueError:
        limpar_terminal()
        print("CPF inválido, verifique se alguém já está utilizando ou se foi escrito corretamente")
        print(barra)
        gerenciadorAlunos()
    if(len(cpf)!= 11):#verificar string para ver se o cpf está do tamanho certo
        limpar_terminal()
        print("CPF inválido, verifique se alguém já está utilizando ou se foi escrito corretamente")
        print(barra)
        gerenciadorAlunos()
    try:
       peso_float = float(peso)
    except ValueError:
        limpar_terminal()
        print("Peso inválido, verifique se ele foi escrito corretamente em KG")
        print(barra)
        gerenciadorAlunos()
    try:
       altura_int = int(altura)
    except ValueError:
        limpar_terminal()
        print("Altura inválida, verifique se ela foi escrita corretamente em centímetros")
        print(barra)
        gerenciadorAlunos()
        # verificar se nome ou cpf já está sendo utilizado
    for i in range(len(cadAlunos)):#for para verificar se nenhum nome, email ou cpf já foi cadastrado na academia
        if cadAlunos[i].nome == nome:
            limpar_terminal()
            print("Esse nome já esta sendo utilizado, por favor insira outro. Por favor ")
            print(barra)
            gerenciadorAlunos()
        if cadAlunos[i].cpf == cpf_int:
            limpar_terminal()
            print("CPF inválido, verifique se alguém já está utilizando ou se foi escrito corretamente")
            print(barra)
            gerenciadorAlunos()
        if cadAlunos[i].email == email:
            limpar_terminal()
            print("Esse endereço de e-mail já esta sendo utilizado, por favor insira outro. Por favor ")
            print(barra)
            gerenciadorAlunos()
    alunoNovo = Aluno(nome, cpf_int, peso_float, altura, email) # criar objeto aluno com os dados digitados pelo usuário
    cadAlunos.append(alunoNovo) # cadastra aluno
    treinoAlunos.append([]) # insere um treino vazio
    limpar_terminal()
    print("Cadastro realizado com sucesso! Você será redirecionado para o gerenciador de alunos")
    print(barra)
    gerenciadorAlunos()
#Função para consultar o aluno pelo nome
def consultarAluno():
    limpar_terminal() 
    nome = input("Digite o nome do aluno que você deseja consultar: ")
    nome = nome.upper()
    idAluno = -1
    for i in range(len(cadAlunos)):
      if(nome == cadAlunos[i].nome):
         idAluno = i
    if(idAluno==-1): # Como idAluno por padrão é -1, o for assim irá verificar até encontrar o aluno com nome igual, quando não encontrar o id permanece o mesmo
       limpar_terminal()
       print("Nenhum aluno com esse nome foi encontrado!")
       print(barra)
       gerenciadorAlunos()
    else:
        status = "Ativo" if cadAlunos[idAluno].status else "Inativo" #operador ternário para deixar o valor como ativo ou inativo de acordo com o valor de status
        limpar_terminal()
        if(len(treinoAlunos[idAluno])==0):#caso o aluno nao possua treino cadastrado
           print(f"Id = {idAluno} | Nome = {nome} | CPF = {cadAlunos[idAluno].cpf} | Altura = {cadAlunos[idAluno].altura} | Peso = {cadAlunos[idAluno].peso} | Email = {cadAlunos[idAluno].email} | Status = {status}")
           print("Esse aluno ainda não possui um treino")
        else:#caso o aluno possua treino cadastrado
            print(f"Id = {idAluno} | Nome = {nome} | CPF = {cadAlunos[idAluno].cpf} | Altura = {cadAlunos[idAluno].altura} | Peso = {cadAlunos[idAluno].peso} | Email = {cadAlunos[idAluno].email} | Status = {status}")
            print(f"Exercício | Repetições | Peso")
            for i in range(len(treinoAlunos[idAluno])):
                print(f"{treinoAlunos[idAluno][i].nomeExercicio:^6} | {treinoAlunos[idAluno][i].numRepeticoes:^6} | {treinoAlunos[idAluno][i].pesoExercicio:^6}")
        print(barra)
        gerenciadorAlunos()

def atualizarAluno(): #função para atualizar os dados do aluno
    limpar_terminal()
    if(len(cadAlunos))==0:
       print("Ainda não há alunos cadastrados.")
       print(barra)
       gerenciadorAlunos()
    mostrarAlunosID() #função para mostrar os nomes e ids de todos alunos
    idAtualizar = input("Insira o id do aluno que você deseja atualizar: ")
    try:
       idAtualizar = int(idAtualizar)
    except:
        limpar_terminal()
        print("ID inválido")
        print(barra)
        gerenciadorAlunos()
    if(idAtualizar>len(cadAlunos) or idAtualizar<0):
        limpar_terminal()
        print("ID inválido")
        print(barra)
        gerenciadorAlunos()
    nome = input("Insira o nome do aluno: ")
    nome = nome.upper()
    cpf = input("Inisira o CPF do aluno (sem pontuação): ")
    peso = input("Insira o peso do aluno em quilogramas: ")
    altura = input("Insira a altura do aluno em centímetros: ")
    email = input("Insira o email do aluno: ")
    #Verificar se o formato dos dados é válido, isso inclui a tipagem das variáveis e formatos como peso, altura e cpf:
    if(verificaEmail(email)):
        try:
         print("Enviado")
        except:
           print("Houve um problema ao cadastrar o email! ")
    else:
       limpar_terminal()
       print("Email inválido, verfique se está certo!")
       print(barra)
       gerenciadorAlunos()
    try:
       cpf_int = int(cpf)
    except ValueError:
        limpar_terminal()
        print("CPF inválido, verifique se alguém já está utilizando ou se foi escrito corretamente")
        print(barra)
        gerenciadorAlunos()
    if(len(cpf)!= 11):
        limpar_terminal()
        print("CPF inválido, verifique se alguém já está utilizando ou se foi escrito corretamente")
        print(barra)
        gerenciadorAlunos()
    try:
       peso_float = float(peso)
    except ValueError:
        limpar_terminal()
        print("Peso inválido, verifique se ele foi escrito corretamente em KG")
        print(barra)
        gerenciadorAlunos()
    try:
       altura_int = int(altura)
    except ValueError:
        limpar_terminal()
        print("Altura inválida, verifique se ela foi escrita corretamente em centímetros")
        print(barra)
        gerenciadorAlunos()
    # verificar se nome ou cpf já está sendo utilizado
    for i in range(len(cadAlunos)):
        if(i!= idAtualizar):
            if cadAlunos[i].nome == nome:
                limpar_terminal()
                print("Esse nome já esta sendo utilizado, por favor insira outro. Por favor ")
                print(barra)
                gerenciadorAlunos()
            if cadAlunos[i].cpf == cpf_int:
                limpar_terminal()
                print("CPF inválido, verifique se alguém já está utilizando ou se foi escrito corretamente")
                print(barra)
                gerenciadorAlunos()
            if cadAlunos[i].email == email:
                limpar_terminal()
                print("Esse endereço de e-mail já esta sendo utilizado, por favor insira outro. Por favor ")
                print(barra)
                gerenciadorAlunos()
    #Adicionado os atributos ao objeto caso sejam válidos:
    cadAlunos[idAtualizar].nome = nome
    cadAlunos[idAtualizar].cpf = cpf
    cadAlunos[idAtualizar].peso = peso
    cadAlunos[idAtualizar].altura = altura
    cadAlunos[idAtualizar].email = email
    limpar_terminal()
    print("Atualização feita com sucesso!")
    print(barra)
    gerenciadorAlunos()
#Função para apagar o cadastro de um aluno
def apagarCadAluno():
    limpar_terminal()
    nome = input("Digite o nome do aluno que você deseja apagar o cadastro: ")
    nome = nome.upper()
    idAluno = -1
    for i in range(len(cadAlunos)): 
      if(nome == cadAlunos[i].nome):
         idAluno = i
    if(idAluno==-1): #Primero é feita a busca do nome do aluno, caso não seja encontrado nenhum aluno o idAluno continuará como -1, retornando que nenhum aluno foi encontrado
       limpar_terminal()
       print("Nenhum aluno com esse nome foi encontrado!")
       print(barra)
       gerenciadorAlunos()
    else:
        #verificar se o usuário realmente deseja apagar tudo:
        verificador = input("Deseja mesmo apagar tudo? Digite 1 para apagar e 2 para cancelar: ")
        try:
           verificador = int(verificador)
        except ValueError:
           limpar_terminal()
           print("Opção Inválida!")
           print(barra)
           gerenciadorAlunos()
        if(verificador == 2):
            limpar_terminal()
            print("Ação cancelada!")
            print(barra)
            gerenciadorAlunos()
        elif(verificador == 1):
            limpar_terminal()
            cadAlunos.pop(idAluno)
            treinoAlunos.pop(idAluno)
            print("O aluno foi deletado!")
            print(barra)
            gerenciadorAlunos()
        else:
            limpar_terminal()
            print("Opção inválida!")
            print(barra)
            gerenciadorAlunos()

def gerarRelatorio():
    limpar_terminal()
    print("Selecione se você deseja exibir: \n1 para todos os alunos \n2 para somente os ativos \n3 para somente os inativos")#Verifica o que o usuário quer ver
    opcao = input("> ")
    try:#verifica se o formato de entrada da variável é possível
        opcao = int(opcao)
        ordenados = sorted(cadAlunos, key=lambda x: x.nome) #Cria uma lista, organizando a lista cadAlunos de acordo com a ordem alfabética do atributo nome dos objetos alunos
        if opcao == 1:
            limpar_terminal()
            for i in range(len(ordenados)):#Exibindo todos
                status = "Ativo" if ordenados[i].status else "Inativo"
                print(f"Nome = {ordenados[i].nome} | CPF = {ordenados[i].cpf} | Peso = {ordenados[i].peso} | Altura = {ordenados[i].altura} | Status = {status}")
            print(barra)
            gerenciadorAlunos()
        elif opcao == 2:
            limpar_terminal()
            for i in range(len(ordenados)):
                status = "Ativo" if ordenados[i].status else "Inativo"
                if(ordenados[i].status == True):#condição para exibir somente os com status ativo
                    print(f"Nome = {ordenados[i].nome} | CPF = {ordenados[i].cpf} | Peso = {ordenados[i].peso} | Altura = {ordenados[i].altura} | Status = {status}")
            print(barra)
            gerenciadorAlunos()
        elif opcao == 3: 
            limpar_terminal()
            for i in range(len(ordenados)):
                status = "Ativo" if ordenados[i].status else "Inativo"
                if(ordenados[i].status == False):#condição para exibir somente os com status inativo
                    print(f"Nome = {ordenados[i].nome} | CPF = {ordenados[i].cpf} | Peso = {ordenados[i].peso} | Altura = {ordenados[i].altura} | Status = {status}")
            print(barra)
            gerenciadorAlunos()
        else:#caso seja uma opção fora do "leque" de opções
            limpar_terminal()
            print("Opção Inválida!")
            print(barra)
            gerenciadorAlunos()
    except:
       limpar_terminal()
       print("Valor Inválido!")
       print(barra)
       gerenciadorAlunos()

#função para inserir exercícios
def insereExercicio(idAluno): #recebe como parâmetro o id de um aluno que foi digitado no gerenciador de treino 
    limpar_terminal()
    nome = input("Inisira o nome do exercício: ")
    nome = nome.upper() #deixa nome maiusculo
    rep = input("Inisira a quantidade de repetições: ")        
    peso = input("Insira o peso em KG(caso não seja necessário digite 0): ")
    try:
       peso = int(peso)
    except ValueError:
        limpar_terminal()
        print("Peso inválido")
        print(barra)
        menuPrincipal()
    if(idAluno>len(cadAlunos) or idAluno<0):#verificando se o id existe
       limpar_terminal()
       print("Não há alunos cadastrados com esse ID")
       print(barra)
       menuPrincipal()
    else:
        cont = 0
        for i in range(len(treinoAlunos[idAluno])):
            if(treinoAlunos[idAluno][i].nomeExercicio == nome): # um loop com contador para verificar se há nomes iguais, caso algum nome de treino seja igual vai somar 1
                    cont +=1 
        if(cont==0): #se for igual a 0, ou seja não houve nenhum nome igual no loop anterior ele vai adicionar o exercício
            exer = Exercicio(nome, rep, peso)
            treinoAlunos[idAluno].append(exer)
            cadAlunos[idAluno].status = True
            limpar_terminal()
            print("Exercício adicionado com sucesso!")
            print(barra)
            menuPrincipal()
        else:
           limpar_terminal()
           print("Esse exercício já está cadastrado no treino, você será redirecionado para o gerenciador de treino.")
           print(barra)
           menuPrincipal()
#Função para alterar exercício
def alterarExercicio(idAluno):
    limpar_terminal()
    print("Escolha o exercício que deseja alterar")
    for i in range(len(treinoAlunos[idAluno])): #loop para exibir todos os exercícios de um aluno, 
       print(f"Pressione {i} para alterar {treinoAlunos[idAluno][i].nomeExercicio}")
    print("Pressione -1 para voltar")
    treinoAlterado = input("> ")
    try:#verificar se o valor inserido é válido
       treinoAlterado = int(treinoAlterado)
    except ValueError:
       limpar_terminal()
       print("Opção Inválida!")
       print(barra)
       menuPrincipal()
    if(treinoAlterado>len(treinoAlunos[idAluno]) or treinoAlterado<-1):#se a opção não existir(for um nº maior do que há de exercício ou menor de -1)
        limpar_terminal()
        print("Opção Inválida!")
        print(barra)
        menuPrincipal()
    elif(treinoAlterado==-1):
        limpar_terminal()
        print(barra)
        menuPrincipal()
    nome = input("Inisira o nome do exercício: ")
    nome = nome.upper()
    rep = input("Inisira o número de repetições: ")
    peso = input("Insira o peso em KG(caso não seja necessário digite 0): ")
    try:
       peso = int(peso)
    except ValueError:
        limpar_terminal()
        print("Peso inválido")
        print(barra)
        menuPrincipal()
    treinoAlunos[idAluno][treinoAlterado].nomeExercicio = nome
    treinoAlunos[idAluno][treinoAlterado].numRepeticoes = rep
    treinoAlunos[idAluno][treinoAlterado].pesoExercicio = peso
    limpar_terminal()
    print("Treino alterado com sucesso!")
    print(barra)
    menuPrincipal()
#Função para excluir exercício a partir do id
def excluirExercicio(idAluno):
    limpar_terminal()
    print("Escolha o exercício que deseja excluir")
    for i in range(len(treinoAlunos[idAluno])):#verificar todos os exercícios que um aluno possui
       print(f"Pressione {i} para deletar {treinoAlunos[idAluno][i].nomeExercicio}")
    print("Pressione -1 para voltar")
    treinoAlterado = input("> ")
    try:
       treinoAlterado = int(treinoAlterado)
    except ValueError:
       limpar_terminal()
       print("Valor Inválido!")
       print(barra)
       menuPrincipal()
    if(treinoAlterado>len(treinoAlunos) or treinoAlterado<-1):
       limpar_terminal()
       print("Opção inválida!")
       print(barra)
       menuPrincipal()
    elif(treinoAlterado==-1):
       limpar_terminal()
       print(barra)
       menuPrincipal()
    else:
        treinoAlunos[idAluno].pop(treinoAlterado)#excluir os exercícios do aluno
        if(len(treinoAlunos[idAluno])==0):#caso o número de exercícios restantes seja = a 0, vai deixar o status do usuário como false
           cadAlunos[idAluno].status = False
        limpar_terminal()
        print("O exercício foi excluido com sucesso!")
        print(barra)
        menuPrincipal()
#Função para excluir todos os exercícios de um aluno
def excluirTudo(idAluno):
    verificacao = input("Você deseja mesmo excluir todos os treinos? \nSe sim digite 1, caso contrário digite 2 \n> ")#Verificar se o usuário que excluir tudo
    try:
       verificacao = int(verificacao)
    except:
       limpar_terminal()
       print("Opção Inválida!")
       print(barra)
       menuPrincipal()
    if(verificacao == 2):
       limpar_terminal()
       menuPrincipal()
    elif(verificacao==1):
       treinoAlunos[idAluno] = [] #esvazia a lista
       cadAlunos[idAluno].status = False # torná o status em inativo
       limpar_terminal()
       print("Treino excluído com sucesso!")
       print(barra)
       menuPrincipal()
    else:
       limpar_terminal()
       print("Opção Inválida")
       print(barra)
       menuPrincipal()
#funções para gerenciar alunos e treinos
def gerenciadorAlunos():
  acao = input("Bem-vindo ao gerenciador de alunos \nPressione 1 para adicionar um novo aluno \nPressione 2 para consultar aluno pelo nome \nPressione 3 para atualizar o cadastro de um aluno \nPressione 4 para excluir um aluno \nPressione 5 para gerar um relatório dos alunos \nPressione 6 para voltar para o gerenciador principal\n>")
  try:
    acao = int(acao)
  except ValueError:
    limpar_terminal()
    print("Digite um comando válido")
    print(barra)
    gerenciadorAlunos()
  print(barra)
  #O input da ação vai ser redirecionado para a função que estava informada no texto
  if acao == 1:
    cadastroAluno()
  elif acao == 2:
    consultarAluno()
  elif acao == 3:
    atualizarAluno()
  elif acao == 4:
    apagarCadAluno()
  elif acao == 5:
    gerarRelatorio()
  elif acao ==6:
    limpar_terminal()
    menuPrincipal()
  else:#caso seja um outro valor
     limpar_terminal()
     print("Valor inválido")
     print(barra)
     gerenciadorAlunos()

def gerenciadorTreino():
    mostrarAlunosID()#exibir ids dos alunos
    idAluno = input("Bem vindo ao gerenciador de treinos, primeiramente digite o ID do aluno cujo treino vai ser editado ")#ver o id do aluno que vai ser "editado"
    try:
       idAluno = int(idAluno)
    except ValueError:
       limpar_terminal()
       print("ID inválido")
       print(barra)
       menuPrincipal()
    if(idAluno>len(cadAlunos) or idAluno<0):#verificar se o id do aluno realmente existe
       limpar_terminal()
       print("ID inválido")
       print(barra)
       menuPrincipal()
    limpar_terminal()
    acao = input("Pressione 1 para adicionar um novo exercício \nPressione 2 para alterar um exercício existente \nPressione 3 para excluir um exercício existente \nPressione 4 para apagar todos os exercícios \nPressione 5 para voltar para o menu principal\n>")
    try:#verificar o formato da variável que entrou no input
       acao = int(acao)
    except ValueError:
       limpar_terminal
       print("Digite um comando válido")
       print(barra)
       menuPrincipal()
    print(barra)
    #O input da ação vai ser redirecionado para a função que estava informada no texto
    if acao == 1:
       insereExercicio(idAluno)
    elif acao == 2:
       alterarExercicio(idAluno)
    elif acao == 3:
       excluirExercicio(idAluno)
    elif acao == 4:
       excluirTudo(idAluno)
    elif acao == 5:
       limpar_terminal()
       menuPrincipal()
    else:
     limpar_terminal()
     print("Valor inválido")
     print(barra)
     gerenciadorTreino()
# Função principal da academia
def menuPrincipal():
    acao = input("Bem vindo ao sistema de gerenciamento da Academia da UFFS \nPressione 1 para gerenciar os alunos\nPressione 2 para gerenciar treinos \n> ")
    try:
       acao = int(acao)
    except ValueError:
       limpar_terminal()
       print("Digite um comando válido")
       print(barra)
       menuPrincipal()
    print(barra)
    if acao == 1: #redireciona para o gerenciador de alunos
        limpar_terminal()
        gerenciadorAlunos()
    elif acao == 2: #redireciona para o gerenciador de treino
      limpar_terminal()
      gerenciadorTreino()
    else:
       limpar_terminal()
       print("Digite um comando válido")
       print(barra)
       menuPrincipal()
    
menuPrincipal()