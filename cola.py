class Cola:
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
            return self.__elementos.pop(0) 
        return None

    def isEmpty(self) -> bool:
        return len(self.__elementos) == 0

    def top(self) -> object:
        if not self.isEmpty():
            return self.__elementos[0]
        return None

    def size(self) -> int:
        return len(self.__elementos)

    def reverse(self):
        nueva_cola = Cola()
        for elemento in reversed(self.__elementos):
            nueva_cola.push(elemento)
        return nueva_cola

    def pushAll(self, otraCola):
        for elemento in otraCola.__elementos:
            self.push(elemento)