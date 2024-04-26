#!/usr/bin/env python
# coding: utf-8

# In[ ]:


""" Ejercicios con Diccionarios - Ejercicio Número 1 """ 

""" ENUNCIADO: 1. Frecuencia de pares. Diseña una función dpar(M), en que, dada una lista M de números enteros 
positivos, devuelva un diccionario donde se muestre la frecuencia de aparición de los números 
pares de M."""

"""
    
    --- Aprendizaje para eficiencia: Se puede crear un nuevo item en un diccionario existente con solo definirlo.
    diccionario={"uno":1,"dos":2}
    diccionario["tres"]=3
    print(diccionario)
    
    Output es {"uno":1,"dos":2,"tres":3}
"""
def dpar(M:list):

    pares={}
    
    for item in M:
        if item  % 2 == 0:
            if item not in pares:
                pares[item] = 1
            else:
                pares[item] += 1
    
    return pares




# In[ ]:


M = [12, 19, 19, 18, 18, 16, 18, 13, 19, 18, 12, 18, 11, 20, 14, 14, 20, 20, 20, 16, 13, 15, 19, 14, 12]
print(dpar(M))


# In[ ]:


""" Ejercicios con Diccionarios - Ejercicio Número 2 """ 

""" ENUNCIADO: Temperaturas ciudades. Se tienen las temperaturas de ciudades durante los primeros 4 meses 
del año en una lista de listas, donde cada lista representa la información de una ciudad (nombre y 
luego las temperaturas). Diseña una función TempMaxMin(lst) en que, dada una lista de listas 
como que la que se presenta, devuelva un diccionario con los nombres de las ciudades como claves
y como valores una lista con las temperaturas máxima y mínima."""

"""
    
    --- Aprendizaje para eficiencia: Misma filosofía que ejercicio anterior. Definimos sobre el propio bucle cada nueva parte del diccioanrio.
    
    dictionary[lst[0]]=[maxT,minT] De esta forma nos saldrá "nombre de ciudad":[max,min]
"""

def TempMaxMin(lists:list): 
    dictionary={}
    for lst in lists: #Llamamos a cada lista dentro de la lista
        lst_length= len(lst)
        minT= lst[1]
        maxT= lst[1]
        for item in lst:
            if isinstance(item,float or int):
                if item < minT:
                   minT = item
                if item > maxT:
                   maxT = item
        dictionary[lst[0]]=[maxT,minT]
                
    return dictionary
    
    


# In[ ]:


lst_ciudad = [['Londres', 3.4, 6.3, 10.5, 6.8], \
 ['Oslo', -3.8, -5.0, 5.1, 4.2], ['Berlin', 7.5, 4.1, 12.3, 13.0], \
 ['Málaga', 14.7, 12.3, 19.5, 18.4]]

TempMaxMin(lst_ciudad )


# In[ ]:


""" Ejercicios con Diccionarios (Input de dos diccionarios) - Ejercicio Número 3 """ 

""" Enunciado:Temperaturas nevada. Se dispone de dos diccionarios. En uno de ellos (ej. dPersC) se guardan, 
como claves, nombres de personas y como valores los nombres de las ciudades donde residen; y 
en el otro (ej. dCiudT) se guardan, como claves, nombres de ciudades y como valores las 
respectivas temperaturas de esas ciudades (en ºC), medidas el día de la primera nevada del año.
Diseña una función PersMayTemp(dPersC, dCiudT) en que, dados dos diccionarios como los 
descritos, devuelva una lista con los nombres de las personas que residen en ciudades en las cuales 
la temperatura estuvo por debajo de 0ºC el día de esa primera nevada de este año. La lista 
resultante debe estar ordenada alfabéticamente. En caso de no haber ciudades con temperaturas 
bajo cero, se devolverá la lista vacía. 
Nota: se considera que toda ciudad del diccionario dPersC está en dCiudT """

"""
    
    --- A veces podría ser útil usar la siguiente función para pillar unalista con todos los "keys" del diccionario" list(dCi.keys())
"""

