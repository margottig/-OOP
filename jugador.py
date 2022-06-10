from coopEquipo import CoopEquipo
from equipo import Equipo

class Jugador(Equipo):
    numeroJugador = 10

    # Inicializador/Contructor
    def __init__(self, data ):
        super().__init__(data['nombre_equipo'])  #HEREDAR
        self.nombre = data['nombre']
        self.edad = data['edad']
        self.posicion = data['posicion']
        self.cuentas = []
        # self.equipo = data['nombre_equipo']

    def getNombre(self):
        print(f'El nombre del jugador es: {self.nombre}')
        return self

    def setNombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        return self

    #POLIMORFISMO
    def mensajeAleatorio(self):
        print('Hola desde la subclase Jugador ')
        return self
      
    #ABSTRACCIÓN
    def crearCuenta(self, numeroCuenta, cantidad):
        self.cuentas.append(CoopEquipo(numeroCuenta, cantidad))
        return self

    @classmethod
    def getNumeroJugador(cls):
        print(f'El numero del jugador es: {cls.numeroJugador}')
        return cls




        
