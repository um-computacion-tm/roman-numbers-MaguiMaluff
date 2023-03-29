import unittest

def roman_to_decimal(roman):
    resultado = 0
    for letra in roman[: : -1]:
        if letra == "I":
            if resultado > 3:
                resultado -= 1
            else:
                resultado += 1
        elif letra == "V":
            resultado += 5
        elif letra == "X":
            if resultado > 39:
                resultado -= 10
            else:
                resultado += 10
        elif letra == "L":
            resultado += 50
        elif letra == "C":
            if resultado > 1000:
                resultado -= 100
            else:
                resultado += 100
        elif letra == "D":
            resultado += 500
        elif letra == "M":
            resultado += 1000
    return resultado
    
 

class TestRomanToDecimal(unittest.TestCase):
    def test_1(self):
        resultado = roman_to_decimal("I")
        self.assertEqual(resultado, 1)
    def test_2(self):
        resultado = roman_to_decimal("II")
        self.assertEqual(resultado, 2)
    def test_3(self):
        resultado = roman_to_decimal("III")
        self.assertEqual(resultado, 3)
    def test_5(self):
        resultado = roman_to_decimal("V")
        self.assertEqual(resultado, 5)
    def test_6(self):
        resultado = roman_to_decimal("VI")
        self.assertEqual(resultado, 6)
    def test_7(self):
        resultado = roman_to_decimal("VII")
        self.assertEqual(resultado, 7)
    def test_8(self):
        resultado = roman_to_decimal("VIII")
        self.assertEqual (resultado, 8)
    def test_10(self):
        resultado = roman_to_decimal("X")
        self.assertEqual(resultado, 10)
    def test_9(self):
        resultado = roman_to_decimal("IX")
        self.assertEqual(resultado, 9)
    def test_19(self):
        resultado = roman_to_decimal("XIX")
        self.assertEqual(resultado, 19)
    def test_29(self):
        resultado = roman_to_decimal("XXIX")
        self.assertEqual(resultado, 29)
    def test_43(self):
        resultado = roman_to_decimal("XLIII")
        self.assertEqual(resultado, 43)
    def test_60(self):
        resultado = roman_to_decimal("LX")
        self.assertEqual(resultado, 60)
    def test_129(self):
        resultado = roman_to_decimal("CXXIX")
        self.assertEqual(resultado, 129)
    def test_111(self):
        resultado = roman_to_decimal("CXI")
        self.assertEqual(resultado, 111)
    def test_555(self):
        resultado = roman_to_decimal("DLV")
        self.assertEqual(resultado, 555)
    def test_666(self):
        resultado = roman_to_decimal("DCLXVI")
        self.assertEqual(resultado, 666)
    def test_1111(self):
        resultado = roman_to_decimal("MCXI")
        self.assertEqual(resultado, 1111)
    def test_1999(self):
        resultado = roman_to_decimal("MCMXCIX")
        self.assertEqual(resultado, 1999)





if __name__ == '__main__':
    unittest.main()