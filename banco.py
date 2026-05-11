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
    @staticmethod
    def main():
        cola_espera = Cola()

        nombres = ["Ana", "Beto", "Carlos", "Diana", "Luis"]
        
        print("--- LLEGADA DE PERSONAS AL BANCO ---")
        for nombre in nombres:
            nueva_persona = Persona(nombre)
            cola_espera.push(nueva_persona)
            print(f"{nombre} ha entrado a la cola.")

        print("\n--- INICIO DE ATENCIÓN EN LA CAJA ---")

        while not cola_espera.isEmpty():
            persona_atendida = cola_espera.pop()
            print(f"La persona {persona_atendida.get_nombre()} ha sido atendida.")

if __name__ == "__main__":
    CajaBanco.main()