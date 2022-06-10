class Equipo:
    listaEquipos = []

     # Inicializador/Contructor
    def __init__(self, nombre_equipo ):
        self.equipo = nombre_equipo
        Equipo.listaEquipos.append(nombre_equipo)

    def getNombreEquipo(self):
        print(f'El nombre del equipo es: {self.equipo}')
        return self

    def mensajeAleatorio(self):
        print('Hola desde la clase Equipo ')
        return self