# Requisitos Funcionales - DIGIPYMON

## 1. Gestión del Jugador
- El sistema debe permitir al usuario introducir un nombre al iniciar la partida.
- El sistema debe crear un jugador con:
  - Un nombre
  - Un equipo de Digipymon vacío (inicialmente)
  - Una cantidad inicial de digicoins (10)

## 2. Inicio de Partida
- El sistema debe generar un Digipymon inicial aleatorio.
- El sistema debe añadir este Digipymon al equipo del jugador.
- El sistema debe otorgar al jugador objetos iniciales:
  - 3 digipyballs
  - 1 poción

## 3. Menú Principal
- El sistema debe mostrar un menú con las siguientes opciones:
  1. Buscar Digipymon
  2. Luchar contra un entrenador
  3. Ir a la tienda
  4. Usar objetos
  5. Consultar inventario
  6. Consultar Digipymon
  7. Salir
- El sistema debe permitir al usuario seleccionar una opción mediante entrada de texto.
- El sistema debe ejecutar la acción correspondiente a la opción elegida.

## 4. Generación de Digipymon
- El sistema debe generar Digipymon con atributos aleatorios:
  - Vida (entre 10 y 20)
  - Ataque (entre 1 y 10)
  - Nivel (entre 1 y 3)
  - Tipo (fuego, agua o planta)
  - Nombre aleatorio

## 5. Búsqueda y Captura
- El sistema debe permitir encontrar Digipymon salvajes.
- El sistema debe mostrar la información del Digipymon encontrado.
- El sistema debe calcular una probabilidad de captura basada en el nivel.
- El sistema debe permitir al usuario decidir si intenta capturarlo.
- El sistema debe comprobar:
  - Si el jugador tiene digipyballs
  - Si el equipo tiene menos de 6 Digipymon
- El sistema debe consumir una digipyball al intentar capturar.
- El sistema debe añadir el Digipymon al equipo si la captura tiene éxito.

## 6. Sistema de Combate
- El sistema debe generar un enemigo con nombre aleatorio.
- El sistema debe asignar al enemigo un equipo con el mismo número de Digipymon que el jugador.
- El sistema debe permitir al jugador aceptar o rechazar el combate.
- El sistema debe enfrentar los Digipymon uno a uno.
- El sistema debe comparar los valores de ataque para determinar el resultado.
- El sistema debe actualizar la vida de los Digipymon tras cada combate.
- El sistema debe contabilizar victorias y derrotas.
- El sistema debe otorgar o quitar digicoins según el resultado final.

## 7. Inventario
- El sistema debe permitir almacenar objetos con su cantidad.
- El sistema debe permitir añadir objetos al inventario.
- El sistema debe permitir usar objetos.
- El sistema debe reducir la cantidad de un objeto al usarlo.
- El sistema debe eliminar un objeto si su cantidad llega a 0.
- El sistema debe mostrar el contenido del inventario.

## 8. Uso de Objetos
- El sistema debe permitir seleccionar un objeto del inventario.
- El sistema debe impedir usar objetos no disponibles.
- El sistema debe permitir elegir un Digipymon al que aplicar el objeto.
- El sistema debe aplicar efectos:
  - Poción: aumenta la vida
  - Anabolizante: aumenta el ataque
- El sistema no debe permitir usar digipyballs directamente.

## 9. Tienda
- El sistema debe mostrar los objetos disponibles para compra.
- El sistema debe permitir seleccionar un objeto a comprar.
- El sistema debe comprobar si el jugador tiene suficientes digicoins.
- El sistema debe añadir el objeto al inventario tras la compra.
- El sistema debe restar el coste en digicoins.

## 10. Consulta de Información
- El sistema debe permitir visualizar:
  - El inventario del jugador
  - El equipo de Digipymon

## 11. Reglas del Juego
- El sistema debe limitar el equipo a un máximo de 6 Digipymon.
- El sistema debe impedir capturar más si el equipo está lleno.
- El sistema debe impedir combatir con Digipymon debilitados.
- El sistema debe permitir huir de combates con penalización.

## 12. Finalización del Juego
- El sistema debe permitir al usuario salir del juego desde el menú.
- El sistema debe finalizar la ejecución cuando el usuario seleccione salir.
