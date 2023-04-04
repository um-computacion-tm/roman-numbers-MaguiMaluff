import unittest
from my_decimal_to_roman import decimal_to_roman
from my_romans_to_decimals import roman_to_decimal

#Tests de decimal_to_roman
class TestDecimalToRoman(unittest.TestCase):
    def test_1(self):
        resultado = decimal_to_roman(1)
        self.assertEqual(resultado, 'I')
    def test_0(self):
        resultado = decimal_to_roman(0)
        self.assertEqual(resultado, '0')
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
    def test_300(self):
        resultado = decimal_to_roman(300)
        self.assertEqual(resultado, 'CCC')
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

#Tests de romans_to_decimals
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