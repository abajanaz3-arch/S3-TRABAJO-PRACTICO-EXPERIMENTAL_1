class Pila:
    """
    Diagrama UML:
    ---------------------------------
    |             Pila              |
    ---------------------------------
    | - elementos: list             |
    ---------------------------------
    | + Pila()                      |
    | + push(elemento: Object)      |
    | + pop(): Object               |
    | + isEmpty(): bool             |
    | + top(): Object               |
    | + size(): int                 |
    | + reverse(): Pila             |
    | + pushAll(otraPila: Pila)     |
    ---------------------------------
    """
    def __init__(self):
        self.__elementos = []

    def push(self, elemento: object):
        self.__elementos.append(elemento)

    def pop(self) -> object:
        if not self.isEmpty():
            return self.__elementos.pop()
        return None

    def isEmpty(self) -> bool:
        return len(self.__elementos) == 0

    def top(self) -> object:
        if not self.isEmpty():
            return self.__elementos[-1]
        return None

    def size(self) -> int:
        return len(self.__elementos)

    def reverse(self):
        nueva_pila = Pila()
        for elemento in reversed(self.__elementos):
            nueva_pila.push(elemento)
        return nueva_pila

    def pushAll(self, otraPila):
        for elemento in otraPila.__elementos:
            self.push(elemento)