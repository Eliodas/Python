class Stack:
    class Nodo:
        def __init__(self,valor,siguiente=None) -> None:
            self.valor=valor
            self.siguiente=siguiente
    def __init__(self) -> None:
        self.pila=None
        self.longitud=0
    def push(self,x):
        self.pila=Stack.Nodo(x,self.pila)
        self.longitud+=1

    def pop(self):
        if len(self)==0:
            pass
        else:
            self.pila=self.siguiente
            self.longitud-=1
    @property
    def top(self):
        if len(self)==0:
            return None
        else:
            return self.pila.valor

    def is_empty(self):
        if len(self)==0:
            return True
        else:
            return False

    def __len__(self):
        return self.longitud
    