def PersMayTemp(dPe:list, dCi:list)->list:
    ciudades = list()
    #city_names= list(dCi.keys())   Esto está bien saberlo por si queremos sacar los keys algún día. Lo importante es saber tmabién que cunando iteramos con un for sobre un diccionario, solo se itera sobre los keys y no seobre cada valor asociado.
    for item in dCi:
        if dCi[item] < 0:
          ciudades.append(str(item))
    personas = list()
    for item in dPe:
        if dPe[item] in ciudades:
            personas.append(item)
    personas.sort()
    return personas
    
    


# In[ ]:


dCi = {'Manchester': 1.1, 'Madrid': -8.9, 'Gava': 4, \
 'Pobla de Segur': -5.6, 'Lleida': -3.2, 'Elche': 2.1, \
 'Burgos': -6.0, 'Sant Boi': 4.5}
dPe = {'Pepe': 'Manchester', 'Lionel': 'Gava', 'Mike': 'Sant Boi', \
 'Puyol': 'Pobla de Segur', 'Jaime': 'Elche', 'Sergi': 'Lleida',\
 'Ernesto': 'Madrid', 'Carlos': 'Burgos'}
print(PersMayTemp(dPe, dCi))



# In[ ]:


""" Ejercicios con Diccionarios  - Ejercicio Número 4 """ 

"""ENUNCIADO: Se dispone de un diccionario de personas con su presión arterial. En cada elemento 
del diccionario la clave es el nombre de la persona y el valor es una lista con la edad y las presiones 
sistólica (alta) y diastólica (baja). Si consideramos que una persona sufre de hipertensión si la 
presión sistólica es mayor o igual a 140 mmHg o la diastólica es mayor o igual a 90 mmHg, diseña 
una función lst_hiper(dic, edad) en que, dado un diccionario dic como el descrito y una edad, 
devuelva la lista de los nombres de las personas menores de esa edad que sufren hipertensión 
arterial. 
Se valorará devolver la lista de nombres ordenada alfabéticamente. """

""" 
    --- Aprendizaje: Hay que buscar eficiencia en los bucles. Teía pensado hacer otro if en base a una primra limpiezas(edad)
    pero no es necesario por que se puede incluir todo en una sola lógica!-->if dicc[person][0] < edad and (dicc[person][1]>= 140 or dicc[person][2]>= 90):
"""

def lst_hiper(dicc, edad:int)-> list:
    personas = []
    for person in dicc:
        if dicc[person][0] < edad and (dicc[person][1]>= 140 or dicc[person][2]>= 90):
            personas.append(person)
    personas.sort()
    return personas

        


# In[ ]:


dpers = {'Maria': [40, 135, 90],'Nuria': [63, 141, 92], \
'Jose': [47, 110, 59], 'Luis': [49, 146, 94], \
'Oriol': [52, 130, 89], 'Carlos': [65, 125, 89], \
'Pepe': [70, 130, 92] }
print(lst_hiper(dpers, 45),lst_hiper(dpers, 100))


# In[ ]:


""" Ejercicios con Diccionarios  - Ejercicio Número 5 """ 

""" ENUNCIADO: Nivel de potasio en sangre. Se tiene un diccionario con los valores de concentración de potasio 
en sangre ([K+]) de un grupo pacientes medidos antes de entrar a terapia de hemodiálisis. La clave 
es el nombre del paciente y el valor es la [K+] (en mmol/L). Además, se tiene una lista del tipo 
[valor1, valor2, valor3, valor4] con los distintos valores que clasifican la condición clínica en que 
están los pacientes, de acuerdo a las concentraciones de potasio en sangre ([K+]). Estos valores 
dependen del tipo de población (niños, adultos, etc.). 
La condición clínica del paciente sigue el siguiente criterio de clasificación: 
- Si el valor de [K+] es menor que valor1 indica 'hipokalemia crítica', 
- si es mayor o igual al valor1 y menor que el valor2 sería 'hipokalemia leve',
- si está entre valor2 y valor3 (ambos inclusive) indica 'normal', 
- si es mayor que valor3 y menor o igual que valor4 es 'hiperkalemia moderada'
- y valores mayores que valor4 sería 'hiperkalemia severa'. 
Ejemplo de una lista con elementos [valor1, valor2, valor3, valor4] para un adulto de mediana edad: 
[2.0, 3.5, 5.2, 7.0]
Diseña una función nivelKsang(dK, lst) en que, dado un diccionario dK que tiene como clave el 
nombre de un paciente y como valor su nivel de [K+] en sangre, y una lista lst con 4 valores de 
clasificación, como los descritos, devuelva un diccionario que tenga como claves los nombres de los 
pacientes y como valores su clasificación, de acuerdo a los niveles de [K+] en sangre."""

