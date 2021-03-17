class Progresion:
    def __init__(self, inicial, distancia, cantidad):
        self.__inicial= inicial
        self.__distancia= distancia
        self.__cantidad=cantidad

    def __iter__(self):
        self.__valor=self.__inicial
        self.__contador=0
        return self
    
    def __next__(self):
        if self.__contador==self.__cantidad:
            raise StopIteration
        else:
            resultado = self.__valor
            self.__contador+=1
            self.__valor+=self.__distancia
            return resultado
    
def progresion(inicial, distancia, cantidad):
    valor=inicial
    contador=0

    while contador<cantidad:
        yield valor
        valor+=distancia
        contador +=1



if __name__=="__main__":
    lista= [1,3,2,4,5,32] #iterable vs iterator

    for elemento in lista:
        print(elemento)
    
    for numero in Progresion(23, 2, 5):
        print(numero)
    
    for numero in progresion(23,2,5):
        print(numero)