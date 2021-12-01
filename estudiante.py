"""
    By Kevin Medrano Ayala
    Modulo Estudiante
    Atributos:
        - Nombre
        - Edad
        - Codigo
        - ppa -> Promedio del estudiante
    Metodos:
        - Hablar --> Recibe parametro mensaje
        - Comer  --> Recibe parametro alimento
        - Leer   --> Recibe parametro libro
        - Promedio --> Recibe parametro lista de 5 notas
"""

# importar modulos
from persona import Persona
import random

class Estudiante(Persona):
    """Constructor"""
    def __init__(self, nombre, edad,codigo="K101",ppa=6) -> None:
        super().__init__(nombre, edad)
        self._codigo = codigo
        self._ppa = ppa
        self._notas = []
    
    """Propiedades"""
    @property
    def codigo(self):
        """The codigo property."""
        return self._codigo
    
    @codigo.setter
    def codigo(self, value):
        self._codigo = value
    
    @property
    def ppa(self):
        """The ppa property."""
        return self._ppa
    
    @ppa.setter
    def ppa(self, value):
        self._ppa = value
    
    @property
    def notas(self):
        """The notas property."""
        return self._notas
    @notas.setter
    def notas(self, value):
        self._notas = value
    """Metodos - Comportamientos"""
    def leer(libro) -> None:
        print(f'{super().nombre} esta leyendo: {libro}')
    
    def promedio(self) -> float:
        self._notas = [x for x in random.sample(range(10),5)]
        print(f'\tNotas de {self._nombre}: {self._notas}')
        self._ppa = float(sum(self._notas)/float(len(self._notas)))
        return self._ppa
    def __str__(self) -> str:
        return f'{super().__str__()}\n\tEstudiante:\n\tCodigo: {self._codigo}\n\tppa: {self._ppa}'
    
def main():
    estudiante1 = Estudiante("Kevin M.",25)
    estudiante2 = Estudiante("Josy S.",27,codigo="J201")
    estudiante1.promedio()
    estudiante2.promedio()
    print('*'*40)
    print(estudiante1)
    print('*'*40)
    print(estudiante2)

if __name__ == "__main__":
    main()