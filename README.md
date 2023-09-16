# Repositorio para Semana Tec TC1001S

Cambios hechos en cada juego:
### Paint
- Añadir color naranja para la pluma que se llama con la letra 'o' (line 117)
- Añadir función para dibujar un círculo (relleno), que toma como los 2 puntos de entrada como el diámetro del círculo y que utiliza la función ya existente de circle() de la librería de turtle para dibujar el círculo pasando como parámetro el radio, centrándose pero comenzando desde la longitud del radio hacia la izquierda para poder obtener el diámetro
- Añadir función que dibuja un rectángulo (relleno) que toma como entrada 2 puntos que son utilizados como la diagonal del rectángulo
- Añadir la función que dibuja un triángulo equilátero (relleno), que toma como entrada 2 puntos y los utiliza como la base del triángulo

### Snake
- Añadir función que mueve la comida de 1 paso en 1 paso de manera aleatoria una vez se ha comido la serpiente el pedazo anterior y que no se salga del cuadro de juego
- Añadir una función para que se les asigne un color aleatorio tanto a la serpiente como a la comida pero sin repetir el color y no incluye el color rojo dentro de la lista que se toma como entrada; la serpiente es asignada color primero 

### Pacman
- Añadir función que hace que los fantasmas sean más listos, tomando como criterio el hecho de que recorren más tramos que no han recorrido antes y dejan poca probabilidad de no encontrar al pacman ya que cuando chocan se van por direcciones opuestas por lo que no pasan por donde otro fantasma ya pasó
- Cambiar la distribución del tablero para que sea un poco más lineal y auxilie al cambio en movimiento que se le realizó a los fantasmas
- Cambiar el parámetro de velocidad de movimiento de los fantasmas (line 166)

### Cannon
- Cambiar el parámetro de velocidad del movimiento tanto de target como de balls para que ambas se muevan más rápido (line 82)
- Eliminar loop que checa que los targets se encuentren dentro del rango en la función move(), además de crear una condición que checa cuando un target se sale de rango y lo resetea a la misma posición en el eje y pero del lado contrario en x para que el juego nunca termine

### Memory
- Añadir un contador de taps, función que cuenta los taps con variable global, llamar a la función desde la función tap(), y crear función que muestra los taps en pantalla en la esquina superior izquierda (punto a mejorar, no cuenta con fondo propio el texto por lo que sobre el fondo oscuro del auto cuando se termina el juego no se alcanza a ver tan bien)
- Añadir función que reconoce cuando el juego se termina (cuando todas las tiles son destapadas) y despliega un mensaje de felicitación
- Cambiar los parámetros que despliegan los números sobre las tiles para que se vean más centrados (line 94)
- Como extra, cambiar el uso de números en los tiles a letras y caracteres especiales (los primeros 32 de ASCII), como adicional se podrían agregar imágenes como en un típico juego de memorama o incluso simplemente una distinción de colores o palabras haría que le juego fuera algo menos complicado
