from sys import path
path.append('Packages')
from datetime import *
from doublyLinkedList import *
from arrayStack import *
from arrayQueue import *
from book import *
from library import *


def __main__():
    biblioteca = Library()

    biblioteca.add_client('Vitor')
    biblioteca.add_client('Pedro')
    biblioteca.add_client('Caio')
    biblioteca.add_client('Saulo')
    biblioteca.add_client('Filipe')
    biblioteca.add_client('Mateus')
    biblioteca.add_client('Rakel')
    biblioteca.add_client('Alan')
    biblioteca.add_client('Lucas')
    biblioteca.add_client('Bruna')
    biblioteca.add_client('Ana')
    biblioteca.add_client('Laura')
    biblioteca.add_client('Fernanda')
    biblioteca.add_client('Maria')
    biblioteca.add_client('João')
    biblioteca.add_client('Elder')
    biblioteca.add_client('Carlos')
    biblioteca.add_client('Rafael')
    biblioteca.add_client('Felipe')
    biblioteca.add_client('Guilherme')
    biblioteca.add_client('José')

    # MVP
    # adicionando livros à biblioteca
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for letra in alfabeto:
        for i in range(10):
            biblioteca.add_book(f'livro {letra}{i+1}', f'autor {i+1}', 2000+i, 10)

    biblioteca.add_book('A arte da guerra', 'Sun Tzu', -500)
    biblioteca.add_book('Harry Potter e a Pedra Filosofal', 'J.K. Rowling', 1997)
    biblioteca.add_book('O Senhor dos Aneis', 'J.R.R. Tolkien', 1955)
    biblioteca.add_book('Dom Quixote', 'Miguel de Cervantes', 1605)
    biblioteca.add_book('A Revolucao dos Bichos', 'George Orwell', 1945)
    biblioteca.add_book('O Pequeno Principe', 'Antoine de Saint-Exupéry', 1943)
    biblioteca.add_book('Grande Sertao: Veredas', 'Guimarães Rosa', 1956)
    biblioteca.add_book('Memorias Postumas de Bras Cubas', 'Machado de Assis', 1881)
    biblioteca.add_book('Capitaes da Areia', 'Jorge Amado', 1937)
    biblioteca.add_book('Vidas Secas', 'Graciliano Ramos', 1938)
    biblioteca.add_book('O Principe', 'Nicolau Maquiavel', 1532)
    biblioteca.add_book('O Leao, a Feiticeira e o Guarda-Roupa', 'C.S. Lewis', 1950)

    #adicionando 30 livros com 10 pessoas na fila de espera de cada livro.
    emprestados = 'ABC'
    for letra in emprestados:
        for livro in range(6):
            for cliente in range(10):
                id_cliente = cliente + 1
                titulo = f'livro {letra}{livro + 1}'
                biblioteca.add_reservation(id_cliente, titulo)

    for i in range(10):
        id_cliente = i + 1
        biblioteca.add_reservation(id_cliente, 'A arte da guerra')
        biblioteca.add_reservation(id_cliente, 'Harry Potter e a Pedra Filosofal')
        biblioteca.add_reservation(id_cliente, 'O Senhor dos Aneis')
        biblioteca.add_reservation(id_cliente, 'Dom Quixote')
        biblioteca.add_reservation(id_cliente, 'A Revolucao dos Bichos')
        biblioteca.add_reservation(id_cliente, 'O Pequeno Principe')
        biblioteca.add_reservation(id_cliente, 'Grande Sertao: Veredas')
        biblioteca.add_reservation(id_cliente, 'Memorias Postumas de Bras Cubas')
        biblioteca.add_reservation(id_cliente, 'Capitaes da Areia')
        biblioteca.add_reservation(id_cliente, 'Vidas Secas')
        biblioteca.add_reservation(id_cliente, 'O Principe')
        biblioteca.add_reservation(id_cliente, 'O Leao, a Feiticeira e o Guarda-Roupa')

    # Simulando notificação de 5 reservas do mesmo livro
    print("")
    biblioteca.loan_book_copy(20, "A arte da guerra")
    biblioteca.return_book_copy(20, "A arte da guerra")
    for i in range(1, 6):
        biblioteca.loan_book_copy(i, "A arte da guerra")
        biblioteca.return_book_copy(i, "A arte da guerra")

    # Simulando notificação de 5 reservas do mesmo livro
    print("")
    biblioteca.loan_book_copy(20, "Harry Potter e a Pedra Filosofal")
    biblioteca.return_book_copy(20, "Harry Potter e a Pedra Filosofal")
    for i in range(1, 6):
        biblioteca.loan_book_copy(i, "Harry Potter e a Pedra Filosofal")
        biblioteca.return_book_copy(i, "Harry Potter e a Pedra Filosofal")

    # Simulando notificação de 1 reserva de 10 livros diferentes
    print("")
    biblioteca.loan_book_copy(20, "O Senhor dos Aneis")
    biblioteca.return_book_copy(20, "O Senhor dos Aneis")
    biblioteca.loan_book_copy(1, "O Senhor dos Aneis")
    biblioteca.return_book_copy(1, "O Senhor dos Aneis")

    print("")
    biblioteca.loan_book_copy(20, "Dom Quixote")
    biblioteca.return_book_copy(20, "Dom Quixote")
    biblioteca.loan_book_copy(1, "Dom Quixote")
    biblioteca.return_book_copy(1, "Dom Quixote")

    print("")
    biblioteca.loan_book_copy(20, "A Revolucao dos Bichos")
    biblioteca.return_book_copy(20, "A Revolucao dos Bichos")
    biblioteca.loan_book_copy(1, "A Revolucao dos Bichos")
    biblioteca.return_book_copy(1, "A Revolucao dos Bichos")

    print("")
    biblioteca.loan_book_copy(20, "O Pequeno Principe")
    biblioteca.return_book_copy(20, "O Pequeno Principe")
    biblioteca.loan_book_copy(1, "O Pequeno Principe")
    biblioteca.return_book_copy(1, "O Pequeno Principe")

    print("")
    biblioteca.loan_book_copy(20, "Grande Sertao: Veredas")
    biblioteca.return_book_copy(20, "Grande Sertao: Veredas")
    biblioteca.loan_book_copy(1, "Grande Sertao: Veredas")
    biblioteca.return_book_copy(1, "Grande Sertao: Veredas")

    print("")
    biblioteca.loan_book_copy(20, "Memorias Postumas de Bras Cubas")
    biblioteca.return_book_copy(20, "Memorias Postumas de Bras Cubas")
    biblioteca.loan_book_copy(1, "Memorias Postumas de Bras Cubas")
    biblioteca.return_book_copy(1, "Memorias Postumas de Bras Cubas")

    print("")
    biblioteca.loan_book_copy(20, "Capitaes da Areia")
    biblioteca.return_book_copy(20, "Capitaes da Areia")
    biblioteca.loan_book_copy(1, "Capitaes da Areia")
    biblioteca.return_book_copy(1, "Capitaes da Areia")

    print("")
    biblioteca.loan_book_copy(20, "Vidas Secas")
    biblioteca.return_book_copy(20, "Vidas Secas")
    biblioteca.loan_book_copy(1, "Vidas Secas")
    biblioteca.return_book_copy(1, "Vidas Secas")

    print("")
    biblioteca.loan_book_copy(20, "O Principe")
    biblioteca.return_book_copy(20, "O Principe")
    biblioteca.loan_book_copy(1, "O Principe")
    biblioteca.return_book_copy(1, "O Principe")

    print("")
    biblioteca.loan_book_copy(20, "O Leao, a Feiticeira e o Guarda-Roupa")
    biblioteca.return_book_copy(20, "O Leao, a Feiticeira e o Guarda-Roupa")
    biblioteca.loan_book_copy(1, "O Leao, a Feiticeira e o Guarda-Roupa")
    biblioteca.return_book_copy(1, "O Leao, a Feiticeira e o Guarda-Roupa")


    # Interface do sistema
    print("\nBem vindo ao gerenciamento de Biblioteca! ")

    while True:
        #opções de escolha do usuário
        print('\n\tA: Adicionar novo cliente')
        print('\tL: Cadastrar novo livro')
        print("\tE: Emprestar livro")
        print("\tD: Devolver Livro")
        print("\tR: Adicionar em fila de reservas de um livro")
        print("\tC: Cancelar reserva de um livro")
        print("\tB: Buscar livro")
        print("\tF: Ver a fila de reservas de um livro")
        print("\tH: Ver histórico de um livro")
        print("\tX: Sair do programa")

        operacao = input("Selecione a operação que deseja: ").upper()  # Entrada da operação que o usuario deseja efetuar

        # Verifica qual foi a operação que o usuário digitou e a executa
        match operacao:
            case "A":
                nomeCliente = input("Qual o nome do cliente? ")

                biblioteca.add_client(nomeCliente)  # Executa o método de adicionar cliente
            case "L":
                nomeLivro = input("Qual o nome do livro? ")
                autorLivro = input("Qual é o nome do autor? ")
                anoLivro = input("Em que ano o livro foi publicado? ")
                while True:  # Recebe a quantidade de cópias do livro, se não for um número, pergunta novamente
                    try:
                        copias = int(input("Quantas cópias foram recebidas? "))
                    except ValueError:
                        continue
                    break

                biblioteca.add_book(nomeLivro, autorLivro, anoLivro, copias)  # Executa o método de adicionar livro
            case "E":
                nomeLivro = input("Qual livro será emprestado? ")
                while True:  # Recebe o id do cliente, se não for um número, pergunta novamente
                    try:
                        idPessoa = int(input("Para qual id de cliente o livro será emprestado? "))
                    except ValueError:
                        continue
                    break

                biblioteca.loan_book_copy(idPessoa, nomeLivro)  # Executa o método de emprestar um livro para um cliente
            case "D":
                nomeLivro = input("Qual livro está sendo devolvido? ")
                while True:  # Recebe o id do cliente, se não for um número, pergunta novamente
                    try:
                        idPessoa = int(input("Qual o id de quem está devolvendo? "))
                    except ValueError:
                        continue
                    break

                biblioteca.return_book_copy(idPessoa, nomeLivro)  # Executa o método de devolver um livro emprestado
            case "R":
                nomeLivro = input("Adicionar reserva de qual livro? ")
                while True:  # Recebe o id do cliente, se não for um número, pergunta novamente
                    try:
                        idPessoa = int(input("Qual o id do cliente que está reservando? "))
                    except ValueError:
                        continue
                    break

                biblioteca.add_reservation(idPessoa, nomeLivro)  # Executa o método de adicionar reserva
            case "C":
                nomeLivro = input("De qual livro será cancelada a reserva? ")
                while True:  # Recebe o id do cliente, se não for um número, pergunta novamente
                    try:
                        idPessoa = int(input("Qual o id de quem está cancelando? "))
                    except ValueError:
                        continue
                    break

                biblioteca.cancel_reservation(idPessoa, nomeLivro)  # Executa o método de cancelar reserva
            case "B":
                nomeLivro = input("Deseja buscar informações de qual livro? ")

                biblioteca.print_book_info(nomeLivro)  # Executa o método de imprimir as informações do livro
            case "H":
                nomeLivro = input("Deseja ver o histórico de qual livro? ")

                biblioteca.print_book_history(nomeLivro)  # Executa o método de imprimir o histórico do livro
            case "F":
                nomeLivro = input("Deseja ver a fila de reservas de qual livro? ")

                biblioteca.print_book_reservation(nomeLivro)  # Executa o método de imprimir a fila de reservas do livro
            case "X":
                quit()  # Finaliza o programa


if __name__ == '__main__':
    __main__()
