from manim import *

# Importar la bisección
from Biseccion.Animar_biseccion import Animar_biseccion

def mi_funcion(x):
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