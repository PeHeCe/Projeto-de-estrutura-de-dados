class Empty(Exception):
    def __init__(self, valor):
      self.valor = valor

    def __str__(self):
      return repr(self.valor)

class ArrayStack:
  """Implementação de Pilha LIFO usando uma lista Python como armazenamento subjacente."""

  def __init__(self):
      """Cria uma pilha vazia."""
      self._data = []                       # instância de lista não pública

  def __len__(self):
      """Retorna o número de elementos na pilha."""
      return len(self._data)

  def is_empty(self):
      """Retorna True se a pilha estiver vazia."""
      return len(self._data) == 0

  def push(self, e):
      """Adiciona o elemento e ao topo da pilha."""
      self._data.append(e)                  # novo item armazenado no final da lista

  def top(self):
      """Retorna (mas não remove) o elemento no topo da pilha.

      Mostra uma exceção de vazia se a pilha estiver vazia.
      """
      if self.is_empty():
          #raise Empty('Stack is empty')
          return None
      else:
          return self._data[-1]                 # o último item na lista

  def pop(self):
      """Remove e retorna o elemento do topo da pilha (ou seja, LIFO).

      Mostra uma exceção de vazia se a pilha estiver vazia.
      """
      if self.is_empty():
          # raise Empty('Stack is empty')
          return None
      else:
          return self._data.pop()               # remove o último item da lista
