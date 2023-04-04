
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
    elif decimal == 0:
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
    if decimal == 0:
        return "0"
    elif decimal < 10:
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


if __name__ == '__main__':
    print(decimal_to_roman(1))
    
#print(decimal2roman(1)) ##imprime lo que devuelve la funcion cuando number es 1