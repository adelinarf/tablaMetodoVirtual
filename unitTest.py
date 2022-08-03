import unittest
from main import tipos, nuevoTipo, verificarEntrada, eliminarStringVacio,buscarMetodos,describeTipo

class Testing(unittest.TestCase):
    def test(self):
        nuevoTipo(["B",":","A","f","g","h"])
        contiene = "B" in tipos
        self.assertEqual(contiene,False)
        nuevoTipo(["B","f","g","h"])
        contiene = "B" in tipos
        self.assertTrue(contiene)
        nuevoTipo(["A",":","B","f","g","m"])
        contiene = "A" in tipos
        self.assertTrue(contiene)
        self.assertEqual(tipos["A"][0],"B")
        self.assertTrue(verificarEntrada(["CLASS","S","c","f"],0))
        self.assertFalse(verificarEntrada(["DESCRIBIR","A","B","C"],1))
        self.assertTrue(verificarEntrada(["CLASS","S",":","A","c","f"],0))
        self.assertFalse(verificarEntrada(["CLASS","S",":"],0))
        self.assertFalse(verificarEntrada(["CLASS"],1))
        self.assertEqual(eliminarStringVacio(["","",""]),[])
        self.assertEqual(eliminarStringVacio(["CLASS","","A","","B","D"]),["CLASS","A","B","D"])
        self.assertEqual(eliminarStringVacio(["DESCRIBIR","","A","","B","D"]),["DESCRIBIR","A","B","D"])
        self.assertEqual(eliminarStringVacio(["DESCRIBIR","","","","","","","","","D"]),["DESCRIBIR","D"])
        self.assertEqual(buscarMetodos("B"),[("B",["f","g","h"])])
        self.assertEqual(buscarMetodos("A"),[("A",["f","g","m"]),("B",["f","g","h"])])
        describeTipo(["B"])
        describeTipo(["A"])
   
if __name__ == '__main__':
    unittest.main()
