class Stack:

    class Iterador:
        def __init__(iself, elements):
            iself.__elements= elements
            iself.__actual=len(iself.__elements)-1

        def __next__(iself):
            if iself.__actual < 0:
                raise StopIteration
            else:
                resultado=iself.__elements[iself.__actual]
                iself.__actual-=1
                return resultado

    def __init__(self):
        self.__elements=[]

    def push(self,value):
        self.__elements.append(value)
    
    @property
    def top(self):
        if len(self.__elements)>0:
            return self.__elements[-1]
        else:
            return None
    
    def pop(self):
        if len(self.__elements)>0:
            return self.__elements.pop(-1)
    
    def __iter__(self):
        actual = len(self.__elements)-1
        
        while actual >=0:
            yield self.__elements[actual]
            actual-=1
    
    
    

if __name__=="__main__":
    s= Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    for elemento in s:
        print(elemento)
        for elemento1 in s:
            print(elemento1)

    """lista = [20,30,40]
    for item in lista:
        print(item)
        print("----")
        for item1 in lista:
            print(item1)"""
    