import random
from manualPreguntas import preguntas

pregCant,cont,numPreg=0,0,1
newDict={}
indexlista3=[]
preguntasFalladas1=[]
numlen=len(preguntas)

print()
print(".........:BIENVENIDO AL TEST DE PRUEBA TEORICA DE MANEJO:.........")
print()

numRandomValues = int(input(f"INGRESE LA CANTIDAD DE PREGUNTAS QUE DESEA RESPONDER (máximo {numlen}): "))

if numRandomValues > numlen:

    print(f'La cantidad máxima es: {numlen} y usted ingreso: {numRandomValues}')
    numRandomValues = int(input(f"INGRESE LA CANTIDAD DE PREGUNTAS QUE DESEA RESPONDER (máximo {numlen}): "))

print()

def randomDict(preguntas,newDict,numlen,numRandomValues):
    '''"preguntas" será el diccionario del que deseo sacar la cantidad de valores aleatorios,
       "numRandomValues" es la cantidad de valores aleatorios que se sacarán del diccionario,
    '''

    indexLista=random.sample(range(numlen), numRandomValues)

    for j in indexLista:
        index=j
        newDict.update({list(preguntas.keys())[index]:list(preguntas.values())[index]})

def showDict(pregCant,numPreg,cont,numRandomValues,preguntasFalladas):

    while pregCant!=numRandomValues:

        for i,j in newDict.items():
            print(f"PREGUNTA N°{numPreg}")
            print()
            print(i.upper(),f"\n\n{j[1]}\n{j[2]}\n{j[3]}\n{j[4]}")
            print()

            rta=input("Ingrese la respuesta correcta con la letra correspondiente: ")
            print()

            if j[0].upper() == rta.upper():
                cont+=1

            if j[0].upper() != rta.upper():
                preguntasFalladas+=[i]

            numPreg+=1
            pregCant+=1

            if pregCant==numRandomValues:
                break;

    print(f"USTED RESPONDIO BIEN {cont} DE {numRandomValues} PREGUNTAS")

randomDict(preguntas,newDict,numlen,numRandomValues)
showDict(pregCant,numPreg,cont,numRandomValues,preguntasFalladas1)

print()

if len(preguntasFalladas1)>=1:
    rtasFallidas=input("Ingrese 'S' si quiere ver las preguntas erroneas, sino presione cualquier tecla: ")
    print()

    if rtasFallidas.upper()=="S":
        print("Las preguntas que usted respondio mal:")

        for i in preguntasFalladas1:
            print("-",i.upper())

    else:
        print("programa finalizado")