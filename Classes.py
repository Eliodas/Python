from re import fullmatch
import sqlite3

class Persona:
    def __init__(self, nombre, dni):
        self.nombre=nombre
        self.dni=dni
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, valor):
        self.__nombre=valor
    
    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self,valor):
        if fullmatch(r"\d{8}[A-Z]",valor):
            self.__dni=valor
        else: 
            ValueError("dni incorrectto")
class Donante(Persona):
    __dbname = None

    @classmethod
    def set_dbname(cls, valor):
        cls.__dbname = valor

    @classmethod
    def get_dbname(cls):
        return cls.__dbname

    def __init__(self, nombre, dni) :
        super().__init__(nombre,dni)
        self.__donaciones = []
    
    @property
    def donaciones(self):
        for donacion in self.__donaciones:
            yield(donacion)

    
    def donar(self, fecha, entidad, cantidad):
        self.__donaciones.append((fecha,entidad,cantidad))



    def __repr__(self) -> str:
        return f"Donante('{self.nombre}', {self.dni})"

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, DNI: {self.dni}"
    
if __name__== "__main__":
   
    pepe=Donante("Pepito Grillo", "34567897L")
    pepe.donar("12/10/2020","Cruz Roja",200.0)
    pepe.donar("12/11/2020","Cruz Roja",200.0)
    print(pepe.donaciones)
    print(pepe)
    for donacion in pepe.donaciones:
        print(donacion)


