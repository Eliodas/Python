class ClassExpectedError(Exception):
    pass
class TypedList(list):
    def __init__(self, element_type):
        """Define listas de un solo tipo"""
        super().__init__()

        if isinstance(element_type, type):
            self.__element_type=element_type
        else:
            raise ClassExpectedError("El parametro debe ser una clase")

    def append(self, value) -> None:
        if type(value)==self.__element_type:
            super().append(value)
        else:
            raise ValueError(f"El elemento debe ser de tipo {self.__element_type}")
    
    def __setitem__(self, index, value):
        if type(value)==self.__element_type:
            super().__setitem__(index,value)
        else:
            raise ValueError(f"El elemento debe ser de tipo {self.__element_type}")
class IntList(TypedList):
    def __init__(self):
        super().__init__(int)



if __name__=="__main__":
    l= IntList()
    l=TypedList(45)
    l.append(12)
    l.append(23)
    l.append(34)
    l.append("Hola")
    l[2]=56
    l[1]="43"
    print(l)