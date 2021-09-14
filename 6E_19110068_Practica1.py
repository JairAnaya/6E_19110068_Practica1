"""
        Jair Shiblón Anaya Rodríguez
                19110068
               Práctica 1
            Sistemas Expertos
                  6E6
"""
import random

nombre = input("Para poder llamarte por tu nombre de detective, ingrésalo enseguida: ")

personajes = ["CAZADOR", "LENADOR", "CARNICERO", "CHOLO", "MAYORDOMO"] #Asignación de personajes
lugares = ["COCINA", "GRANERO", "PATIO", "RECAMARA", "SALA"] #Asignación de lugares
arma = ["DAGA", "HACHA", "MACHETE", "LANZA", "NAVAJA"] #Asignación de armas
asesino = []
pruebaP = personajes.copy()
pruebaL = lugares.copy()
pruebaA = arma.copy()
pista1 = []
pista2 = []
pista3 = []
pista4 = []

##print(pruebaP, pruebaL, pruebaA)
print("\nHace unos días se vio un oso cerca de la casa de campo de Mr. Cluff, el amo de una mansión, por lo que se pidió que fuera un cazador y se le habló a Michael el cazador, ha estado unos días ya en los alrededores de la mansión;\na unos kilómetros se encuentra Lenny el leñador, quien últimamente se había estado viendo con Mr. Cluff para ver algunos asuntos de dinero, al parecer no han quedado bien;\nla comida en la mansión siempre es comida fresca, por lo que desde hace años Mr. Cluff ha contratado a Parker el carnicero para que haya carne fresca;\ntambién se encuentra un vagabundo a quien llaman Freddy el cholo por su forma de vestir, se cree que ha querido adueñarse de la casa desde hace mucho tiempo;\npor último tenemos a Ricky, el mayordomo, quien tiene a su nombre la herencia de todas las posesiones de Mr. Cluff")

print("\nEl día de hoy se encontró a Mr.Cluff asesinado, tu deber será encontrar quién fue el asesino, en dónde realizó el asesinato y con qué arma fue realizado, para hacerlo contarás con 5 oportunidades en las que podrás preguntar para obtener las pistas necesarias, mucha suerte, encontrar al asesino depende de ti", nombre); #Descripción de lo sucedido

#Se elige aleatoriamente personaje, lugar, arma, se repite para elegir las 5 historias
itemPers = random.choice(personajes)
itemLug = random.choice(lugares)
itemArma = random.choice(arma)

pruebaP.remove(itemPers)
pruebaL.remove(itemLug)
pruebaA.remove(itemArma)

itemPers2 = random.choice(pruebaP)
itemLug2 = random.choice(pruebaL)
itemArma2 = random.choice(pruebaA)

pista1.append(itemPers2)
pista1.append(itemLug2)
pista1.append(itemArma2)

pruebaP.remove(itemPers2)
pruebaL.remove(itemLug2)
pruebaA.remove(itemArma2)

itemPers3 = random.choice(pruebaP)
itemLug3 = random.choice(pruebaL)
itemArma3 = random.choice(pruebaA)

pista2.append(itemPers3)
pista2.append(itemLug3)
pista2.append(itemArma3)

pruebaP.remove(itemPers3)
pruebaL.remove(itemLug3)
pruebaA.remove(itemArma3)

itemPers4 = random.choice(pruebaP)
itemLug4 = random.choice(pruebaL)
itemArma4 = random.choice(pruebaA)

pista3.append(itemPers4)
pista3.append(itemLug4)
pista3.append(itemArma4)

pruebaP.remove(itemPers4)
pruebaL.remove(itemLug4)
pruebaA.remove(itemArma4)

itemPers5 = random.choice(pruebaP)
itemLug5 = random.choice(pruebaL)
itemArma5 = random.choice(pruebaA)

pista4.append(itemPers5)
pista4.append(itemLug5)
pista4.append(itemArma5)

    #Guarda al asesino, lugar y arma en una nueva lista, es el asesino que deben adivinar
