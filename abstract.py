from abc import ABC, abstractmethod

class Figura(ABC):
    
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura
    
    def area(self):
        return self.base*self.altura

    def perimetro(self):
        return 2*self.altura+2*self.base

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura
    
    def area(self):
        return self.base*self.altura/2

    def perimetro(self):
        return 3*self.base

def mostrar_figuras(lista):
    for figura in lista:
        print(figura.area())

if __name__=="__main__":
    fig = Rectangulo(5,4)
    print(fig.area())