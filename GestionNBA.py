import mysql.connector
import os
import time

nba = mysql.connector.connect(host="localhost", user="root", password="B00le", database="nba")
vader = nba.cursor()

def borrado():
    os.system("cls")

def preguntado():
    global pregunta
    print("--------------------------\nMANTENIMIENTO DE JUGADORES\n--------------------------\n")
    print("· 1. Insertar jugador\n· 2. Eliminar jugador\n· 3. Modificar jugador\n· 4. Datos del jugador\n· 5. Listar la tabla\n· X. Salir\n")
    pregunta = input("Elija opción: ")
    preguntas()

def askpeso():
    global peso
    try:
        peso = int(input("· Peso del jugador: "))
    except:
        print("\nEl peso tiene que ser un valor numérico\n")
        askpeso()

def askequipo():
    global equipo
    equipo = input("· Equipo del jugador: ")

def exceptequipo():
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

# ---------------------
# 1. INSERTAR JUGADORES
# ---------------------

def insertar():
    borrado()
    vader.execute("SELECT max(codigo) from jugadores")
    codigo_sql = vader.fetchone()
    for x in codigo_sql:
        codigo = int(x+1)
    print("----------------\nINSERTAR JUGADOR\n----------------\n")
    
    nombre = input("· Nombre del jugador: ")
    procedencia = input("· Procedencia del jugador: ")
    altura = input("· Altura del jugador: ")
    askpeso()
    posicion = input("· Posicion del jugador: ")
    askequipo()
    while cosita == True:
        try:
            sql = "INSERT INTO jugadores VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = codigo, nombre, procedencia, altura, peso, posicion, equipo
            vader.execute(sql, val)
            nba.commit()
            print("\nSe ha agregado correctamente al jugador")
            time.sleep(2)
            borrado()
            preguntado()
            insertame = False
        except mysql.connector.IntegrityError:
            exceptequipo()

# ---------------------
# 2. ELIMINAR JUGADORES
# ---------------------

def eliminar():
    borrado()
    print("----------------\nELIMINAR JUGADOR\n----------------\n")
    nombre = input("· Nombre del jugador: ")
    sql = "SELECT * FROM jugadores WHERE Nombre LIKE %s"
    val = (nombre, )
    vader.execute(sql, val)
    codigo_sql = vader.fetchall()
    for x in codigo_sql:
        print(f"\n{x}")
        accion = 'No se'
        while accion != 'S' or 'N':
            accion = input("\n¿Deseas eliminar a este jugador?\n· Si = S\n· No = N\n\nOpción: ")
            if accion == 'S':
                sql = "DELETE FROM jugadores WHERE Nombre LIKE %s"
                vader.execute(sql, val)
                nba.commit()
                print("\nSe ha borrado correctamente al jugador")
                time.sleep(2)
                borrado()
                preguntado()
            elif accion == 'N':
                print("\nSaliendo de Eliminar Jugador")
                time.sleep(2)
                borrado()
                preguntado()

# ---------------------
# 3. INSERTAR JUGADORES
# ---------------------

def modificar():
    borrado()
    print("-----------------\nMODIFICAR JUGADOR\n-----------------\n")
    oldnombre = input("· Indícame el nombre del jugador que deseas modificar: ")
    vader.execute(f"SELECT codigo FROM jugadores WHERE Nombre LIKE '{oldnombre}'")
    codigo_sql = vader.fetchone()
    for x in codigo_sql:
        codigo = x
    vader.execute(f"SELECT * FROM jugadores WHERE Codigo = '{codigo}'")
    codigo_sql2 = vader.fetchall()
    for y in codigo_sql2:
        print(f"\n{y}")
    accion = 'No se'
    while accion != 'S' or 'N':
        accion = input("\n¿Deseas modificar a este jugador?\n· Si = S\n· No = N\n\nOpción: ")
        if accion == 'S':
            cosita = True
            nombre = input("· Nombre del jugador: ")
            procedencia = input("· Procedencia del jugador: ")
            altura = input("· Altura del jugador: ")
            askpeso()
            posicion = input("· Posicion del jugador: ")
            askequipo()
            while cosita == True:
                try:
                    sql = "UPDATE jugadores SET Nombre = %s, Procedencia = %s, Altura = %s, Peso = %s, Posicion = %s, Nombre_equipo = %s WHERE Nombre LIKE %s OR codigo = %s"
                    val = (nombre, procedencia, altura, peso, posicion, equipo, oldnombre, codigo)
                    vader.execute(sql, val)
                    nba.commit()
                    print("\nSe ha editado correctamente al jugador")
                    time.sleep(2)
                    borrado()
                    preguntado()
                    cosita = False
                except mysql.connector.IntegrityError:
                    exceptequipo()
        elif accion == 'N':
            print("\nSaliendo de Modificar Jugador")
            time.sleep(2)
            borrado()
            preguntado()

# ---------------------
# 4. DATOS DEL JUGADOR
# ---------------------

def datos():
    borrado()
    print("-----------------\nDATOS DEL JUGADOR\n-----------------\n")
    nombre = input("· Indícame el nombre del jugador que deseas ver sus datos: ")
    vader.execute(f"SELECT * FROM jugadores WHERE Nombre LIKE '{nombre}'")
    codigo_sql = vader.fetchall()
    jugador = []
    for x in codigo_sql:
        jugador.append(x)
    print(jugador)
def preguntas(): 
    preguntas = {
	    '1': insertar,
        '2': eliminar,
        '3': modificar,
        '4': datos,
        'X': salir,
        'x': salir
    }
    preguntas.get(pregunta, error)()
def error():
    borrado()
    preguntado()
def salir():
    borrado()
    print("Saliendo del programa...")
cosita = True
borrado()
preguntado()
