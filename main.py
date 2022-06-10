# IMPORTAR MODULOS
from equipo import Equipo
from jugador import Jugador


jugadores = [
    {
    	"nombre": "Mario Bros", 
    	"edad":34, 
    	"posicion": "medio", 
    	"nombre_equipo": "Nintendo"
    },
    {
    	"nombre": "Sonic", 
    	"edad":24, 
    	"posicion": "delantero", 
    	"nombre_equipo": "Sega"
    },
    {
    	"nombre": "Rocko ", 
    	"edad":32,
		"posicion": "defensa", 
    	"nombre_equipo": "Nick"
    },
    {
    	"nombre": "Felix", 
    	"edad":33, 
		"posicion": "portero", 
    	"nombre_equipo": "Cat"
    }
]


felix =    {
    	"nombre": "Felix", 
    	"edad":33, 
		"posicion": "portero", 
    	"nombre_equipo": "Cat"
    }

#Jugador 1
jugador_1 = Jugador(felix) #creando el objeto jugador_1
jugador_1.getNombre().setNombre('Rick')  #Encadenando métodos
print(jugador_1.__dict__) #abriendo/imprimeindo el objeto

jugador_1.getNombreEquipo().mensajeAleatorio().crearCuenta(1234, 5000).getNumeroJugador()
#print("El nombre del equipo de jugador_1 es:", Equipo.listaEquipos )

print(jugador_1.__dict__)