asesino.append(itemPers)
asesino.append(itemLug)
asesino.append(itemArma)
##print(asesino)

if itemPers == "CAZADOR":
    nomAses = "MICHAEL"
if itemPers == "LENADOR":
    nomAses = "LENNY"
if itemPers == "CARNICERO":
    nomAses = "PARKER"
if itemPers == "CHOLO":
    nomAses = "FREDDY"
if itemPers == "MAYORDOMO":
    nomAses = "RICKY"

##print(itemPers)
##print(itemLug)
##print(itemArma)
class Switcher(object):
    def service_switcher(self, argument, elecciones):
##        Dispatch method
        method_name = 'case_' + str(argument)
        method = getattr(self, method_name, "INVALIDO")       
        if method == "INVALIDO":
           return method
        return method(method_name)

    def case_a(self, eleccion):
         choosing = int(input("\nElija un personaje:\n1.Cazador\n2.Leñador\n3.Carnicero\n4.Cholo\n5.Mayordomo\n"));
         if choosing == 1:
             opcion = "CAZADOR"
             if opcion == asesino[0]:
                 print("El", asesino[0], "fue visto en", asesino[1], "y traía en su mano un arma:", asesino[2])
             elif opcion == pista1[0]:
                 print("El", pista1[0], "no fue visto en", pista4[1], "y traía en su mano un arma:", pista1[2])
             elif opcion == pista2[0]:
                 print("El", pista2[0], "fue visto en", pista2[1], "y nunca se le vio el arma:", pista3[2])
             elif opcion == pista3[0]:
                 print("El", pista3[0], "fue visto en", pista3[1], "y nunca se le vio el arma:", pista2[2])
             elif opcion == pista4[0]:
                 print("El", pista4[0], "no fue visto en", pista1[1], "y traía en su mano un arma:", pista4[2])
         elif choosing == 2:
             opcion2 = "LENADOR"
             if opcion2 == asesino[0]:
                 print("El", asesino[0], "fue visto en", asesino[1], "y traía en su mano un arma:", asesino[2])
             elif opcion2 == pista1[0]:
                 print("El", pista1[0], "no fue visto en", pista4[1], "y traía en su mano un arma:", pista1[2])
             elif opcion2 == pista2[0]:
                 print("El", pista2[0], "fue visto en", pista2[1], "y nunca se le vio el arma:", pista3[2])
             elif opcion2 == pista3[0]:
                 print("El", pista3[0], "fue visto en", pista3[1], "y nunca se le vio el arma:", pista2[2])
             elif opcion2 == pista4[0]:
                 print("El", pista4[0], "no fue visto en", pista1[1], "y traía en su mano un arma:", pista4[2])
         elif choosing == 3:
             opcion3 = "CARNICERO"
             if opcion3 == asesino[0]:
                 print("El", asesino[0], "fue visto en", asesino[1], "y traía en su mano un arma:", asesino[2])
             elif opcion3 == pista1[0]:
                 print("El", pista1[0], "no fue visto en", pista4[1], "y traía en su mano un arma:", pista1[2])
             elif opcion3 == pista2[0]:
                 print("El", pista2[0], "fue visto en", pista2[1], "y nunca se le vio el arma:", pista3[2])
             elif opcion3 == pista3[0]:
                 print("El", pista3[0], "fue visto en", pista3[1], "y nunca se le vio el arma:", pista2[2])
             elif opcion3 == pista4[0]:
                 print("El", pista4[0], "no fue visto en", pista1[1], "y traía en su mano un arma:", pista4[2])
         elif choosing == 4:
             opcion4 = "CHOLO"
             if opcion4 == asesino[0]:
                 print("El", asesino[0], "fue visto en", asesino[1], "y traía en su mano un arma:", asesino[2])
             elif opcion4 == pista1[0]:
                 print("El", pista1[0], "no fue visto en", pista4[1], "y traía en su mano un arma:", pista1[2])
             elif opcion4 == pista2[0]:
                 print("El", pista2[0], "fue visto en", pista2[1], "y nunca se le vio el arma:", pista3[2])
             elif opcion4 == pista3[0]:
                 print("El", pista3[0], "fue visto en", pista3[1], "y nunca se le vio el arma:", pista2[2])
             elif opcion4 == pista4[0]:
                 print("El", pista4[0], "no fue visto en", pista1[1], "y traía en su mano un arma:", pista4[2])
         elif choosing == 5:
             opcion5 = "MAYORDOMO"
             if opcion5 == asesino[0]:
                 print("El", asesino[0], "fue visto en", asesino[1], "y traía en su mano un arma:", asesino[2])
             elif opcion5 == pista1[0]:
                 print("El", pista1[0], "no fue visto en", pista4[1], "y traía en su mano un arma:", pista1[2])
             elif opcion5 == pista2[0]:
                 print("El", pista2[0], "fue visto en", pista2[1], "y nunca se le vio el arma:", pista3[2])
             elif opcion5 == pista3[0]:
                 print("El", pista3[0], "fue visto en", pista3[1], "y nunca se le vio el arma:", pista2[2])
             elif opcion5 == pista4[0]:
                 print("El", pista4[0], "no fue visto en", pista1[1], "y traía en su mano un arma:", pista4[2])
         return eleccion
  
    def case_b(self, eleccion):
         choosing2 = int(input("\nElija un lugar:\n1.Cocina\n2.Granero\n3.Patio\n4.Recámara\n5.Sala\n"));
         if choosing2 == 1:
             opcion = "COCINA"
             if opcion == asesino[1]:
                 print("En el lugar:", asesino[1], "fue visto el", asesino[0], "y traía en su mano un arma:", asesino[2])
             if opcion == pista1[1]:
                 print("En el lugar:", pista1[1], "nunca se vio a", asesino[0], "pero estaba el arma:", pista1[2])
             if opcion == pista2[1]:
                 print("En el lugar:", pista2[1], "fue visto el", pista2[0], "y traía en su mano un arma:", pista2[2])
             if opcion == pista3[1]:
                 print("En el lugar:", pista3[1], "fue visto el", pista3[0], "y no se vio el arma:", asesino[2])
             if opcion == pista4[1]:
                 print("En el lugar:", pista4[1], "fue visto el", pista4[0], "y traía en su mano un arma:", pista4[2])
         if choosing2 == 2:
             opcion = "GRANERO"
             if opcion == asesino[1]:
                 print("En el lugar:", asesino[1], "fue visto el", asesino[0], "y traía en su mano un arma:", asesino[2])
             if opcion == pista1[1]:
                 print("En el lugar:", pista1[1], "nunca se vio a", asesino[0], "pero estaba el arma:", pista1[2])
             if opcion == pista2[1]:
                 print("En el lugar:", pista2[1], "fue visto el", pista2[0], "y traía en su mano un arma:", pista2[2])
             if opcion == pista3[1]:
                 print("En el lugar:", pista3[1], "fue visto el", pista3[0], "y no se vio el arma:", asesino[2])
             if opcion == pista4[1]:
                 print("En el lugar:", pista4[1], "fue visto el", pista4[0], "y traía en su mano un arma:", pista4[2])
         if choosing2 == 3:
             opcion = "PATIO"
             if opcion == asesino[1]:
                 print("En el lugar:", asesino[1], "fue visto el", asesino[0], "y traía en su mano un arma:", asesino[2])
             if opcion == pista1[1]:
                 print("En el lugar:", pista1[1], "nunca se vio a", asesino[0], "pero estaba el arma:", pista1[2])
             if opcion == pista2[1]:
                 print("En el lugar:", pista2[1], "fue visto el", pista2[0], "y traía en su mano un arma:", pista2[2])
             if opcion == pista3[1]:
                 print("En el lugar:", pista3[1], "fue visto el", pista3[0], "y no se vio el arma:", asesino[2])
             if opcion == pista4[1]:
                 print("En el lugar:", pista4[1], "fue visto el", pista4[0], "y traía en su mano un arma:", pista4[2])
         if choosing2 == 4:
             opcion = "RECAMARA"
             if opcion == asesino[1]:
                 print("En el lugar:", asesino[1], "fue visto el", asesino[0], "y traía en su mano un arma:", asesino[2])
             if opcion == pista1[1]:
                 print("En el lugar:", pista1[1], "nunca se vio a", asesino[0], "pero estaba el arma:", pista1[2])
             if opcion == pista2[1]:
                 print("En el lugar:", pista2[1], "fue visto el", pista2[0], "y traía en su mano un arma:", pista2[2])
             if opcion == pista3[1]:
                 print("En el lugar:", pista3[1], "fue visto el", pista3[0], "y no se vio el arma:", asesino[2])
             if opcion == pista4[1]:
                 print("En el lugar:", pista4[1], "fue visto el", pista4[0], "y traía en su mano un arma:", pista4[2])
         if choosing2 == 5:
             opcion = "SALA"
             if opcion == asesino[1]:
                 print("En el lugar:", asesino[1], "fue visto el", asesino[0], "y traía en su mano un arma:", asesino[2])
             if opcion == pista1[1]:
                 print("En el lugar:", pista1[1], "nunca se vio a", asesino[0], "pero estaba el arma:", pista1[2])
             if opcion == pista2[1]:
                 print("En el lugar:", pista2[1], "fue visto el", pista2[0], "y traía en su mano un arma:", pista2[2])
             if opcion == pista3[1]:
                 print("En el lugar:", pista3[1], "fue visto el", pista3[0], "y no se vio el arma:", asesino[2])
             if opcion == pista4[1]:
                 print("En el lugar:", pista4[1], "fue visto el", pista4[0], "y traía en su mano un arma:", pista4[2])
         return eleccion
   
    def case_c(self, eleccion):
         choosing3 = int(input("\nElija un arma:\n1.Daga\n2.Hacha\n3.Machete\n4.Lanza\n5.Navaja\n"));
         if choosing3 == 1:
             opcion = "DAGA"
             if opcion == asesino[2]:
                 print("El arma:", asesino[2], "fue vista en:", asesino[1], "y la portaba el", asesino[0])
             if opcion == pista1[2]:
                 print("El arma:", pista1[2], "fue vista en:", pista1[1], "No se vio a", asesino[0])
             if opcion == pista2[2]:
                 print("El arma:", pista2[2], "fue vista en:", pista2[1], "y la portaba el", pista2[0])
             if opcion == pista3[2]:
                 print("El arma:", pista3[2], "pero nunca fue vista en:", asesino[1], "y la portaba el", pista3[0])
             if opcion == pista4[2]:
                 print("El arma:", pista4[2], "fue vista en:", pista4[1], "No se vio a", pista1[0])
         if choosing3 == 2:
             opcion = "HACHA"
             if opcion == asesino[2]:
                 print("El arma:", asesino[2], "fue vista en:", asesino[1], "y la portaba el", asesino[0])
             if opcion == pista1[2]:
                 print("El arma:", pista1[2], "fue vista en:", pista1[1], "No se vio a", asesino[0])
             if opcion == pista2[2]:
                 print("El arma:", pista2[2], "fue vista en:", pista2[1], "y la portaba el", pista2[0])
             if opcion == pista3[2]:
                 print("El arma:", pista3[2], "pero nunca fue vista en:", asesino[1], "y la portaba el", pista3[0])
             if opcion == pista4[2]:
                 print("El arma:", pista4[2], "fue vista en:", pista4[1], "No se vio a", pista2[0])
         if choosing3 == 3:
             opcion = "MACHETE"
             if opcion == asesino[2]:
                 print("El arma:", asesino[2], "fue vista en:", asesino[1], "y la portaba el", asesino[0])
             if opcion == pista1[2]:
                 print("El arma:", pista1[2], "fue vista en:", pista1[1], "No se vio a", asesino[0])
             if opcion == pista2[2]:
                 print("El arma:", pista2[2], "fue vista en:", pista2[1], "y la portaba el", pista2[0])
             if opcion == pista3[2]:
                 print("El arma:", pista3[2], "pero nunca fue vista en:", asesino[1], "y la portaba el", pista3[0])
             if opcion == pista4[2]:
                 print("El arma:", pista4[2], "fue vista en:", pista4[1], "No se vio a", pista3[0])
         if choosing3 == 4:
             opcion = "LANZA"
             if opcion == asesino[2]:
                 print("El arma:", asesino[2], "fue vista en:", asesino[1], "y la portaba el", asesino[0])
             if opcion == pista1[2]:
                 print("El arma:", pista1[2], "fue vista en:", pista1[1], "No se vio a", asesino[0])
             if opcion == pista2[2]:
                 print("El arma:", pista2[2], "fue vista en:", pista2[1], "y la portaba el", pista2[0])
             if opcion == pista3[2]:
                 print("El arma:", pista3[2], "pero nunca fue vista en:", asesino[1], "y la portaba el", pista3[0])
             if opcion == pista4[2]:
                 print("El arma:", pista4[2], "fue vista en:", pista4[1], "y la portaba el", pista4[0])
         if choosing3 == 5:
             opcion = "NAVAJA"
             if opcion == asesino[2]:
                 print("El arma:", asesino[2], "fue vista en:", asesino[1], "y la portaba el", asesino[0])
             if opcion == pista1[2]:
                 print("El arma:", pista1[2], "fue vista en:", pista1[1], "No se vio a", asesino[0])
             if opcion == pista2[2]:
                 print("El arma:", pista2[2], "fue vista en:", pista2[1], "y la portaba el", pista2[0])
             if opcion == pista3[2]:
                 print("El arma:", pista3[2], "pero nunca fue vista en:", asesino[1], "y la portaba el", pista3[0])
             if opcion == pista4[2]:
                 print("El arma:", pista4[2], "fue vista en:", pista4[1], "No se vio a", asesino[0])
         return eleccion
        

