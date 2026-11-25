print("EL ARCHIVO SE ESTÁ EJECUTANDO")

def analizar_texto(ruta_archivo):

    # Leer archivo
    archivo = open(ruta_archivo, "r", encoding="utf-8")
    texto = archivo.read()
    archivo.close()

    # Eliminar saltos de línea para contar caracteres
    caracteres = texto.replace("\n", "").replace("\r", "")
    total_caracteres = len(caracteres)

    # Convertir texto a minúsculas y separar palabras
    palabras = texto.lower().split()
    total_palabras = len(palabras)

    # Contar frecuencia de cada palabra
    frecuencias = {}

    for palabra in palabras:
        palabra = palabra.strip(".,;:!?¿¡()[]{}\"'")

        if palabra != "":
            if palabra in frecuencias:
                frecuencias[palabra] += 1
            else:
                frecuencias[palabra] = 1

    # Ordenar por frecuencia y alfabéticamente
    resultado = sorted(
        frecuencias.items(),
        key=lambda x: (-x[1], x[0])
    )

    # Mostrar resultados
    print("Cantidad de palabras:", total_palabras)
    print("Cantidad de caracteres:", total_caracteres)

    print("\nHistograma:")

    for palabra, cantidad in resultado:
        print(palabra, ":", cantidad, "*" * cantidad)


analizar_texto("data/texto_prueba.txt")