"""

Aprendizaje: Una función chula de traducción que luego se aplica con un loop. Parecido a otros lenguajes.

"""

def nivelKsang(dk,lst:list):
    
    def translator(value,lst):
            if value < lst[0]:
                condicion='hipokalemia crítica'
            elif value >= lst[0] and value < lst[1]:
                condicion='hipokalemia leve'
            elif value >= lst[1] and value <= lst[2]:
                condicion='normal'
            elif value > lst[2] and value <= lst[3]:
                condicion='hiperkalemia moderada'
            elif value > lst[3]:
                condicion='hiperkalemia severa'
            return condicion
    
    
    for item in dk:
        dk[item]= translator(dk[item],lst)
    
    return dk
        


# In[ ]:


dK1 = {'Luis': 2.2, 'Carlos': 7.0, 'Laia': 4.0, 'Mikel': 5.5, \
'Jordi': 5.2, 'Anna': 3.6, 'Joe': 7.2}
ls1 = [2.0, 3.5, 5.2, 7.0]
print(nivelKsang(dK1, ls1))


# In[ ]:


""" Ejercicios con DataFrames  - Ejercicio Número 6 """ 

"""
ENUNCIADO:Temperatura ciudades en DataFrame. A partir de lst_ciudad de las temperaturas de las 
ciudades de los primeros 4 meses del año del ejercicio 2:


a) Diseña un código para crear un objeto DataFrame que contenga en sus columnas: 'Ciudad', 
'Enero', 'Febrero', 'Marzo', 'Abril' y los datos sean los valores de las listas de ciudades de 
lst_ciudad. Agregar como nombre del DataFrame: 'Temperatura ciudades'.

b) Escribe un código para agregar la temperatura mínima, máxima, media y desviación 
estándar de los 4 primeros meses del año al DataFrame anterior. Resultado de la forma:
"""
"""
Aprendizaje
A partir de una lista de listas, usando la función pd.DataFrame(lista=[content],columns=[content]), podemos convertir la lista de listas en un dataframe (un diccionario de columnas o tabla)

Podemos añadir items a un dataframe solo con darle un nuevo nombre y operar sobre el dataframe llamando sus columnas
 
Ejemplo: Temperatura_ciudades['Min'] = Temperatura_ciudades[columns_names].min(axis=1) -> Al poner (axis=1) al final del codigo, especificamos que queremos calcularlo y hacer la operación por filas y no por columnas

"""
lst_ciudad = [['Londres', 3.4, 6.3, 10.5, 6.8], \
 ['Oslo', -3.8, -5.0, 5.1, 4.2], ['Berlin', 7.5, 4.1, 12.3, 13.0], \
 ['Málaga', 14.7, 12.3, 19.5, 18.4]]

import pandas as pd

DataFrame= pd.DataFrame(lst_ciudad, columns=['Ciudad', 'Enero', 'Febrero', 'Marzo', 'Abril'])
DataFrame.name = "Temperatura ciudades"


columns_names = DataFrame.columns[1:DataFrame.shape[1]]


Temperatura_ciudades['Min'] = DataFrame[columns_names].min(axis=1)
Temperatura_ciudades['Max'] = DataFrame[columns_names].max(axis=1)
Temperatura_ciudades['Media'] = DataFrame[columns_names].mean(axis=1)
Temperatura_ciudades['StdDev'] = DataFrame[columns_names].std(axis=1)




