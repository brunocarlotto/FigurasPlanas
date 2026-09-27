from math import pi
from .figuraplana import FiguraPlana


"""
Esse é o módulo que implementa figuras simples a partir de dimensões características.
""" 



class Retangulo(FiguraPlana):
    """
    Representa um retângulo de base b altura h.
    Iniciado com canto superior direito nas coordenadas (b/2, h/2).    
    """

    def __init__(self, b:float, h:float) -> None:

        self.b = b
        self.h = h
        A = b * h
        Ix = (b * h**3) / 12
        Iy = (h * b**3) / 12
        xc = 0.0
        yc = 0.0
        Ixy = 0.0
        super().__init__(A, Ix, Iy, xc, yc, Ixy)

    def __repr__(self) -> str:
        return f"Retangulo(b={self.b}, h={self.h})"

    def __str__(self) -> str:
        txt = f"Retângulo: b= {self.b}, h= {self.h} \n"
        txt += super().__str__()
        return txt

class TrianguloRetangulo(FiguraPlana):
    """
    Representa um triângulo retângulo de base b e altura h.
    O vértice do ângulo reto está localizado na origem (0, 0).
    """

    def __init__(self, b:float, h:float) -> None:
        self.b = b
        self.h = h
        A = (b * h) / 2
        Ix = (b * h**3) / 12
        Iy = (h * b**3) / 12
        xc = b / 3
        yc = h / 3
        Ixy = (b**2 * h**2) / 24
        super().__init__(A, Ix, Iy, xc, yc, Ixy)

    def __repr__(self) -> str:
        return f"TrianguloRetangulo(b={self.b}, h={self.h})"

    def __str__(self) -> str:
        txt = f"Triângulo retângulo: b= {self.b}, h= {self.h} \n"
        txt += super().__str__()
        return txt