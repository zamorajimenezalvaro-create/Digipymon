# Digipymon

## ¿De qué trata?

Este proyecto es un juego RPG por consola en Python en el que el jugador asume el papel de un entrenador de criaturas llamadas Digipymon.

El objetivo principal es:

- Explorar
- Capturar Digipymon
- Combatir contra otros entrenadores
- Gestionar recursos (dinero y objetos)

Todo esto mediante un sistema sencillo basado en menús.

## Funcionamiento general

El juego sigue un bucle principal con un menú donde el jugador puede elegir acciones:

1. Buscar Digipymon salvajes
2. Combatir contra entrenadores
3. Comprar en la tienda
4. Usar objetos
5. Ver inventario
6. Ver Digipymons
7. Salir

Al empezar:

- El jugador introduce su nombre
- Recibe un Digipymon inicial aleatorio
- Empieza con objetos y dinero

## Sistema de Digipymon

Cada Digipymon tiene:

- Nombre (aleatorio)
- Vida
- Ataque
- Tipo: fuego, agua o planta
- Nivel (1–3)

Se generan de forma aleatoria, lo que da variedad al juego.

## Sistema de combate

El combate es automático y por comparación de ataque:

- Cada Digipymon del jugador lucha contra uno del enemigo
- Se comparan los valores de ataque

### Reglas:

- Si tu ataque es mayor → ganas
- Si es menor o igual → pierdes

### Consecuencias:

- El Digipymon pierde vida tras cada combate
- Puede quedar debilitado (vida = 0)

### Resultado final:

- Más victorias → ganas digicoins
- Más derrotas → pierdes digicoins
- Igual → empate

Es un sistema simple, sin turnos ni habilidades.

## Sistema de inventario

El jugador tiene un inventario basado en diccionario con objetos:

### Objetos disponibles:

- Digipyball → sirve para capturar
- Poción → cura +10 vida
- Anabolizante → +5 ataque

### Características:

- Los objetos se consumen al usarlos
- Si se acaban, se eliminan del inventario

## Sistema de captura

Cuando encuentras un Digipymon puedes intentar capturarlo con una digipyball, la probabilidad de captura es: 100 - (nivel * 10)

### Reglas:

- Necesitas digipyballs
- Máximo 6 Digipymons en el equipo
- Si fallas → el Digipymon escapa

# Tienda (Digishop)

Puedes comprar objetos usando digicoins:

| Objeto        | Precio |
|---------------|--------|
| Digipyball    | 5      |
| Poción        | 3      |
| Anabolizante  | 4      |

# Sistema económico

- Empiezas con 10 digicoins
- Ganas monedas al ganar combates
- Pierdes monedas al perder o huir

# Clases del proyecto

El código está organizado en clases:

- Jugador → gestiona equipo y dinero
- Enemigo → entrenador rival
- Digipymon → criatura con estadísticas
- Inventario → objetos del jugador
- ListaNombres → nombres aleatorios

# Reglas importantes del juego

- Máximo 6 Digipymons
- Los Digipymons pueden quedar debilitados
- No hay curación automática
- No hay ventaja de tipos (todavía)
- Combate basado solo en ataque
- Recursos limitados (objetos y dinero)