# In[ ]:


""" Resultados ejercicio 6"""
print("A. Dataframe de ciudades")
print("")
print(DataFrame)
print("")
print("")
print("")
print("B. Estadtísticos de temperatura en ciudades")
print("")
print(Temperatura_ciudades)
print("")
print("")


# In[ ]:


""" Ejercicios con DataFrames  - Ejercicio Número 7 """ 

"""
Base de datos cardiaca. La base de datos de enfermedades cardiacas UCI heart.csv, que se 
encuentra disponible en el aula y en el enlace https://www.kaggle.com/ronitf/heart-disease-uci , 
contiene 14 atributos (columnas):
1. age: edad
2. sex: sexo (1: hombre, 0: mujer)
3. cp: tipo de dolor en el pecho (4 valores)
4. trestbps: presión arterial sistólica en reposo
5. chol: colesterol sérico en mg/dl
6. fbs: azúcar en sangre (en ayunas) > 120 mg/dl
7. restecg: Resultados electrocardiográficos en reposo (valores 0,1,2)
8. thalach: frecuencia cardíaca máxima alcanzada
9. exang: angina inducida por ejercicio (1: sí, 0: no)
10. oldpeak: depresión del segmento ST inducida por el ejercicio relativo al descanso
11. slope: pendiente del segmento ST de ejercicio máximo
12. ca: número de vasos principales (0-3) coloreados por flourosopía
13. thal: 3 = normal; 6 = defecto fijo; 7 = defecto reversible
Y el atributo 14, target se refiere a la presencia (1) o no (0) de enfermedad cardiaca.
En este ejercicio se pide que se lea o cargue la base de datos desde heart.csv a un objeto DataFrame
(por ejemplo, dfCardio) y se presenten los siguientes resultados:


a) Mostrar las primeras 10 instancias (filas) del DataFrame. 
b) Calcular el número (conteo) de hombres y mujeres.
c) Calcular el número (conteo) de casos de angina de pecho inducida (atributo: exang)
d) Hallar el DataFrame con la estadística descriptiva de la frecuencia cardiaca (thalach)
e) Hallar un DataFrame que incluya la estadística descriptiva de la presión arterial sistólica en 
reposo (trestbps) y el colesterol (chol). (ambos en el mismo DataFrame)

"""
"""
Aprendizaje:

"""
import pandas as pd
heart=pd.read_csv("heart.csv")

#Primeras diez filas(instancias)

first10=heart.head(10)

#Conteo de hombres y mujeres
hombres = 0
mujeres =0
for item in heart['sex']:
    if item == 1:
        hombres+=1
    elif item == 0:
        mujeres+=1
hombres_mujeres={"Hombres":hombres,"Mujeres":mujeres,"Total":hombres+mujeres}

#Conteo de anginas
anginas=0
for item in heart['exang']: 
    if item == 1:
        anginas +=1

        
#Dataframe de estadística descriptiva  (Usamos describe() para hacer las cosas fácil)

def estadistica_descriptiva(columname:str): 
    output = (heart[columname].describe())
    output['moda']= heart[columname].mode().iloc[0] ##La moda no aporta mucho, pero me parece un buen ejercicio añadirlo al set originado.
    return output


frecuencia_cardiaca = estadistica_descriptiva('thalach')
frecuencia_cardiaca = pd.DataFrame({'Estadísticos': frecuencia_cardiaca.index, 'Frecuencia cardíaca': frecuencia_cardiaca.values})

#Dataframe de estadística descriptiva de presiónarteialycolesterol (Usamos la función de antes)

presion = estadistica_descriptiva('trestbps')
colesterol = estadistica_descriptiva('chol')
presionycolesterol = pd.DataFrame({'Estadísticos': presion.index, 'Presión arterial sistólica': presion.values,'Colesterol': colesterol.values})


# In[ ]:


