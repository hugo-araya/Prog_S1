def lee_datos(nombre):
    ar = open(nombre)
    lista = []
    linea = ar.readline()
    for linea in ar:
        linea = linea.rstrip("\n")
        lista.append(linea)
    return lista

def desorden(cadena):
    return 1

def proceso(cadenas):
    # cadenas es una lista de string
    # cadenas_procesadas es un lista de listas (cadena, desorden)
    cadenas_procesadas = []
    for cadena in cadenas:
        des = desorden(cadena)
        cadenas_procesadas.append([cadena, des])
    return cadenas_procesadas

        # puede ser una lista de listas o un diccionario
    return # Las cadenas con su respetivo desorden

def ordenar(cadenas_procesadas):
    pass

def escribir_archivo(nombre, cadenas_ordenadas):
    pass

if __name__ == "__main__":
    cadenas = lee_datos("ADN.DAT") # Retorna una lista de cadenas
    cadenas_procesadas = proceso(cadenas)
    print (cadenas_procesadas)
    cadenas_ordenadas = ordenar(cadenas_procesadas)
    escribir_archivo("ADN.RES", cadenas_ordenadas)

