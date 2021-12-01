"""
    By Kevin Medrano Ayala
    Modulo Persona
    Atributos:
        - Nombre
        - Edad
    Metodos:
        - Hablar --> Recibe como parametro mensaje
        - Comer  --> Recibe como parametro alimento
"""

class Persona:
    """Constructor"""
    def __init__(self,nombre,edad) -> None:
        self._nombre = nombre
        self._edad = edad
    
    """Propiedades"""
    @property
    def nombre(self):
        """The nombre property."""
        return self._nombre
    
    @nombre.setter
    def nombre(self, value):
        self._nombre = value
    
    @property
    def edad(self):
        """The edad property."""
        return self._edad
    
    @edad.setter
    def edad(self, value):
        self._edad = value
    
    """Metodos"""
    def hablar(self, mensaje) -> None:
        print(f'{self._nombre} dice: {mensaje}')
    
    def comer(self,alimento) -> None:
        print(f'{self._nombre} esta comiendo: {alimento}')
    
    def __str__(self) -> str:
        return f'\tClass Persona\n\tNombre: {self._nombre}\n\tEdad: {self._edad}'

def main():
    persona1 = Persona("Kevin M.",24)
    print(persona1)
    
if __name__ == "__main__":
    #print(__name__)
    main()