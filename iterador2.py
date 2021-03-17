class Words:
    def __init__(self,string):
        self.__string = string

    def __iter__(self):
        self.__start = 0
        return self
    
    def __next__(self):
        if self.__start<len(self.__string):
            while self.__start<len(self.__string)\
                and self.__string[self.__start].isspace:
                self.__start+=1

            self.__end = self.__start

            while self.__end < len(self.string)\
                and not self.__string[self.__end].isspace():
                self.__end+=1

            palabra = self.__string[self.__start:self.__end]
            self.__start = self.__end+1
            return palabra
        else:
            raise StopIteration

        
            


if __name__ == "__main__":
    texto = "palabra1      palabra1          palabra4     "

    lista_split=texto.split()
    print(lista_split)
    for palabra in lista_split:
        print(palabra)

    for palabra in Words(texto):
        print(palabra)
    
    