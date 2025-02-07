Minger - Game
Descripción
Minger es un juego creado con la librería Pygame donde el protagonista es un vikingo llamado "Minger", que debe evitar chocar con un caracol que avanza por la pantalla. 
El jugador/vikingo/minger tiene que saltar para esquivar el caracol, pero debe ser rápido, ya que la velocidad del caracooler aumenta con el tiempo.

El juego cuenta con una mecánica sencilla de movimiento y saltos, además de aumentar la dificultad conforme avanzas. 
Cada vez que el caracol atraviesa la pantalla, el contador se incrementa y la velocidad de éste aumenta. 
El objetivo es evitar el choque con el caracol el mayor tiempo posible.

Cómo jugar
Ejecuta el script Python:
python minger_game.py
El objetivo del juego es evitar que el caracol colisione con el vikingo Minger.
Usa la barra espaciadora (SPACE) para hacer que el Minger salte.
Si Minger colisiona con el caracol, el juego terminará y podrás continuar presionando SPACE o salir presionando Q.

Controles
Espacio (SPACE): el Minger salta para evitar al caracol.
Tecla Q: Para salir del juego durante la pantalla de "Game Over".

Descripción del código
pygame: Se utiliza para crear el entorno gráfico y manejar las interacciones del juego.
Movimiento: el Minger puede saltar para esquivar al caracol. Se aplica gravedad para simular el salto, y la velocidad de caída depende de la gravedad.
Dificultad: Cada vez que el caracol recorre la pantalla, la velocidad de éste aumenta.
Colisión: Si el caracol toca al vikingo, el juego termina y muestra un mensaje de "Game Over".
Pantalla de inicio y fin: Muestra el nombre del juego y la suma de puntos, además de la opción de continuar o salir.

Recursos
Las imágenes necesarias para ejecutar el juego deben estar ubicadas en la carpeta skylines. 
Estas imágenes incluyen:

shield.png: Icono de la ventana.
basic.jpg: Fondo del cielo.
ground.png: Fondo del suelo.
snail1.png: Imagen del caracol.
static_viking.png: Imagen del vikingo en reposo.
jumping_viking.png: Imagen del vikingo saltando.
falling_viking.png: Imagen del vikingo cayendo.