""" Resultados ejercicio 7"""
print("A. Las primeras 10 filas")
print("")
print(first10)
print("")
print("")
print("")
print("B. Conteo de hombres y de mujeres en diccionario")
print("")
print(hombres_mujeres)
print("")
print("")
print("")
print("C. Conteo de casos de angina de pecho inducida")
print("")
print(f"Número de casos: {anginas}")
print("")
print("")
print("")
print("D. DataFrame de Frecuencia cardíaca")
print("")
print(frecuencia_cardiaca)
print("")
print("")
print("")
print("E. DataFrame de Presión arterial y colesterol")
print("")
print(presionycolesterol)
print("")
print("")
print("")


# In[ ]:


""" Ejercicios con DataFrames  - Ejercicio Número 8 """ 

"""
ENUNCIADO:
Base de datos presión arterial en DataFame. Dado un diccionario sobre hipertensión como el del 
ejemplo en el docstring del ejercicio 4, diseña una función que entre (sea el input) un diccionario donde la clave es
el nombre de la persona y el valor es una lista con la edad y las presiones sistólica y diastólica (en 
unidades: mmHg), devuelva un dataFrame que incluya como columnas: 'Nombre', 'Edad', 'Sistólica', 
'Diastólica' y una última columna calculada, etiquetada 'Diagnóstico', con datos categóricos con 
valores 'baja', 'normal', 'alta'. 

La presión arterial 'baja' la definimos así: si la presión sistólica es menor 
que 90 mmHg o la diastólica menor que 60 mmg. La presión 'alta' sería si la sistólica es mayor o igual 
a 140 mmHg o la diastólica es mayor o igual a 90 mmHg. En otras condiciones sería 'normal'. Ejemplo 
de diccionario de entrada y resultado.

Nota. Se considerará que no habrá casos donde la diferencia entre la presión sistólica y diastólica (presión de 
pulso) supere los 60 mmHg, es decir, no habrá casos donde simultáneamente se encuentre un paciente con la 
tensión diastólica menor que la 'baja' y la sistólica mayor que la 'alta'
"""


"""

APRENDIZAJE:  Así es como se itera en columnas con pandas y se añade un resultado a una columna nueva (O una antigua ya dependiendo de cual sea el objetivo)

    for item, row in output.iterrows():
        if row["Sistólica"]<90 or row["Diatólica"]<60:
           output.at[item,"Diagnóstico"]="baja"
        if row["Sistólica"]>=140 or row["Diatólica"]>=90:
           output.at[item,"Diagnóstico"]="alta"
        else:
           output.at[item,"Diagnóstico"]="normal"
                   

"""
import pandas as pd
dpers = {'Maria': [40, 135, 90],'Nuria': [63, 141, 92], \
 'Jose': [47, 110, 59], 'Luis': [49, 146, 94], \
 'Oriol': [52, 130, 89], 'Carlos': [65, 125, 89], \
 'Pepe': [70, 130, 92],'Benitez': [20, 40, 20]}


def evalua_tension(dictionary):
    edad=[]
    sistolica=[]
    diastolica=[]
    for item in dictionary:
        contador=0
        for value in dictionary[item]:
                contador+=1
                if contador == 1:
                    edad.append(value)
                if contador == 2:
                    sistolica.append(value)
                if contador == 3:
                    diastolica.append(value)         


    output=pd.DataFrame({"Nombre":dictionary.keys(),"Edad":edad,"Sistólica":sistolica,"Diatólica":diastolica})
    
    for item, row in output.iterrows():
        if (row["Sistólica"]<90) or (row["Diatólica"]<60):
           output.at[item,"Diagnóstico"]="baja"
        elif (row["Sistólica"]>=140) or (row["Diatólica"]>=90):
           output.at[item,"Diagnóstico"]="alta"
        else:
         output.at[item,"Diagnóstico"]="normal"

    ##Suponemos que no se puede producir alta y baja al mismo tiempo según el enunciado
    return output
    


# In[ ]:


evalua_tension(dpers)