switch = Switcher()
eleccion = " "
res = True

while(res):#Para poder reiniciar el programa en caso de que no se haya encontrado la solución
    

    listpers = itemPers
    listlug = itemLug
    listarma = itemArma
    ##i = 0
    guessing = []
    for i in range(5):
        choice = input("\nElige una opción:\na)Personaje\nb)Lugar\nc)Arma\n");
        eleccion = switch.service_switcher(choice, eleccion)

    adiPers = int(input("\n¿Quién fue el asesino?:\n1.Cazador\n2.Leñador\n3.Carnicero\n4.Cholo\n5.Mayordomo\n"))
    i = adiPers-1
    valorPers = personajes[i]
    guessing.append(valorPers)

    adiLug = int(input("\n¿En dónde fue el asesinato?:\n1.Cocina\n2.Granero\n3.Patio\n4.Recámara\n5.Sala\n"))
    j = adiLug-1
    valorLug = lugares[j]
    guessing.append(valorLug)

    adiArma = int(input("\n¿Con qué arma?:\n1.Daga\n2.Hacha\n3.Machete\n4.Lanza\n5.Navaja\n"))
    k = adiArma-1
    valorArma = arma[k]
    guessing.append(valorArma)

    print(guessing)

    if (set(asesino)==set(guessing)):
        print("\nFelicidades, has acertado a todas las pistas", nombre, "Holmes\n", nomAses, asesino)
        res = False
    else:
        print("\nSuerte para la próxima, estuviste cerca")
        if set(itemPers)==set(valorPers):
            print("Has acertado el asesino")
        if set(itemLug)==set(valorLug):
            print("Has acertado el lugar")
        if set(itemArma)==set(valorArma):
            print("Has acertado el arma")
        rep = int(input("¿Quieres volver a intentar?\n1.Si\t2.No\n"))
        if rep == 1:
            res = True
        else:
            print("Respuesta correcta:\n", nomAses, asesino)
            res = False
        
    
print("\n\nLa partida ha finalizado")


