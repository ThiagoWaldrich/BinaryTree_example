# Importante incluir o tratamento de erros. O sistema é voltado para profissionais da saúde, uma vez que eles não saibam lidar com 
# os sistemas, torna-se necessários


from tabulate import tabulate
import os 

class Node: #Importante para definir um nó
     
    def __init__(self,key): 
        self.item = key 
        self.dir = None 
        self.esq = None 

class Tree:

    def __init__(self):
        self.root = None #define a raiz

    def inserir(self, v):
        novo = Node(v) # cria um novo Nó
        if self.root == None:
            self.root = novo
        else: # se nao for a raiz
            atual = self.root
            while True:
                anterior = atual
                if v <= atual.item: # ir para esquerda
                    atual = atual.esq
                    if atual == None:
                        anterior.esq = novo
                        return
                else: # ir para direita
                    atual = atual.dir
                    if atual == None:
                        anterior.dir = novo
                        return

    def buscar(self, chave):
        if self.root == None:
            return None # se arvore vazia
        atual = self.root # começa a procurar desde raiz
        while atual.item != chave: # enquanto nao encontrou
            if chave < atual.item:
                atual = atual.esq # caminha para esquerda
            else:
                atual = atual.dir # caminha para direita
            if atual == None:
                return None 
        return atual  # terminou o laço while e chegou aqui é pq encontrou item    
  
    def inOrder(self, atual):
        if atual != None:
            self.inOrder(atual.esq)
            print(atual.item,end=" ")
            self.inOrder(atual.dir)
  

    def encaminhar(self):
        print(" Exibindo em ordem: ",end="")
        self.inOrder(self.root)
        print('')


def first():
    nome = input('Insira seu nome completo: ')
    telefone = int(input('Insira seu número de contato: '))
    rg = int(input('Insira seu RG: ').strip())
    gênero = input('Insira seu gênero(masculino, feminino, prefiro não declarar): ')
    pacientes.append(dados.copy())
    arv.inserir(rg)
    os.system('cls') 
    dados[rg] = {
        'nome': nome,
        'telefone': telefone,
        'rg': rg,
        'gênero': gênero
        }


def second():
    print(f'Ao todo temos {len(pacientes)} paciente(s) cadastrados no sistema')
    rg = int(input('Qual o número de cadastro do paciente que você deseja encontrar?: '))	
    if arv.buscar(rg) != None:
        print('Paciente Encontrado!')
        sint= input('Deseja verificar os sintomas dos pacientes cadastrados ? [S/N]')
        if sint in 'Ss':
            print(dados[rg])
        else:
            print('Opção Negada ! Entre com a nova operação')
    else:
        os.system('cls')
        print(' Paciente não encontrado!') 

def third():
    print(dados)

def mostra_pacientes(pacientes,chaves):
    table = []
    for arv.buscar() in chaves:
        table.append([
            pacientes[chave]['nome'],
            pacientes[chave]['telefone'],
            pacientes[chave]['RG'],
            pacientes[chave]['gênero']
        ])

        print(tabulate(table))


     
arv = Tree()
print('_'*30)
print('UNIDADE DE PRONTO ATENDIMENTO')
opcao = 0
dados = dict()
pacientes = []
while True:
    print('')
    print('***********************************')
    print('Entre com a opcao:')
    print(' --- 1: Inserir Cadastro')
    print(' --- 2: Pesquisar Paciente')
    print(' --- 3: Exibir todos os nºs de cadastro')
    print(' --- 4: Sair do programa')
    print("***********************************")
    opcao = int(input())
    if opcao == 1:
        first()
    elif opcao == 2:
        second() 
    elif opcao == 3:
        arv.encaminhar()
       # third()
        mostra_pacientes(pacientes,)
    elif opcao == 4:
        break

    
    """
    



    
    
    
    
    
    
    
    
    """