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

def decimales(decimal):
    deci = ''
    if decimal >= 10 and decimal < 40:
        decimalinicial = decimal / 10
        unidadfinal = unidad_decimal(decimal) 
        deci = ("X" * int(decimalinicial)) + unidadfinal
    ## del 40 al 49
    elif decimal >= 40 and decimal < 50:
        unidadfinal = unidad_decimal(decimal)
        deci = "XL" + unidadfinal
    # del 50 al 89
    elif decimal >= 50  and decimal < 90:
        unidadfinal = unidad_decimal(decimal)
        deci = "L" + ("X" * int((decimal/10) - 5)) + unidadfinal
    ## del 90 al 99
    elif decimal >= 90 and decimal < 100:
        unidadfinal = unidad_decimal(decimal)
        deci = "XC" + unidadfinal
    return deci

def centenas(decimal):
    centenainicial = decimal // 100
    centena = ''
    if centenainicial >= 2 and centenainicial < 4:
        centena = "C" * int(centenainicial)
    elif centenainicial == 4:
        centena = "CD"
    elif centenainicial >= 5 and centenainicial < 9:
        centena = "D" + "C" * int(centenainicial - 5)
    elif centenainicial == 9:
        centena = "CM"
    elif centenainicial == 10:
        centena = "M"
    elif centenainicial == 1:
        centena = "C"
    return centena

def decimal_to_roman(decimal):
    ## de 0 a 9
    if decimal < 10:
        unidadtotal = unidad_decimal(decimal)
        return unidadtotal
    ###del 10 al 99
    elif decimal >= 10 and decimal < 100:
        decenatotal = decimales(decimal)
        return decenatotal
    ## del 100 al 1000
    elif decimal >= 100 and decimal <= 1000:
        tipo = decimal - (decimal // 100)*100
        if tipo < 10:
            centenatotal = centenas(decimal)
            unidadtotal = unidad_decimal(tipo)
            return centenatotal + unidadtotal
        else:
            centenatotal = centenas(decimal)
            decenatotal = decimales(tipo)
            return centenatotal + decenatotal
        
## decimal decimal / 10 y unidad decimal % 10

class TestDecimalToRoman(unittest.TestCase):
    def test_uno(self):
        # pre condicion
        ### NO HAY ###
        # proceso
        resultado = decimal_to_roman(1)
        # verificacion
        self.assertEqual(resultado, 'I')
    def test_2(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado, 'II')
    def test_3(self):
        resultado = decimal_to_roman(3)
        self.assertEqual(resultado, 'III')
    def test_10(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, 'X')
    def test_5(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, 'V')
    def test_6(self):
        resultado = decimal_to_roman(6)
        self.assertEqual(resultado, 'VI')
    def test_7(self):
        resultado = decimal_to_roman(7)
        self.assertEqual(resultado, 'VII')
    def test_8(self):
        resultado = decimal_to_roman(8)
        self.assertEqual (resultado, 'VIII')
    def test_30(self):
        resultado = decimal_to_roman(30)
        self.assertEqual(resultado, 'XXX')
    def test_20(self):
        resultado = decimal_to_roman(20)
        self.assertEqual(resultado, 'XX')
    def test_19(self):
        resultado = decimal_to_roman(19)
        self.assertEqual(resultado, 'XIX')
    def test_23(self):
        resultado = decimal_to_roman(23)
        self.assertEqual(resultado, 'XXIII')
    def test_39(self):
        resultado = decimal_to_roman(39)
        self.assertEqual(resultado, 'XXXIX')
    def test_40(self):
        resultado = decimal_to_roman(40)
        self.assertEqual(resultado, 'XL')
    def test_43(self):
        resultado = decimal_to_roman(43)
        self.assertEqual(resultado, 'XLIII')
    def test_49(self):
        resultado = decimal_to_roman(49)
        self.assertEqual(resultado, 'XLIX')
    def test_50(self):
        resultado = decimal_to_roman(50)
        self.assertEqual(resultado, 'L')
    def test_57(self):
        resultado = decimal_to_roman(57)
        self.assertEqual(resultado, 'LVII')
    def test_68(self):
        resultado = decimal_to_roman(68)
        self.assertEqual(resultado, 'LXVIII')
    def test_90(self):
        resultado = decimal_to_roman(90)
        self.assertEqual(resultado, 'XC')  
    def test_93(self):
        resultado = decimal_to_roman(93)
        self.assertEqual(resultado, 'XCIII') 
    def test_100(self):
        resultado = decimal_to_roman(100)
        self.assertEqual(resultado, 'C') 
    def test_103(self):
        resultado = decimal_to_roman(103)
        self.assertEqual(resultado, 'CIII')
    def test_105(self):
        resultado = decimal_to_roman(105)
        self.assertEqual(resultado, 'CV')
    def test_110(self):
        resultado = decimal_to_roman(110)
        self.assertEqual(resultado, 'CX')
    def test_203(self):
        resultado = decimal_to_roman(203)
        self.assertEqual(resultado, 'CCIII')
    def test_155(self):
        resultado = decimal_to_roman(155)
        self.assertEqual(resultado, 'CLV')
    def test_439(self):
        resultado = decimal_to_roman(439)
        self.assertEqual(resultado, 'CDXXXIX')
    def test_524(self):
        resultado = decimal_to_roman(524)
        self.assertEqual(resultado, 'DXXIV')
    def test_689(self):
        resultado = decimal_to_roman(689)
        self.assertEqual(resultado, 'DCLXXXIX')
    def test_789(self):
        resultado = decimal_to_roman(789)
        self.assertEqual(resultado, 'DCCLXXXIX')
    def test_712(self):
        resultado = decimal_to_roman(712)
        self.assertEqual(resultado, 'DCCXII')
    def test_891(self):
        resultado = decimal_to_roman(891)
        self.assertEqual(resultado, 'DCCCXCI')
    def test_907(self):
        resultado = decimal_to_roman(907)
        self.assertEqual(resultado, 'CMVII')
    def test_999(self):
        resultado = decimal_to_roman(999)
        self.assertEqual(resultado, 'CMXCIX')
    def test_1000(self):
        resultado = decimal_to_roman(1000)
        self.assertEqual(resultado, 'M')

if __name__ == '__main__':
    unittest.main()