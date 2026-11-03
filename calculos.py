import datos
def calcular_total():
    return sum(datos.gastos)
print(calcular_total)

def calcular_saldo(total):
    resultado = datos.presupuesto - total
    return resultado