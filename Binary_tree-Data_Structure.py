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
        if self.root == None: # checa se o valor da raiz é nulo
            self.root = novo #caso comporve-se, o novo valor é atribuído a raiz
        else: # se nao for a raiz
            atual = self.root #atual recebe o valor da raiz
            while True:
                anterior = atual #anterior recebe o valor atual, que é o valor da raiz
                if v <= atual.item: # ir para esquerda
                    atual = atual.esq # atribui o valor atual como sendo o nó a esquerda
                    if atual == None: # se o atual(que recebeu o valor atual.esq) for vazio
                        anterior.esq = novo #então atribua o valor novo ao valor anterior esquerdo 
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
            self.inOrder(atual.esq)  # se existir será exibido
            print(atual.item,end=" ")# No central sempre existirá
            self.inOrder(atual.dir) # se existir será exibido
  

    def encaminhar(self):
        print(" Exibindo em ordem: ",end="")
        self.inOrder(self.root)
        print('')


def first():
    dados['Nome'] = str(input('Informe o nome do paciente: '))
    dados['Idade'] = int(input('Informe a idade do paciente(somente números): '))
    dados['Cadastro'] = int(input('Qual o número de cadastro do paciente?: '))
    dados['Sintomas'] = str(input('Quais os sintomas que o paciente apresenta?: '))
    pacientes.append(dados.copy())
    arv.inserir(dados['Cadastro'])
    os.system('cls') 


def second():
    print(f'Ao todo temos {len(pacientes)} paciente(s) cadastrados no sistema')
    sec_pes = int(input('Caso deseje verificar os dados do último paciente cadastrado, digite a matricula dele: '))	
    if arv.buscar(sec_pes):
        print('Paciente Encontrado!')
        sint= input('Deseja verificar a ficha do paciente ? [S/N]')
        if sint in 'Ss':
            print(dados)
        else:
            print('Opção Negada ! Entre com a nova operação')
    else:
        os.system('cls')
        print(' Paciente nao encontrado!') 

def third():
    for e in pacientes:
        for k, v in e.items():
            print(f' {k}  {v}')


     
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
        third()
    elif opcao == 4:
        break 
