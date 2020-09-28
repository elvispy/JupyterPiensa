with open('data3.txt', 'r+') as archivo:
    print("El puntero está en la posición: ", archivo.tell())
    print(archivo.read())
    print(archivo.write('hola'))
    print("-------------")
    archivo.seek(0)
    print("El puntero está ahora en la posición :", archivo.read())
