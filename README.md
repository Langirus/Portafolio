# Rebalanceo de Portafolio

Este repositorio contiene una implementación simple de un portafolio de inversión
con capacidad de rebalancearse según una asignación objetivo.

El foco de esta solución es mostrar de forma clara la lógica de rebalanceo,
más que construir un sistema financiero completo.

---

## Problema

Dado:
- Un portafolio con una distribución actual de acciones
- Una asignación objetivo (por ejemplo: 40% META, 60% AAPL)

Determinar:
- Qué acciones se deben **comprar**
- Qué acciones se deben **vender**

para que el portafolio quede alineado con la asignación objetivo.

---

## Decisiones de Diseño y Supuestos

Para mantener la solución simple y enfocada en el problema principal, se tomaron los siguientes supuestos:

- El portafolio se modela en términos de **valor actual por acción**, no en número de acciones.
- Los porcentajes de asignación deben sumar **1.0**.
- No se consideran comisiones, impuestos ni restricciones de tamaño mínimo de compra/venta.
- El rebalanceo se realiza usando el **valor total actual del portafolio**.

Este enfoque permite expresar la lógica de forma directa y fácil de entender.

---

## Cómo Funciona el Rebalanceo

1. Se calcula el valor total del portafolio.
2. Para cada acción, se calcula su valor objetivo según el porcentaje asignado.
3. Se compara el valor objetivo con el valor actual.
4. Si la diferencia es:
   - Positiva → la acción se debe **comprar**
   - Negativa → la acción se debe **vender**

El resultado del rebalanceo se entrega en dos estructuras:
- `comprar`: acciones y montos a comprar
- `vender`: acciones y montos a vender

---

## Ejemplo

Portafolio actual:
```python
{"META": 200, "AAPL": 200}
