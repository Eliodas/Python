import unittest 
from words import words
class NoWordsTests(unittest.TestCase):
    def setUp(self):
        return super().setUp()
        self.result=[]

        def test_01(self):
            """String vacia"""

            test_string = ""

            for word in words(test_string):
                self.result.append(word)


            self.assertEquals(len(self.results),0, "Falla: " + self.__doc__)
        
        def test_02(self):
            """String con un espacio"""

            test_string = " "

            for word in words(test_string):
                self.result.append(word)


            self.assertEquals(len(self.results),0, "Falla: " + self.__doc__)