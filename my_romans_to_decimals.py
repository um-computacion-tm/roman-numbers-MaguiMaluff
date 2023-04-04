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

if __name__ == '__main__':
    unittest.main()
