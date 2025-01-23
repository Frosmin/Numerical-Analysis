# Decimal al binario 
def dec_bin(n):
    if n == 0:
        return '0'
    else:
        return dec_bin(n//2) + str(n%2)
def decimal_a_binario(decimal, precision=64):
    parte_entera = int(decimal)
    parte_decimal = decimal - parte_entera
    binario_entero = dec_bin(parte_entera)
    binario_decimal = ""
    while parte_decimal > 0 and len(binario_decimal) < precision:
        parte_decimal *= 2
        if parte_decimal >= 1:
            binario_decimal += "1"
            parte_decimal -= 1
        else:
            binario_decimal += "0"
    if parte_decimal == 0:
        return f"{binario_entero}.{binario_decimal}"
    else:
        return f"{binario_entero}.{binario_decimal}"  
# Binario a decimal
def bin_dec(n):
    return int(n, 2)
def binario_a_decimal(binario):
    partes = binario.split('.')
    parte_entera = partes[0]
    parte_decimal = partes[1] if len(partes) > 1 else "0"
    decimal_entero = int(parte_entera, 2)
    decimal_fraccionario = 0
    for i in range(len(parte_decimal)):
        decimal_fraccionario += int(parte_decimal[i]) * (2 ** -(i + 1))
    return decimal_entero + decimal_fraccionario


print("Binario a decimal")
print(f"(1)" + " " +dec_bin(132))
print(f"(2)" + " " +dec_bin(524))
print(f"(3)" + " " +dec_bin(1235))
print(f"(4)" + " " +decimal_a_binario(0.7656))
print(f"(4)" + " " +decimal_a_binario(0.34))

print("decimal a binario")
print(f"(1)" + " " + str(bin_dec("1011")))
print(f"(2)" + " " + str(bin_dec("1110010")))
print(f"(3)" + " " + str(binario_a_decimal("1001.00101")))



