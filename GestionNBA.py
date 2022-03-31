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
    print("----------------------------------------------------")
    print("ＭＡＮＴＥＮＩＭＩＥＮＴＯ  ＤＥ  ＪＵＧＡＤＯＲＥＳ")
    print("----------------------------------------------------")
    print("")
    print("・1. Insertar jugador")
    print("・2. Eliminar jugador")
    print("・3. Modificar jugador")
    print("・4. Datos del jugador")
    print("・5. Listar la tabla")
    print("・X. Salir")
    print("")
    pregunta = input("Elija opción: ")
    preguntas()

def insertar():
    borrado()
    vader.execute("SELECT max(codigo) from jugadores")
    codigo_sql = vader.fetchone()
    for x in codigo_sql:
        codigo = int(x+1)
    print("----------------------------------")
    print("ＩＮＳＥＲＴＡＲ  ＪＵＧＡＤＯＲ")
    print("----------------------------------")
    print("")
    nombre = input("・Nombre del jugador: ")
    procedencia = input("・Procedencia del jugador: ")
    altura = input("・Altura del jugador: ")
    peso = input("・Peso del jugador: ")
    posicion = input("・Posicion del jugador: ")
    equipo = input("・Equipo del jugador: ")

    sql = "INSERT INTO jugadores VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = codigo, nombre, procedencia, altura, peso, posicion, equipo
    vader.execute(sql, val)
    nba.commit()
    print("")
    print("Se ha agregado correctamente al jugador")
    time.sleep(5)
    borrado()
    preguntado()

def eliminar():
    borrado()
    print("----------------------------------")
    print("ＥＬＩＭＩＮＡＲ  ＪＵＧＡＤＯＲ")
    print("----------------------------------")
    print("")
    nombre = input("・Nombre del jugador: ")

    sql = "DELETE FROM jugadores WHERE (Nombre = %s)"
    vader.execute(sql, nombre)
    nba.commit()
    print("")
    print("Se ha borrado correctamente al jugador")
    time.sleep(5)
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
        'X': salir,
        'x': salir
    }
    preguntas.get(pregunta, error)()

borrado()
preguntado()
