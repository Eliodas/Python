class StackEmptyError(Exception):
        pass
# from stackexceptions import StackEmptyError # Descomentar cuando esté añadida la excepción StackEmptyError

class Stack:
    def __init__(self):
        self.lista=[]
    
    def push(self, valor):
        self.lista.append(valor)
    
    def pop(self):
        if len(self.lista)>0:
            return self.lista.pop(-1)
        else:
            raise StackEmptyError()
        
    def top(self):
        if len(self.lista)>0:
            return self.__str__()
            
        else:
            raise StackEmptyError()
        
    def is_empty(self):
        if len(self.lista)>0:
            return False
        return True
        
    def __len__(self):
        return len(self.lista)
        
    def __str__(self):
        return self.lista[-1]


if __name__ == "__main__":
    # Creamos una pila vacía
    my_stack = Stack()

    # Insertamos 10 elementos en my_stack
    for i in range(10):
        my_stack.push(i)
        print(my_stack.top)
    
    print("---")

    # Vaciamos my_stack y mostramos los elementos a medida que los quitamos
    while not my_stack.is_empty():

        print(my_stack.top)
        my_stack.pop()

    # Descomentar la línea de abajo para probar la excepción
    #my_stack.pop()


