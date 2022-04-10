import mysql.connector
import os
import time

nba = mysql.connector.connect(
    host="localhost",
    user="root",
    password="B00le",
    database="nba"
)

vader = nba.cursor()

def borrado():
    os.system("cls")

def preguntado():
    global pregunta
    print("--------------------------")
    print("MANTENIMIENTO DE JUGADORES")
    print("--------------------------")
    print("")
    print("· 1. Insertar jugador")
    print("· 2. Eliminar jugador")
    print("· 3. Modificar jugador")
    print("· 4. Datos del jugador")
    print("· 5. Listar la tabla")
    print("· X. Salir")
    print("")
    pregunta = input("Elija opción: ")
    preguntas()

def askpeso():
    global peso
    try:
        peso = int(input("· Peso del jugador: "))
    except:
        print("")
        print("El peso tiene que ser un valor numérico")
        print("")
        askpeso()

def askequipo():
    global equipo
    try: 
        equipo = input("· Equipo del jugador: ")
    except:
        lista = []
        vader.execute("SELECT Nombre FROM equipos")
        codigo_sql = vader.fetchall()
        print("")
        print("Sólo puedes poner uno de los siguientes equipos:")
        for x in codigo_sql:
            lista.append(x)
        lista2 = str(lista)
        lista3 = lista2.replace(",", "").replace('"', '').replace("'", '').replace("(", "").replace(")", "").replace(" ", " | ")
        print(lista3)
        print("")
        askequipo()
        
def insertar():
    borrado()
    vader.execute("SELECT max(codigo) from jugadores")
    codigo_sql = vader.fetchone()
    for x in codigo_sql:
        codigo = int(x+1)
    print("----------------")
    print("INSERTAR JUGADOR")
    print("----------------")
    print("")
    
    nombre = input("· Nombre del jugador: ")
    procedencia = input("· Procedencia del jugador: ")
    altura = input("· Altura del jugador: ")
    askpeso()
    posicion = input("· Posicion del jugador: ")
    askequipo()

    sql = "INSERT INTO jugadores VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = codigo, nombre, procedencia, altura, peso, posicion, equipo
    vader.execute(sql, val)
    nba.commit()
    print("")
    print("Se ha agregado correctamente al jugador")
    time.sleep(3)
    borrado()
    preguntado()

def eliminar():
    borrado()
    print("----------------")
    print("ELIMINAR JUGADOR")
    print("----------------")
    print("")
    nombre = input("· Nombre del jugador: ")

    sql = "DELETE FROM jugadores WHERE Nombre LIKE %s"
    val = (nombre, )
    vader.execute(sql, val)
    nba.commit()
    print("")
    print("Se ha borrado correctamente al jugador")
    time.sleep(3)
    borrado()
    preguntado()

def modificar():
    borrado()
    print("-----------------")
    print("MODIFICAR JUGADOR")
    print("-----------------")
    print("")
    oldnombre = input("· Indícame el nombre del jugador que deseas modificar: ")
    print("")
    vader.execute(f"SELECT codigo FROM jugadores WHERE Nombre LIKE '{oldnombre}'")
    codigo_sql = vader.fetchone()
    for x in codigo_sql:
        codigo = x
    print(codigo)
    nombre = input("· Nombre del jugador: ")
    procedencia = input("· Procedencia del jugador: ")
    altura = input("· Altura del jugador: ")
    askpeso()
    posicion = input("· Posicion del jugador: ")
    askequipo()

    try:
        sql = "UPDATE jugadores SET Nombre = %s, Procedencia = %s, Altura = %s, Peso = %s, Posicion = %s, Nombre_equipo = %s WHERE Nombre LIKE %s OR codigo = %s"
        val = (nombre, procedencia, altura, peso, posicion, equipo, oldnombre, codigo)
        vader.execute(sql, val)
        nba.commit()
        print("")
        print("Se ha editado correctamente al jugador")
    except mysql.connector.IntegrityError as e:
        print("Error: {}".format(e))
        return {"message": e}
        time.sleep(3)
        modificar()
    time.sleep(3)
    borrado()
    preguntado()

def error():
    borrado()
    preguntado()
def salir():
    borrado()
    print("Saliendo del programa...")

def preguntas(): 
    preguntas = {
	    '1': insertar,
        '2': eliminar,
        '3': modificar,
        'X': salir,
        'x': salir
    }
    preguntas.get(pregunta, error)()

borrado()
preguntado()
