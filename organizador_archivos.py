import os
import shutil

contador = 0

ruta = input("Ingrese la ruta: ")

if not os.path.exists(ruta):
    print("Ruta no válida")
    exit()

archivos = os.listdir(ruta)

for archivo in archivos:

    origen = os.path.join(ruta, archivo)

    if os.path.isdir(origen):
        continue

    nombre = archivo.lower()

    if nombre.endswith(".pdf"):
        carpeta = "Pdfs"
    elif nombre.endswith(".xlsx"):
        carpeta = "Excel"
    elif nombre.endswith(".jpeg") or nombre.endswith(".png") or nombre.endswith(".jpg"):
        carpeta = "Imagenes"
    elif nombre.endswith(".doc") or nombre.endswith(".docx"):
        carpeta = "Docs"
    elif nombre.endswith(".mp4"):
        carpeta = "Videos"
    elif nombre.endswith(".html") or nombre.endswith(".htm"):
        carpeta = "Html"
    elif nombre.endswith(".exe"):
        carpeta = "Exe"
    else:
        continue

    carpeta_destino = os.path.join(ruta, carpeta)

    if not os.path.exists(carpeta_destino):
        os.mkdir(carpeta_destino)

    destino = os.path.join(carpeta_destino, archivo)

    if os.path.exists(destino):
        print(f"{archivo} ya existe, se omite")
        continue

    print(f"Moviendo: {archivo} → {carpeta}")
    shutil.move(origen, destino)
    contador += 1

print("\nSe movieron", contador, "archivos")
