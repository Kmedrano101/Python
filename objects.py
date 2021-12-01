"""
    By Kevin Medrano Ayala
"""

# Crear una clase
# Los atributos deben de ser privados y no ser accedidos directamente
class Figura:
    # Constructor
    def __init__(self,color, n_lados=2) -> None:
        # Declaramos atributo normal
        self.n_lados = n_lados
        # Declaramos atributo privado "_"
        self._color = color
    # Propiedades
    @property
    def color(self):
        """Propiedad de color."""
        return self._color
    
    @color.setter
    def color(self, value):
        self._color = value
    
    @color.deleter
    def color(self):
        del self._color
        
class Persona():
    def __init__(self) -> None:
        self._nombre = ''
        self._edad = 0
    
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
    def hablar(self, mensaje) -> str:
        print("Se ha enviado el mensaje!")
        return "Se esta hablando... "+mensaje
    def comer(self,alimento) -> None:
        print("Se ha iniciado a comer...")
    
def main():
    # Instaciar objetos
    triangulo = Figura("rojo")
    cuadrado = Figura("azul",4)
    persona = Persona()
    persona.nombre = "Kevin Medrano"
    persona.edad = 25
    #del cuadrado.color
    print(f'Triangulo es color {triangulo.color} ')
    print(f'Cuadrado tiene {str(cuadrado.color)} lados')
    print(f'Datos de la persona: \nNombre: {persona.nombre}\nEdad: {persona.edad}')
    
    
if __name__ == '__main__':
    main()