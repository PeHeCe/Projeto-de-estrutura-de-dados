class ListNode:
    def __init__(self, data, nextNode=None, antNode=None):
        self.data = data
        self.nextNode = nextNode
        self.antNode = antNode

class DoublyLinkedListIterator:
    def __init__(self, firstNode=None):
        """Cria uma lista vazia"""
        self.firstNode = firstNode
        self.lastNode = firstNode
        self.iterator = firstNode
        if firstNode:
            self.size = 1
        else:
            self.size = 0

    def addNode(self, data):  # Anexar um Node depois do iterador:
        """Pre condicao: Iterador definido
           Pos condicao: O data eh inserido em um Noh depois do iterador. O iterador fica sobre este Noh
        """
        newNode = ListNode(data, None, None)  # trata a lista vazia
        newNode.nextNode = None
        newNode.antNode = None
        if (self.size == 0):  # trata a lista vazia
            self.iterator = newNode
            self.firstNode = newNode
            self.lastNode = newNode
        elif self.iterator == self.lastNode:  # o iterador está no último elemento
            self.lastNode.nextNode = newNode  # este Noh para a ser agora o último Noh
            newNode.antNode = self.iterator
            self.iterator = newNode
            self.lastNode = newNode  # por o ponteiro lastNode sobre o último Noh
        else:  # o iterador está em algum elemento interno
            newNode.nextNode = self.iterator.nextNode  # novo Noh aponta para o noh seguinte do iterador
            newNode.antNode = self.iterator
            self.iterator.nextNode.antNode = newNode
            self.iterator.nextNode = newNode  # faz o prox do no sob o iterador apontar para o novo no
            self.iterator = newNode  # por o iterador sob o novo no
        self.size += 1  # incrementa o contador e retorna true pois teve sucesso na adicao
        return True

    def insNode(self, data):  # insere um Node antes do iterador
        """Pre condicao: Iterador definido
           Pos condicao: O data eh inserido em um Noh antes do iterador. O iterador fica sobre este Noh.
        """
        newNode = ListNode(data, None, None)  # trata a lista vazia
        newNode.nextNode = None
        if (self.size == 0):  # trata a lista vazia
            self.iterator = newNode
            self.firstNode = newNode
            self.lastNode = newNode
        elif self.iterator == self.firstNode:  # o iterador está no primeiro elemento
            newNode.nextNode = self.firstNode  # o novo Noh aponta para o antigo primeiro Noh
            self.firstNode.antNode = newNode
            self.firstNode = newNode  # firstNode aponta para o novoNoh que passa a ser o primeiro Noh
            self.iterator = newNode  # o iterador fica sob o novoNoh que foi inserido
        else:  # o iterador está em algum elemento interno
            self.iterator.antNode.nextNode = newNode  # o nextNode do anterior ao iterador se torna o novo
            newNode.antNode = self.iterator.antNode  # o anterior ao iterador se torna o antNode do novo
            newNode.nextNode = self.iterator  # o noh iterador se torna o nextNode do novo
            self.iterator.antNode = newNode  # o novo se torna o antNode do noh iterador
            self.iterator = newNode  # o iterador é colocado sob o novo

        self.size += 1  # incrementa o contador e retorna true pois teve sucesso na adicao
        return True

    def elimNode(self):  # elimina o elemento que está sobre o iterador e avanca o iterador para proximo Noh.
        if (self.iterator == self.firstNode):  # iterador sobre o primeiro elemento
            if (self.lastNode == self.firstNode):  # tem so um Noh
                self.lastNode = None  # aponta para nada
                self.firstNode = None
                self.iterator = None
            else:  # tem mais de um Node
                self.firstNode = self.firstNode.nextNode  # firstNode aponta para o proximo noh que passa a ser o primeiro
                self.iterator.nextNode.antNode = None  # apaga o antNode do proximo Noh e ele passa a ser o primeiro
                self.iterator.nextNode = None  # isola o Noh
                self.iterator = self.firstNode  # avanca para o proximo Noh
        else:  # iterator pode estar sob o ultimo ou um elemento interno
            if self.iterator == self.lastNode:  # o iterador esta sob o ultimo:
                self.lastNode = self.iterator.antNode  # coloca o noh anterior ao iterador como lastNode
                self.iterator.antNode = None  # isola o noh
                self.lastNode.nextNode = None  # isola o noh
                self.iterator = None  # o iterador nao aponta mais para um elemento da lista
            else:  # iterador sobre elemento intermediario
                self.iterator.antNode.nextNode = self.iterator.nextNode  # o nextNode do anterior recebe o nextNodedo noh atual
                self.iterator.nextNode.antNode = self.iterator.antNode  # o antNode do próximo recebe o antNode do noh atual
                nohAnterior = self.iterator.antNode  # guarda o noh anterior
                self.iterator.nextNode = None  # isola o noh
                self.iterator.antNode = None  # isola o noh
                self.iterator = nohAnterior  # coloca o iterador no noh anterior

        self.size = self.size - 1  # decrementa o tamanho da lista
        return True

    def first_Node(self):  # coloca o iterador sobre o primeiro Node da Lista
        self.iterator = self.firstNode
        return True

    def last_Node(self):  # coloca o iterador sobre o útlimo Node da Lista
        self.iterator = self.lastNode
        return True

    def nextNode(self):  # avança o iterador uma posição. para tal o iterador deve estar definido(sobre um Noh)
        if (self.iterator):
            self.iterator = self.iterator.nextNode
        return True

    def antNode(self):
        if (self.iterator):
            self.iterator = self.iterator.antNode
        return True

    def posNode(self, position):  # coloca o iterador sobre a posição position
        """o iterador eh posto sobre o Nod da posicao que vai de 1 ate size.
           qualquer outro valor leva o iterador a ficar indefinido(None)
           Return True para posicao valida e False para iterador indefinido
        """
        if (position > 0 and position <= self.size):
            i = 1
            self.iterator = self.firstNode  # poe o iterador sob o primeiro Node
            while (i < position):
                if (self.iterator.nextNode != None):
                    self.iterator = self.iterator.nextNode
                    i = i + 1
            return True
        else:
            if position <= 0:
                self.iterator = self.firstNode
                return True
            if position > self.size:
                self.iterator = self.lastNode
                return True

    def isUndefinedIterator(self):  # retorna verdadeiro se o iterador estiver indefinido
        if (self.iterator == None):
            return True
        else:
            return False

    def printNode(self):
        curr = self.firstNode
        while curr:
            print(curr.data)
            curr = curr.nextNode
