# Análisis numérico
Es un proyecto con el objetivo de animar diversos algoritmos presentados en cada uno de los videos del canal

# Métodos cerrados

## Bisección
Si se desea animar una bisección desde el main se recomienda usar el siguiente código

``` python
from manim import *

# Importar la bisección
from Biseccion.Animar_biseccion import Animar_biseccion

def f(x):
    return x**3 - 6*x**2 + 11*x - 6

if __name__ == "__main__":
    config.quality = "low_quality" 
    config.preview = True          
   
    escena = Animar_biseccion(
        funcion=mi_funcion, 
        a=0.1, 
        b=1.8, 
        n=5, 
        tol=0.0001
    )
   
    escena.render()
```

Observe que para el criterio de parada se inyecta la tolerancua y el número de pasos, estos dos entran a un bucle while y el primero que se cumpla es el criterio que lo rompe

```python
while (error > tol) and i < n:
    # ...
```