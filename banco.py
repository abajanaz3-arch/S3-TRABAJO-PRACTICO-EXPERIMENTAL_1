from cola import Cola

class Persona:
    """
    Diagrama UML:
    ---------------------------------
    |            Persona            |
    ---------------------------------
    | - nombre: str                 |
    ---------------------------------
    | + Persona(nombre: str)        |
    | + get_nombre(): str           |
    ---------------------------------
    """
    def __init__(self, nombre: str):
        self.__nombre = nombre

    def get_nombre(self) -> str:
        return self.__nombre
    
class Cliente(Persona):
    """
    Diagrama UML:
    ---------------------------------
    |            Cliente            |
    ---------------------------------
    | - tipo: str                   |
    ---------------------------------
    | + Cliente(nombre: str, tipo: str) |
    | + get_tipo(): str             |
    ---------------------------------
    """
    def __init__(self, nombre: str, tipo: str):
        super().__init__(nombre)
        self.__tipo = tipo

    def get_tipo(self) -> str:
        return self.__tipo
    
class CajaBanco:
    """
    Diagrama UML:
    ---------------------------------
    |           CajaBanco           |
    ---------------------------------
    | (Sin atributos)               |
    ---------------------------------
    | + main(): void                |
    ---------------------------------
    """
class CajaBanco:
    @staticmethod
    def main():
        cola_espera = Cola()

        datos_clientes = [
            ("Ana", "Normal"),
            ("Beto", "Preferente"),
            ("Carlos", "Normal")
        ]

        print("--- LLEGADA DE CLIENTES AL BANCO ---")
        for nombre, tipo in datos_clientes:
            nuevo_cliente = Cliente(nombre, tipo)
            cola_espera.push(nuevo_cliente)
            print(f"{nuevo_cliente.get_nombre()} ({nuevo_cliente.get_tipo()}) ha entrado.")

        print("\n--- INICIO DE ATENCIÓN EN LA CAJA ---")

        while not cola_espera.isEmpty():
            p = cola_espera.pop()
            print(f"Atendiendo a: {p.get_nombre()} | Tipo: {p.get_tipo()}")


if __name__ == "__main__":
    CajaBanco.main()
