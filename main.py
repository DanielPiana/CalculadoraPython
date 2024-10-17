#Hacemos 4 funciones, cuya utilidad será sumar, restar,
# multiplicar o dividir dos números que le pasemos

def restar(num1,num2):
    return num1 - num2
def multiplicar(num1,num2):
    return num1 * num2
def dividir(num1,num2):
    #Como una división entre 0 no tiene sentido, lo ponemos como excepción
    if num2 != 0:
        return num1 / num2
    else:
        return "Se ha intentado dividir entre 0"

#Creo un diccionario para asignar un numero y un nombre a una acción (Switch en java)
#Las claves (1,2,3,4) representar numeros que el usuario puede elegir para decidir que operación hacer
#Los valores se acceden como posiciones en un Array
#valor[0] es la primera posición, accederá al nombre que le hemos puesto a la operación (Suma,Resta,Multiplicacion,Division)
#valor[1] es la segunda posición, accederá a la funcion que realiza las operaciones definidas previamente
operaciones = {
    "1":("Suma",lambda num1,num2:num1+num2),
    "2":("Resta",restar),
    "3":("Multiplicacion",multiplicar),
    "4":("Dividir",dividir)
    }

def calculadora():
    #Creo una colección donde iremos guardando todas las operaciones que haga el usuario
    historial = []
    while True:
        print("Que operación desea realizar?")
        #Creamos un bucle que recorre operaciones e imprima el numero de opciones que tiene disponibles (1,2,3,4) con su nombre
        #Básicamente como un foreach en java para recorrer una colección
        for clave,valor in operaciones.items():
            print(f"{clave}: {valor[0]}")

        #opcion es la opción que elegira el usuario
        opcion = input("Opción: ")

        #Con el if comprobamos si la opcion ingresada por el usuario existe en nuestro diccionario de operaciones
        #Si es válida se guardará en la variable opcion
        if opcion in operaciones:
            #Guardamos los 2 numeros elegidos por el usuario
            #Ponemos un try except para controlar que no ponga algo que no sea un número
            try:
                num1 = float(input("Escriba el primer número: "))
                num2 = float(input("Escriba el segundo número: "))
            except ValueError:
                print("Por favor, introduzca números válidos")
                continue #Si da error imprimimos un mensaje y con continue volvemos al principio del bucle
            #Guardamos el resultado en una variable
            #Accedemos al segundo elemento [1] (el metodo) con la opción proporcionada con el usuario (opcion)
            #Con los parametros proporcionados por el usuario también (num1,num2)
            resultado = operaciones[opcion][1](num1,num2)
            print(f"Resultado: {resultado}")
            #Ahora guardamos los detalles de la operación para llevar un historial
            historial.append(f"{operaciones[opcion][0]} de {num1} y {num2} es: {resultado}")
        else:
            print("Opción no reconocida")
            #Ya finalizado el proceso preguntamos al usuario si quiere seguir realizando operaciones
            seguir = input("¿Quiere seguir? (Si/No)")
            #Hacemos que lo que haya escrito se transforme en mayusculas para evitar que sea case sensitive
            #Y si la respuesta es diferente a si hacemos un break y se acaba el bucle, por tanto se cierra el programa
            if seguir.capitalize() != "Si":
                break
calculadora() #Ejecutamos la aplicacion