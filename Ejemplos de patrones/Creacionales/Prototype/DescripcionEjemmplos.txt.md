Ejemplo 1 
 Prototype básico
Qué es: Clonar objetos sin usar new.
Qué enseña: La idea central del patrón: crear copias de un objeto existente en lugar de instanciar desde cero.


Ejemplo 2 
 Prototype con modificación tras clonar
Qué es: Extiende el básico permitiendo cambiar atributos en el clon.
Qué enseña: Cómo un clon puede partir de un objeto base pero adaptarse (ej. cambiar nombre).


Ejemplo 3 
Prototype con composición
Qué es: Un objeto tiene referencias a otros objetos (ej. personaje con arma).
Qué enseña: La diferencia entre clon superficial y la problemática de compartir objetos internos.


Ejemplo 4 
Prototype con clon profundo
Qué es: Cada objeto clonado tiene sus propios objetos internos.
Qué enseña: Cómo resolver el problema de las referencias compartidas usando clon profundo.


Ejemplo 5 
Prototype Registry
Qué es: Registro de prototipos para crear clones a partir de una “plantilla” guardada.
Qué enseña: Cómo gestionar múltiples prototipos de forma centralizada. Es el uso más profesional y reutilizable del patrón Prototype.