from datetime import *
from doublyLinkedList import *
from arrayQueue import *
from arrayStack import *
from book import *
from client import *

class Library:

    def __init__(self):
        self.clients = []
        self.books = DoublyLinkedListIterator()


    # Recuperar o objeto livro utilizando seu nome
    def get_book_object_by_name(self, nome):
        self.books.first_Node()  # Poe o iterador de books no primeiro noh

        while not self.books.isUndefinedIterator():  # enquanto ainda estiver iterador

            if self.books.iterator.data.title == nome.upper():  # o nome do livro é igual ao nome passado
                return self.books.iterator.data  # retorna o objeto livro dentro da lista duplamente encadeada
            
            self.books.nextNode()  # enquanto o nome for diferente do nome passado, passa o noh
        
        self.books.last_Node()
        return None  # Se o nome passado não estiver na lista


    # Recuperar o objeto cliente utilizando seu id
    def get_client_object_by_id(self, client_id):
        clients_with_id = list(filter(lambda client: client.id == client_id, self.clients))  # filtra os clientes em uma lista, que vai ter somente o cliente com o id passado

        if len(clients_with_id) == 0:  # se o cliente com o id passado não existir na lista
            return None
        
        return clients_with_id[0]  # se o id passado existir na lista
    

    # Adicionar cliente ao sistema
    def add_client(self, client_name):
        print(f'Cliente {client_name}, de id: {len(self.clients) + 1}')
        self.clients.append(Client(len(self.clients) + 1, client_name))  # instancia e adiciona um objeto cliente na lista de clientes da 


    # Adicionar livro ao sistema
    def add_book(self, title, author, publication_year, copies=1):
        # Retorna o objeto livro pelo seu titulo
        book = self.get_book_object_by_name(title)

        if book is not None:  # Caso o livro exista:
            print('O livro ja existe no catalogo')
            while True:
                adicionarCopia = input('Digite "s" se quiser adicionar mais copias ').upper()
                if adicionarCopia == 'S':
                    book.copies_number += copies  # Incrementa a quantidade de cópias
                    break
                break
            return None
            
        self.books.addNode(Book(title, author, publication_year, copies))  # instancia e adiciona um objeto livro na lista de livros da biblioteca
        print(f'O livro {title} foi adicionado ao catalogo')


    # Emprestar a copia de um livro
    def loan_book_copy(self, client_id, book_title, loan_date=datetime.now().strftime('%d/%m/%Y'), return_date=None):

        client = self.get_client_object_by_id(client_id)  # recebe o objeto cliente
        book = self.get_book_object_by_name(book_title)  # recebe o objeto livro

        if client is None:  # se o cliente passado não existir no sistema
            print('Esse cliente nao existe no sistema')
            return None
        if book is None:  # se o livro passado não existir no sistema
            print('Esse livro nao existe no sistema')
            return None

        if not book.client_has_pending_loan(client.id) and book.loaned_copies < book.copies_number:  # cliente nao tem emprestimos com devolucao pendentes e tem copias disponiveis para emprestimo
            book.loan_history.push({'client_id': client.id, 'loan_date': loan_date, 'return_date': return_date})  # adiciona o emprestimo na pilha de historico do livro emprestado
            book.loaned_copies += 1  # Adiciona uma copia para o numero de copias emprestadas

            # Caso a fila de reservas não esteja vazia e o cliente seja o primeiro da fila, ele é retirado dela
            if not book.reservation_queue.is_empty():
                if book.reservation_queue.first().get('client_id') == client_id:
                    book.reservation_queue.dequeue()

            print(f"{book.title} emprestado para {client.name}")
            return True
        
        if book.client_has_pending_loan(client.id):  # se o cliente tem emprestimo pendente
            print(f'O cliente {client.name} já está com esse livro emprestado')
            return None
        
        print(f'Nao ha copias disponiveis, adicionando {client.name} a fila de espera')  # se o cliente pode pegar o livro emprestado porém não ha copias disponiveis
        book.reservation_queue.enqueue({'client_id': client.id, 'client_name': client.name})
        return True

    # Devolver a copia de um livro
    def return_book_copy(self, client_id, book_title):
        client = self.get_client_object_by_id(client_id)  # recebe o objeto cliente
        book = self.get_book_object_by_name(book_title)  # recebe o objeto livro

        if client is None:  # se o cliente passado não existir no sistema
            print('Esse cliente nao existe no sistema')
            return None
        if book is None:  # se o livro passado não existir no sistema
            print(f'O livro {book_title} nao existe no sistema')
            return None
        
        if book.client_has_pending_loan(client_id):  # se o cliente tem um emprestimo pendente
            book.return_copy(client.id)  # modifica a pilha com o historico de emprestimos do livro, recebendo a data de devolucao
            print(f'{book.title} devolvido por {client.name}')
            # Caso o livro possua pelo menos uma reserva, notifica quem está na primeira posição da fila
            if not book.reservation_queue.is_empty():
                print(f"O cliente {book.reservation_queue.first().get("client_name")} é o próximo na fila de reservas deste livro")
            return True
        
        print('Esse cliente não tem nenhum emprestimo pendente')  # se o cliente nao tem emprestimo pendente
        return None

    # Adicionar um cliente a fila de reservas de um livro
    def add_reservation(self, client_id, book_title):
        client = self.get_client_object_by_id(client_id)  # recebe o objeto cliente
        book = self.get_book_object_by_name(book_title)  # recebe o objeto livro

        if client is None:  # se o cliente passado não existir no sistema
            print('Esse cliente nao existe no sistema')
            return None
        if book is None:  # se o livro passado não existir no sistema
            print(f'O livro {book_title} nao existe no sistema')
            return None

        book.add_reservation(client)

    # Cancelar uma reserva de livro
    def cancel_reservation(self, client_id, book_title):
        client = self.get_client_object_by_id(client_id)  # recebe o objeto cliente
        book = self.get_book_object_by_name(book_title)  # recebe o objeto livro

        if client is None:  # se o cliente passado não existir no sistema
            print('Esse cliente nao existe no sistema')
            return None
        if book is None:  # se o livro passado não existir no sistema
            print(f'O livro {book_title} nao existe no sistema')
            return None
        
        book.cancel_reservation(client.id)  # modifica a fila de reserva do livro, retirando a reserva do cliente passado

        print(f'Reserva do livro {book.title} de {client.name} cancelada')


    # Ver todas informações de um livro específico
    def print_book_info(self, book_title):
        book = self.get_book_object_by_name(book_title)  # recebe o objeto livro

        if book is not None: # Verifica se o livro que foi passado existe no sistema
            book.print_info() # Chama a função da classe Book


    # Ver a pilha de historico de emprestimos de um livro
    def print_book_history(self, book_title):
        book = self.get_book_object_by_name(book_title)  # recebe o objeto livro

        if book is not None:  # se o livro passado existir no sistema
            book.print_history()


    # Ver a fila de reserva de emprestimos de um livro
    def print_book_reservation(self, book_title):
        book = self.get_book_object_by_name(book_title)  # recebe o objeto livro

        if book is not None:  # se o livro passado existir no sistema
            book.print_reservation_queue()
