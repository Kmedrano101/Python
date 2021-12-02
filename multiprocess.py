"""
    By Kevin Medrano Ayala
    Example Multiprocessing
    Atributos:
        - rbaud
        - bits
    Metodos:
        - recibir
        - escribir
"""

from multiprocessing import Process,Manager
import time, random

class Serial():
    """Example for Serial."""
    def __init__(self, puerto,rbaud=9600,bits=8):
        super(Serial, self).__init__()
        self._rbaud = rbaud
        self._bits = bits
        self._puerto = puerto
        
    """Propiedades"""
    @property
    def rbaud(self):
        """The rbaud property."""
        return self._rbaud
    
    @rbaud.setter
    def rbaud(self, value):
        self._rbaud = value
    
    @property
    def bits(self):
        """The bits property."""
        return self._bits
    
    @bits.setter
    def bits(self, value):
        self._bits = value
    
    @property
    def puerto(self):
        """The puerto property."""
        return self._puerto
    
    @puerto.setter
    def puerto(self, value):
        self._puerto = value
    
    """Metodos / Comportamientos"""
    def recibir(self) -> str:
        time.sleep(1)
        return str(random.randint(10,40))
    
    def escribir(self,data) -> None:
        print(f'Datos enviados: {data}')
        time.sleep(1)
        
manager = Manager()
datos = manager.list()

def recibir20Datos(nData) -> list:
    data = Serial("COM2")
    for _ in range(nData):
        datos.append(data.recibir())
    return datos

def enviarUltimaDato() -> None:
    print("Enviando datos...")
    time.sleep(1.5)
    print("Datos enviados con exito.")
    
# def contadorEventos() -> int:
#     value = 0
#     time.sleep(1)
#     value += 1
#     return value
def main():
    print("Inicio del programa Main\n","#"*40)
    start = time.time()
    """Recibir 10 datos y luego enviarlos"""
    nData = 10
    process1 = Process(target=recibir20Datos,args=(nData,))
    Process(target=enviarUltimaDato).start()
    #print(recibir20Datos(10)) #Test without multiprocessing
    end = time.time()
    tiempoT = "{:.4f}".format(end-start)
    process1.start()
    process1.join()
    print(datos)
    print(f'Tiempo transcurrido: {tiempoT}')
    print("Fin del programa Main\n","#"*40)

if __name__ == "__main__":
    main()