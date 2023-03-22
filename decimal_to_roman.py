import unittest

def unidad_decimal(decimal):
    unidadinicial = decimal % 10
    unidad = ''
    if unidadinicial <= 3:
        unidad = 'I' * unidadinicial
    elif unidadinicial == 4:
        unidad = 'IV'
    elif unidadinicial == 5:
        unidad = 'V'
    elif unidadinicial > 5 and unidadinicial < 9:
        unidad = 'V'+('I' * (unidadinicial - 5))
    elif unidadinicial == 9:
        unidad = 'IX'
    elif unidadinicial == 0:
        unidad = '0'
    return unidad

def decimal_to_roman(decimal):
    ## de 0 a 9
    if decimal < 10:
        unidadfinal = unidad_decimal(decimal)
        return unidadfinal
    ###del 10 al 39
    elif decimal >= 10 and decimal < 40:
        decimalinicial = decimal / 10
        unidadfinal = unidad_decimal(decimal) 
        return ("X" * int(decimalinicial)) + unidadfinal
    ## del 40 al 49
    elif decimal >= 40 and decimal < 50:
        unidadfinal = unidad_decimal(decimal)
        return "XL" + unidadfinal
    ## del 50 al 89
    elif decimal >= 50  and decimal < 90:
        unidadfinal = unidad_decimal(decimal)
        return ("X" * int((decimal/10) - 5)) + "L" + unidadfinal
    elif decimal >= 90 and decimal < 100:
        unidadfinal = unidad_decimal(decimal)
        return "XC" + unidadfinal

## decimal decimal / 10 y unidad decimal % 10

class TestDecimalToRoman(unittest.TestCase):
    def test_uno(self):
        # pre condicion
        ### NO HAY ###
        # proceso
        resultado = decimal_to_roman(1)
        # verificacion
        self.assertEqual(resultado, 'I')

    def test_dos(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado, 'II')

    def test_tres(self):
        resultado = decimal_to_roman(3)
        self.assertEqual(resultado, 'III')

    def test_diez(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, 'X')

    def test_cinco(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, 'V')

    def test_seis(self):
        resultado = decimal_to_roman(6)
        self.assertEqual(resultado, 'VI')

    def test_siete(self):
        resultado = decimal_to_roman(7)
        self.assertEqual(resultado, 'VII')
    
    def test_ocho(self):
        resultado = decimal_to_roman(8)
        self.assertEqual (resultado, 'VIII')

    def test_trescero(self):
        resultado = decimal_to_roman(30)
        self.assertEqual(resultado, 'XXX')

    def test_veinte(self):
        resultado = decimal_to_roman(20)
        self.assertEqual(resultado, 'XX')

    def test_unonueve(self):
        resultado = decimal_to_roman(19)
        self.assertEqual(resultado, 'XIX')
    
    def test_dostres(self):
        resultado = decimal_to_roman(23)
        self.assertEqual(resultado, 'XXIII')

    def test_tresnueve(self):
        resultado = decimal_to_roman(39)
        self.assertEqual(resultado, 'XXXIX')
    
    def test_trescero(self):
        resultado = decimal_to_roman(30)
        self.assertEqual(resultado, 'XXX')

    def test_cuarenta(self):
        resultado = decimal_to_roman(40)
        self.assertEqual(resultado, 'XL')
    
    def test_cuatrotres(self):
        resultado = decimal_to_roman(43)
        self.assertEqual(resultado, 'XLIII')
    
    def test_cuatronueve(self):
        resultado = decimal_to_roman(49)
        self.assertEqual(resultado, 'XLIX')

    def test_cincuenta(self):
        resultado = decimal_to_roman(50)
        self.assertEqual(resultado, 'L')
    
    def test_cincosiete(self):
        resultado = decimal_to_roman(57)
        self.assertEqual(resultado, 'LVII')
    
    def test_seisocho(self):
        resultado = decimal_to_roman(68)
        self.assertEqual(resultado, 'XLVIII')

    def test_noventa(self):
        resultado = decimal_to_roman(90)
        self.assertEqual(resultado, 'XC')  

    def test_nuevetres(self):
        resultado = decimal_to_roman(93)
        self.assertEqual(resultado, 'XCIII') 


if __name__ == '__main__':
    unittest.main()