## 👥 Integrantes

- **Juan David Mayorga López** – 20232020116
- **Samuel Andrés Barrera Pulido** – 20232020156
- **Mariam Betin Escobar** – 20232020300
---
**Correccion de Antipatrones**

Este proyecto parte de un código diseñado con antipatrones para analizarlos y corregirlos. El objetivo fue identificar tres antipatrones principales, explicar su impacto y proponer una solución manteniendo la misma estructura general del programa.

---

1. God Object

Problema:
La clase AppManager tenía demasiadas responsabilidades: cargar datos, imprimir, calcular descuentos, calcular envíos y ejecutar el programa.

Solución:
Se dividió la lógica en clases especializadas:
UserRepository → manejo de datos
DiscountCalculator → descuentos
ShippingCalculator → cálculos de envío
AppManager → ahora solo coordina

---

2. Magic Numbers (Números mágicos)

Problema:
Había valores sin explicación (5, 7, 20, 0.25, 123.45...).
Esto dificulta entender el código y modificar reglas del negocio a largo plazo o si hay un reemplazo de equipo.

Solución:
Se crearon constantes con nombres descriptivos:
BaseDomestic, WeightThreshold...

Esto hace que las reglas sean claras y fáciles de ajustar.

---
3. Code-Paste Programming

Problema:
Los métodos ship_cost_domestic y ship_cost_international tenían casi la misma lógica con pequeñas variaciones.

Solución:
Se creó un método común _ship_cost_common() que recibe los valores distintos y reutiliza la misma fórmula.
Esto elimina duplicación y permite la extenciones futuras si se usa algun otro medio de envio.