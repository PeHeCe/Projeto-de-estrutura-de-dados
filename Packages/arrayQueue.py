class ArrayQueue:
    """Implementação de fila FIFO usando uma lista Python como armazenamento subjacente."""
    DEFAULT_CAPACITY = 30          # capacidade moderada para todas as novas filas

    def __init__(self):
        """Cria uma fila vazia."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._first = -1
        self._last = -1

    def __len__(self):
        """Retorna o número de elementos na fila."""
        return self._size

    def is_empty(self):
        """Retorna True se a fila estiver vazia."""
        return self._size == 0

    def first(self):
        # Retorna (mas não remove) o elemento na frente da fila. Mostra uma exceção de vazia se a fila estiver vazia.
        if self.is_empty():
            print('fila vazia')
            return None
        else:
            return self._data[self._first]

    def dequeue(self): #desenfileirar
        """Remove e retorna o primeiro elemento da fila (ou seja, FIFO).

        Mostra uma exceção de vazia se a fila estiver vazia.
        """
        if self.is_empty():
            print('fila vazia')
            return None  #raise Empty('Queue is empty')
        else:
            answer = self._data[self._first]
            self._data[self._first] = None         # ajudar na coleta de lixo
            if(self._first == self._last):
                self._first = -1
                self._last = -1
            else:
                self._first = (self._first + 1) % len(self._data)
            self._size -= 1
            return answer

    def enqueue(self, e): # enfileirar
        """Adiciona um elemento no final da fila."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))     # dobrar o tamanho do array
        if(self._size == 0):  # fila vazia
            self._data[0] = e
            self._first = 0 # o primeiro elemento está na posição zero
            self._last = 0  # o último elemento está na posição zero
        else:
            self._last = (self._last + 1) % len(self._data) # determina a nova posição do último elemento
            self._data[self._last] = e  # adiciona e como último elemento na fila
        self._size += 1

    def _resize(self, cap):                  # assumimos cap >= len(self)
        """Redimensionar para uma nova capacidade >= len(self)."""
        old = self._data                       # manter o controle da lista existente
        self._data = [None] * cap              # alocar lista com nova capacidade
        walk = self._first
        for k in range(self._size):            # considerar apenas elementos existentes
            self._data[k] = old[walk]            # deslocar intencionalmente os índices
            walk = (1 + walk) % len(old)         # usar o tamanho antigo como módulo
        self._first = 0                        # frente foi realinhada
