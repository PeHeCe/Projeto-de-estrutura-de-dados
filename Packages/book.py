from datetime import *
from arrayStack import *
from arrayQueue import *

class Book:
    
    def __init__(self, title:str, author:str, publication_year:int, copies:int=1, loaned_copies:int=0):
        """Criar um novo livro"""
        self.title = title.upper()
        self.author = author
        self.publication_year = publication_year
        self.copies_number = copies
        self.loaned_copies = loaned_copies
        self.loan_history = ArrayStack()
        self.reservation_queue = ArrayQueue()

    
    # Testar se o cliente tem algum emprestimo com devolucao pendente
    def client_has_pending_loan(self, client_id):
        suport_list = []  # cria uma lista suporte
        while not self.loan_history.is_empty():  # enquanto a pilha de historico nao estiver vazia 
            if self.loan_history.top().get('client_id') != client_id:  # nome do cliente do topo da pilha eh diferente do nome do cliente querendo devolver a copia
                suport_list.append(self.loan_history.pop())  # desempilha o dicionario do topo dentro da lista suporte
                continue
            break

        if self.loan_history.is_empty() or self.loan_history.top().get('return_date') != None:  # cliente nao tem devolucoes pendentes
            for item in reversed(suport_list):  # refaz a pilha do jeito que era antes do teste
                self.loan_history.push(item)
            return False
        
        for item in reversed(suport_list):  # refaz a pilha do jeito que era antes do teste
            self.loan_history.push(item)
        
        return True  # cliente tem emprestimos com devolucao pendente


    # Devolver livro
    def return_copy(self, client_id):
        support_list = []  # cria uma lista supporte
        while not self.loan_history.is_empty():  # enquanto a pilha de historico nao estiver vazia 
            if self.loan_history.top().get('client_id') != client_id:  # id do cliente do topo da pilha eh diferente do nome do cliente querendo devolver a copia
                support_list.append(self.loan_history.pop())  # desempilha o dicionario do topo dentro da lista supporte
                continue  # pula o comando break e refaz a condicao
            break

        if self.loan_history.is_empty():  # o cliente nao tem emprestimos registrados
            for item in reversed(support_list):  # refaz a pilha do jeito que era antes da modificacao
                self.loan_history.push(item)

            print('Nao ha emprestimos nesse nome')
            return False
        
        # Modifica o dicionario para receber o dia atual como data de devolucao do livro
        support_list.append(self.loan_history.pop())
        support_list[-1]['return_date'] = datetime.now().strftime('%d/%m/%Y')
        self.loan_history.push(support_list[-1])
        support_list.pop()

        for item in reversed(support_list):  # refaz a pilha do jeito que era antes da modificacao
            self.loan_history.push(item)

        # Diminui o número de livros emprestados em 1
        self.loaned_copies -= 1

        return True

    # Adicionar reserva ao livro
    def add_reservation(self, client):
        self.reservation_queue.enqueue({'client_id': client.id, 'client_name': client.name})  # Adiciona a reserva no final da fila

        print(f"Cliente {client.name} adicionado à fila de reserva do livro {self.title}")


    # Cancelar uma reserva
    def cancel_reservation(self, client_id):
        support_list = []  # cria uma lista supporte
        while not self.reservation_queue.is_empty():  # enquanto a fila de reserva nao estiver vazia 
            if self.reservation_queue.first().get('client_id') != client_id:  # id do cliente na frente da fila eh diferente do id do cliente querendo cancelar a reserva
                support_list.append(self.reservation_queue.dequeue())  # tira o dicionario da frente da fila e coloca dentro da lista suporte
                continue  # pula o comando break e refaz a condicao
            break

        if self.reservation_queue.is_empty():  # o cliente nao tem emprestimos registrados
            for item in support_list:  # refaz a fila do jeito que era antes da modificacao
                self.reservation_queue.enqueue(item)

            print('Nao ha reservas nesse nome')
            return False

        self.reservation_queue.dequeue()  # Retira o cliente da fila de reserva

        # refaz a fila do jeito que era antes da modificacao
        while not self.reservation_queue.is_empty(): 
            support_list.append(self.reservation_queue.dequeue())
        for item in support_list:
            self.reservation_queue.enqueue(item)

    # Ver todas informações de um livro específico
    def print_info(self):
        print(f"Título: {self.title}")
        print(f"Autor: {self.author}, {self.publication_year}")
        print(f"Cópias: {self.copies_number}, {self.loaned_copies} emprestados")

    # Ver o historico inteiro de emprestimos do livro
    def print_history(self):
        support_stack = ArrayStack()  # Criação da pilha de apoio

        # Percorre a pilha de histórico, exibe cada elemento e o coloca na pilha de apoio
        while not self.loan_history.is_empty():
            print(f"\tCliente: {self.loan_history.top().get('client_id')}, Data: {self.loan_history.top().get('loan_date')}, Data Retorno: {self.loan_history.top().get('return_date')}")
            support_stack.push(self.loan_history.pop())

        # Retorna os elementos da pilha de apoio para a pilha original
        while not support_stack.is_empty():
            self.loan_history.push(support_stack.pop())

    # Ver a fila de reserva inteira do livro
    def print_reservation_queue(self):
        support_queue = ArrayQueue()  # Criação da fila de apoio
        posicao = 1  # Cria o contador de posições

        # Percorre a fila
        while not self.reservation_queue.is_empty():
            print(f"\t{posicao}º: {self.reservation_queue.first().get("client_name")}")  # Exibe as reservas da fila com sua posição
            support_queue.enqueue(self.reservation_queue.dequeue())  # Insere o elemento na fila de apoio
            posicao += 1  # Incrementa o contador de posição

        #  Retorna os elementos da fila de apoio para a fila original
        while not support_queue.is_empty():
            self.reservation_queue.enqueue(support_queue.dequeue())
