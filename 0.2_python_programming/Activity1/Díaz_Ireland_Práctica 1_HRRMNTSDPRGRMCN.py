#!/usr/bin/env python
# coding: utf-8

# In[ ]:


""" Ejercicios con strings - Ejercicio Número 1 """ 

""" ENUNCIADO: Identificador válido. Para que los identificadores o nombres de las variables o funciones sean 
válidos deben comenzar e incluir letras a..z. (minúscula o mayúscula) o el guión bajo (_). 
Pueden incluir también números (0..9) pero que no sean el primer carácter del identificador.
Diseña una función FirstChar(s) que, dado un string s (no vacío), nos devuelva True o False 
si el string es válido o no para identificar o dar nombre a una variable o función1 """

    
"""
    
    --- Aprendizaje: 
        - "item".isdigit() chequea si el "item" es tipo número
        - "item".isalpha() chequea si el "item" es tipo text
        - "item".isalnum() chequea si el "item" es tipo text o tipo número directamente. Excluye espacios!
        - "item".isspace() chequea si el "item" es tipo espacio (todos los items)
        
        - Loops (Importante) -> Todas las funciones arriba chequean para todo el string. 
              Para solucionar esto usamos "for" "in" de python
                for: Define el caracter
                in: entra al detalle dentro de nuestro item 
                   (En este caso el in ataca un string, por lo que pasa a revisar cada carácter de un string)
                   (También se puede usar en una lista. Por eso otra opción es converir cada carácter en un item de una lista y comprobarlo)
                   (También funciona para tablas en pandas, etc...)
"""

        


def FirstChar(string: str) -> bool:
    
    characters = list(string)

    def character_is_number_or_alph() -> bool:    
        for char in characters: 
            if char.isdigit() or char.isalpha():
                return True
        else:
            return False      

    def is_first_character_number() -> bool:
        if string[0].isdigit() :
            return True
        else:
            return False
        
    def identify__() -> bool:
        for char in characters: 
            if char == "_":
                return True
        else:
            return False
        
    def character_is_special() -> bool:
        for char in characters: 
            if (not char.isalnum() and not char.isspace() and char != "_"):
                return True
        else:
            return False 
    """
    def second_or_subsequent_character_is_number2() -> bool:
        if string[1:string_length].isdigit():
            return True
        else:
            return False
    """

    if (character_is_number_or_alph() is True or identify__ () is True) and (is_first_character_number() is False) and (character_is_special() is False):  
        return True
    else:
        return False
    

      

  


# In[ ]:


print(FirstChar('paciente001'),FirstChar('P001'),FirstChar('1Pac'),FirstChar('_001'),FirstChar(':p001'))


# In[ ]:


""" Ejercicios con strings - Ejercicio Número 2 """ 

""" ENUNCIADO:  Porcentaje de vocales. Escribe una función porcentVocal(s) en que dado un string s, la 
función devuelva el porcentaje de vocales que contiene el string. Deben considerarse vocales 
minúsculas y mayúsculas. Devolver el resultado con un decimal de precisión.
Consideraremos que las vocales están sin tilde o acento gráfico. Se valorará prever el caso que 
se envíe como argumento un string vacío. """


"""

  --- Aprendizaje: 
     - Si tenemos "x" y queremos hacer x = x + 1. Podemos definir la nueva variable así " x += 1 "

     - Loops (Importante) -> Así se hace un doble loop que chequea todos los sub-items de un item con todos los sub-items de otro item
          for char in string:
           for vocal in vocals:
            if char == vocal:
             i = i + 1
          return i

"""


def porcentVocal(string:str) -> float:

  vocals = {"A","a","E","e","I","i","O","o","U","u"}
  
  def count_vocals () -> int:
    i = 0
    for char in string:
      for vocal in vocals:
        if char == vocal:
          i = i + 1
    return i
   
  string_length = len(string)
  
  percentage = (count_vocals ()/string_length) *100



  return round(percentage,1)





# In[ ]:


print(porcentVocal('Hola'),porcentVocal('Acacia'),porcentVocal('Brrrrrrr'),porcentVocal('aAe'))


# In[ ]:


""" Ejercicios con strings - Ejercicio Número 3 """ 

""" ENUNCIADO:Nuevo string. Diseña una función nuevo_string (s, n) que, dado un string s y un entero 
n ≥ 0, devuelva el string resultante de repetir cada vocal de s exactamente n veces en el lugar 
donde se encuentra situada en s.
"""

"""

  --- Aprendizaje: 

     - Loops (Importante) -> Cuando queremos iterar una sola vez para chequear con una lista "if" "in"
        for char in s: ##Definimos todos los carácteres del string
                if char in vocals: ##Comprobamos todas las vocales con "in" vocals
                  nuevo_string = nuevo_string + (char*n)
                else: 
                  nuevo_string = nuevo_string + char
                  
        # En consecuencia, si en vez de poner (if char in vocals) pusieramos (if char == vocals) no nos valdría ya que solo comprueba el primer valor de vocals ("A")
        
        # Conclusión --> La manera más fácil de revisar una lista con otra es usar for "" in ""(Definimos los items) y luego if "" in "" (Chequeamos los items en la lista)
        
        # Importante interiorizar --> Muchas veces (Inclsuo con un string) al mejor manera de empezar un loop es con un string empty que se vaya rellenando
                  
        

"""

def nuevo_string(s:str, n:int) -> str:
    
    vocals = {"A","a","E","e","I","i","O","o","U","u"}
    
    def add_vocals () -> int:
        nuevo_string = "" ##Empty String para ir acumulando los valores
        for char in s:
                if char in vocals:
                  nuevo_string = nuevo_string + (char*n)
                else: 
                  nuevo_string = nuevo_string + char
        return nuevo_string

    return add_vocals ()
    






# In[ ]:


print(nuevo_string('Charleston', 2),nuevo_string('RDT11', 1),nuevo_string('H2O', 3))


# In[ ]:


""" Ejercicios con strings - Ejercicio Número 4 """ 

""" ENUNCIADO: Notas al pie de página. Diseña una función notas_al_pie(s) que, dado un string s formado 
sólo por letras, signos de puntuación y asteriscos que indican una llamada a una nota al pie 
de página, devuelva un string donde cada asterisco es sustituido por un número entre 
paréntesis que indica el número de nota. El primer * se substituye por (1), el segundo por (2), 
etc. Ejemplos: """

"""

  --- Aprendizaje: En cuanto a los loops. MUY IMPORTANTE poner return al final. Si no no nos da ningún output
  
   CONCEPTO MUY IMPORTANTE CON LOS LOOPS
   
   Primer ejemplo: Aquí el return está al mismo nivel que el for. python lo va a leer como que hay que completar todas las partes del Loop
   
       def is_char_good()-> bool:

     contador=0
        stringchars=list(s)
        for char in stringchars:
            if  (char.isalpha() or char in validchar) and not char.isdigit():
                contador= contador
            else: 
                contador = contador + 1
        return True if contador == 0 else False

   Segundo ejemplo: Aquí el return está al mismo nivel que el if. En este caso solo va a chequear el primer objeto de nuestro string.
   
       def is_char_good()-> bool:
        contador=0
        stringchars=list(s)
        for char in stringchars:
            if  (char.isalpha() or char in validchar) and not char.isdigit():
                contador= contador
            else: 
                contador = contador + 1
            return True if contador == 0 else False
   

"""

def notas_al_pie(s:str) -> str:
    validchar = list('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    
    def is_char_good()-> bool:
        contador=0
        stringchars=list(s)
        for char in stringchars:
            if  (char.isalpha() or char in validchar or char.isspace()):
                contador= contador
            else: 
                contador = contador + 1
        return True if contador == 0 else False
        
            
    def notas() -> str:
        notas_output=""
        contador= 0
        for char in s:
            if char == "*":
                contador = contador + 1
                notas_output = notas_output + "(" + str(contador) + ")"
            else: notas_output = notas_output + char
        return notas_output
            
          
                 
                 

    def output()-> str:
        if(is_char_good() is False):
            return "Message: not valid String as an input" 
        else: return notas()
        
        

    return output()




   




# In[ ]:


print(notas_al_pie('Esta es la primera nota*; y esta la segunda*.'),notas_al_pie('Esta frase no tiene notas. Esta otra tampoco.'),notas_al_pie('*,*. *.'),notas_al_pie('*'),notas_al_pie(''))


# In[ ]:


""" Ejercicios con strings - Ejercicio Número 5 """ 

""" ENUNCIADO: Dado un string s que contiene los nombres y apellidos de una persona, diseña 
la función codigo(s) que devuelva el string ini + str(count), donde ini contiene las iniciales 
de la persona (las letras mayúsculas de s) y count es el número total de letras de sus nombres 
y apellidos (es decir, las letras de s sin contar caracteres blancos o espacios). """

"""
  --- Aprendizaje: Resolución rápida gracias a la práctica con los ejercicios anteriores.
  
   

"""
            

def codigo(s:str) -> str:
    contador = 0
    length_s = len(s)
    if length_s > 0:
        output_codigo= s[0]##Iniciamos con lo que sabemos que es la primera variable
        for char in s:
            contador= contador + 1
            if char.isspace():
                output_codigo = output_codigo + s[contador]
    else: output_codigo= ''
    
    if length_s == 0:
        length = '' 
    else: length = str(length_s)


    return str(output_codigo) +  str(length)



# In[ ]:


print(codigo('Mireia Belmonte García'),codigo('Bruce Frederick Joseph Springsteen'),codigo(''),codigo('Gerard Piqué Bernabéu'),codigo('Sergio Ramos García'))


# In[ ]:


""" Ejercicios con strings - Ejercicio Número 6 """ 

""" ENUNCIADO: Una fórmula química es una representación convencional de los 
elementos que forman un compuesto. Por ejemplo, el 1-2-butadiol sería C2H5O, que se 
representa con el string 'C2H5O'. También pueden aparecer elementos químicos de dos 
caracteres como el calcio Ca en CaCO3 ( 'CaCO3') o el hierro Fe en Fe3O4 ( 'Fe3O4'). En estos 
casos el segundo carácter del símbolo siempre es una minúscula. Diseña la función 
contar_hidrogenos(s) que, dado un string s con un compuesto como los descritos antes, 
devuelve el número de átomos de hidrógeno que contiene. Para simplificar el problema, 
limitaremos el número que puede seguir el símbolo de un elemento a un valor entre 2 y 9. """

"""
  --- Aprendizaje: OJO en los loops con usar el item que estamos iterando para referirnos a una posición de dentás o de delante
  
  MEJOR utilizar la lista original. Es decir en esta resolución: 
                                              s[contador+1] nos va a dar el item de delante
                                              char[contador+1] se hace un lío por que char es un dinamismo que hemos puesto nosotros.
                                        Mejor referirnos a la lista original con el contador del loop.
                            
 

"""



#Nota: Esta función supone que el input va a ser corecto (Por ejemplo, para el Helio, será He y no HE)
def contar_hidrogenos(s:str)-> float:
    contador_H = 0
    contador = -1
    ##valid_numbers = list("23456789")## Not used in the end
    for char in s:
        contador = contador + 1
        if contador+1 == len(s):
            contador=contador-1         
        if char == "H" and s[contador+1].isupper():
            contador_H = contador_H + 1
        elif char == "H" and s[contador+1].isdigit():
            contador_H = contador_H + int(s[contador+1])
        
    return contador_H
            







# In[ ]:


print(contar_hidrogenos('HIO'),contar_hidrogenos('H2O'),contar_hidrogenos('C2H5O'),contar_hidrogenos('Fe3O4'),contar_hidrogenos('C2OH'))


# In[ ]:


""" Ejercicios con listas - Ejercicio Número 7 """

"""
ENUNCIADO: Diseña la función mediaTempRang(lst) en que, dada una lista lst de medidas de 
temperatura en ºC de un experimento, calcule y devuelva el valor medio de aquellas 
temperaturas de la lista que estén en el rango de 15 a 45 ºC, inclusive [15, 45]. Devolver el 
resultado redondeado a 2 cifras decimales. También considerar el caso en que ninguna 
medida de temperatura de la lista esté en el rango dado. En este caso la función devuelve el 
valor -1."""

"""
  --- Aprendizaje: 
  
  ### para hacer un appending de items en un loop a una lista
  siempre nos referimos a la misma lista
  Hay que evitar -> new_list = new_list.append(lst[contador]) por que dara errores
  Usar new_list.append(lst[contador]) a secas.
 

"""

def mediaTempRang(lst:list)-> int:
    new_list=[] 
    contador=-1
    for item in lst:
        contador= contador + 1
        if item >= 15 and item <= 45:
            new_list.append(lst[contador]) 
    ### Careful! As we are appending items each time to a list which is always the same list. if we do -> new_list = new_list.append(lst[contador]) it will give errors 
    
    length_list= len(new_list)
    if length_list == 0:
        average=-1
    else: average = sum(new_list)/length_list
    
    if average > 0: 
        return round(average,2)
    else:
        return -1
    






# In[ ]:


lst1 = [34.5, 12.9, 15, 43, 51.4, 23.4]
print(mediaTempRang(lst1),mediaTempRang([45.5, 12.9, 15, 32.5, 51.4, 21.2]),mediaTempRang([14.5, 12.6, 47.8]),mediaTempRang([15, 16, 14, 50, 17]))



# In[ ]:


""" Ejercicios con listas - Ejercicio Número 8 """ 

"""
ENUNCIADO: . El umbral de nivel de presión del sonido (sound pressure level, SPL) del oído humano es 
aproximadamente de 20 P a frecuencias medias de la voz. Este valor se considera el nivel de 
presión de sonido (SPL) de referencia, 0 dB (20log10(20/20)). La función SPL_dB(P) recibe una 
presión acústica en P, y devuelve su equivalente en dB. 
Diseñar la función detect2ndNdB(lst, N), en que dada una lista lst de valores de nivel de 
presión de sonido (SPL) en P, y un valor N (dB), busque y devuelva el valor de la segunda 
presión SPL que sea al menos de N dB. Por ejemplo, N = 30 dB es el nivel de un susurro en el 
oído, N = 50 dB es el nivel de una conversación normal, N = 80 dB es el nivel de ruido en una 
calle con tráfico. En caso de no encontrar una segunda presión SPL se ha de devolver -1.
Notas: (i) Se debe usar la función SPL_dB(P) que convierte en dB la presión de entrada en P.
(ii) Se debe buscar la 2ª presión de acuerdo a la ubicación en la lista original del argumento.
Por ejemplo, en:
>>> detect2ndNdB([90, 590, 750, 632, 650, 660, 2000, 789, 545], 30)
650
Las presiones marcadas en rojo superan los 30 dB, pero la segunda de la lista original, 650, es 
la que se tiene que devolver.  """

"""
  --- Aprendizaje: En cualquier parte del código. Cada vez que se usa : se abre un nuevo bloque
      
      Por tanto, podemos usar un if else sin tener que definir la variable antes (Podemos definirlo dentro)
  
"""



from math import log10

def detect2ndNdB(lst:list, N:float)-> list:
    def SPL_dB(P):
    # Esta función Calcula Sound Pressure Level en dB: 20log(x/20) cuando x en microPascales
    # Los decibelios (Db) es una medida logaritima del sonido (Por eso lo transformamos de microPascales a una escala reconocible por el ser humano que varía de manera no lineal)
    # Nota interesante: La anatomía del oido detecta desde 20 Hz hasta 20 kHz. Un sonido muy potente (Muchos microPascales o muchos Db, si tiene una frecuencia por debajo o por encima, no hará reaccionar las células del oído, y no seremos capaces de escucharlo)
        return 20*log10(P/20)
    
    list_in_dB=[]
    for item in lst:
        list_in_dB.append(SPL_dB(item))
    
    
    ##selected_dB=[] --> No necesario al final
    position_original_list = []
    contador=-1
    for item in list_in_dB:
        contador = contador+1
        if item >= N:           
           ##selected_dB.append(item) --> No es necesario seleccionar los que cumplen. Solo saber la posición
           position_original_list.append(contador)
     
    nvalid_items = len(position_original_list)      
        
        
    #Important Note about indentations: In python a new piece of code is written when a : is created. Therefore, we do not to necessary define the new variable before creating the code.
    if nvalid_items > 1:
        output = lst[position_original_list[1]]#OJO. Devolvemos la posición 1 por que se empieza a contar desde el 0 (posición 1 igual a segundo item en la lista)
    else: output = -1       
    
    
    return output
        





 


# In[ ]:


print( detect2ndNdB([90,590,750,632, 650, 900, 2000, 789, 545], 30), detect2ndNdB([90,590,750,632, 650, 900, 2000, 789, 545], 33),detect2ndNdB([90,590,750,632, 630, 600, 200, 589, 545], 30),detect2ndNdB([9e3,1e4,1.1e5,2.2e5, 1.3e6, 2.5e6, 3.2e6], 83),detect2ndNdB([2000, 2450.5, 2500 , 456.7, 1567.8], 42))


# In[ ]:


""" Ejercicios con listas - Ejercicio Número 9 """ 

"""
ENUNCIADO: Primos pitagóricos. Diseña la función primoPitagoric2(lst) en que, dada una lista de 
números enteros positivos no repetidos, devuelva una lista con los 2 primeros números 
primos pitagóricos. Si no hubiera al menos 2 primos pitagóricos la función devuelve -1
Un número primo es pitagórico si se puede escribir como la suma de dos cuadrados. Por 
ejemplo 5 = 22 + 11 o 13 = 22 + 32
. Fermat demostró que un primo pitagórico p es igual a 4k + 
1, para algún valor de k entero positivo. Esta condición se puede expresar como: un número 
primo p es pitagórico si p modulo 4 es igual a 1, es decir si el residuo de dividir p entre 4 es 1"""

def primoPitagoric2(lst:list)->list:
    def es_primo(n):
        if n <= 1: return False
        for d in range(2, n//2+1):  ##Interesante. Esta función itera desde valor 2 a (n//2) + 1, es decir, como maximo se divide entre la mitad del número n + 1, ya que no tiene sentido intentar dividir entre más de la mitad (Nos vamos a numeros menores que 2 pero mayores que 1)
            if n % d == 0: # % nos devuelve el resto. Con que un resto sea 0 ya nos vale para que el númro se categorize como no primo
               return False
        return True
    #Usamos la demostración con reducción de los absurdo de Fermat p = 4k +1 siendo p un número pitagórico y k un númer coincidente
    solo_primos = []
        
    for item in lst:
        if es_primo(item) is True:
           solo_primos.append(item)        
    
    dos_primeros_pitagoricos=[]
    for item in solo_primos:
        if item % 4 == 1: ## Si hemos clasificado que el número sea primo antes, clasificando por item%4 == 1 ya tenemos todos los primos que cumplen pitagóricos (por ejemplo 7 no sería pitagórico por que no cumple con item%4 == 1)
           dos_primeros_pitagoricos.append(item)
           if len(dos_primeros_pitagoricos)>1: ##while len(dos_primeros_pitagoricos)<2:
              break      
        
    if len(dos_primeros_pitagoricos)<2:
       output =  -1 
    else: 
       output = dos_primeros_pitagoricos
                 
        

    return output 




# In[ ]:


lista = [81, 85, 89, 93, 97, 101, 105, 109, 113, 117, 121]
print(primoPitagoric2([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),primoPitagoric2([5, 9, 13, 17, 21, 25, 29, 33, 37, 41]),primoPitagoric2([41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81]),primoPitagoric2([3, 4, 5, 6, 7, 8, 9, 10]),primoPitagoric2(lista))


# In[ ]:


""" Ejercicios con listas de listas - Ejercicio Número 10 """ 

"""
ENUNCIADO:Contar positivos. Dada una lista de listas que representa una matriz cuadrada m, diseña una 
función contar_pos(m), que cuente los números positivos que tiene. """


"""
  --- Aprendizaje: Fácil. Como curiosidad, para iterar dentro de una lista de listas, solo definir la iteración dos veces. Será igual parar tierar en palabras en una lista seguro.
  
"""

def contar_pos(m:list)->int:
    contador=0
    for lst in m:
        for item in lst:
            if item>0:
                contador+=1
    return contador



                
            
    





# In[ ]:


print(contar_pos([[1, -2, 3],[-4,5,6],[7,8,-9]]))


# In[ ]:


""" Ejercicios con listas de listas- Ejercicio Número 11 """ 

"""
ENUNCIADO: Mayor densidad. Se dispone del nombre, masa y volumen de un planeta almacenado en una 
lista: [nombre, masa, volumen]. Además, se tiene una lista de planetas como una lista de listas 
de la forma: [[nombre1, masa1, volumen1], [nombre2, masa2, volumen2], ...]. 
Diseña la función mas_denso(Lst), en que dada una lista de planetas Lst, nos devuelva el 
nombre del planeta más denso de esa lista. Si hubiera más de uno con la misma densidad, se 
devuelve el primero que encuentre en la lista original.  """

        
"""
  --- Aprendizaje: Ejercicio muy chulo.
  
  Primero creamos una lista en el que se acumulan las densidades multiplicando la masa por el volumen.
  seguidamente, tomamos el primer valor de la lista rellenandolo en biggest_density (Por que siempre va a ser más que 0) y devolvemos el planeta que supere al anterior, hasta el final de la iteraciónd de la lista.
  
  IMPORTANTE: Para generar la lista bien iterando y operanod al mismo tiempo
  
  MUY IMPORTANTE --> density_list_detail = ([lt[0],(lt[1] * lt[2])]) definir cada lista entre []
  luego ya se puede hacer el second_list.append(density_list_detail) generano una lista de listas
  
  
"""

def mas_denso(lst:list)-> str:
    density_list_detail = []
    density_list_general = []
    for lt in lst:
        density_list_detail = ([lt[0],(lt[1] * lt[2])])
        density_list_general.append(density_list_detail)
            
    
    biggest_density = 0 
    for i in range(0,len(density_list_general)-1):
        if int(density_list_general[i][1]) > int(biggest_density):
           biggest_density_planet = density_list_general[i][0]
           biggest_density = density_list_general[i][1]
    
    return biggest_density_planet





# In[ ]:


mas_denso([['Marte', 1, 2], ['Tierra', 2, 3], ['Venus', 1, 3]])


# In[ ]:


""" Ejercicios con listas de listas - Ejercicio Número 12 """ 

"""
ENUNCIADO:  Fútbol. Se dispone en una lista (equipo) de listas (jugadores) con los registros de los 
jugadores. En cada registro se guarda: su número de dorsal, nombre, si es comunitario o no 
(booleano, comunitario: True), edad y la distancia recorrida en kilómetros en los partidos 
jugados en el último mes. 
No todos los jugadores han jugado todos los partidos del mes, por lo que aparecerá solo la 
distancia recorrida de los partidos jugados.
Diseñar una función jugComKm(equipo, x) en que, dada una lista de un equipo de futbol y 
un número x de kilómetros recorridos, nos devuelva la lista de nombres de los jugadores 
comunitarios que han recorrido de media (promedio) más de x km en los partidos jugados.
De no encontrarse jugadores con este recorrido, se devolverá la lista vacía.
Notas: pudiera haber algún jugador sin partidos jugados y en este caso el promedio lo 
consideramos 0.
Se valorará devolver la lista de nombres ordenada alfabéticamente."""



"""
  --- Aprendizaje: Un slash \ sirve para continuar en la linea de abajo con el mismo bloque
  
"""

lst_equipo = [[3, 'Pique', True, 33, 10.2, 9.0], \
 [4, 'Ramos', True, 34, 11.0, 11.1, 9.8, 8.5], \
 [6, 'Koke', True, 27, 7.5, 9.6, 10.3, 6.5, 5.6], \
 [7, 'Joao', True, 25, 10.5, 8.4, 9.0, 8.6], \
 [8, 'Saul', True, 24, 9.5, 8.9, 10.0, 9.6], \
 [9, 'Suarez', False, 33, 8.6, 7.5], \
 [10, 'Lionel', False, 33, 10.0, 11.1, 9.8, 8.5,10.1], \
 [19, 'Odriozola', True, 25, 9.5], \
 [14, 'Araujo', False, 21, 8.9, 9.5], \
 [15, 'Valverde', False, 22, 9.9, 10.2], \
 [16, 'Pedri', True, 18, 10.5, 11, 9.5, 10.6], \
 [22, 'Hermoso', False, 23, 10, 7.5, 6.6], \
 [23, 'Iago', True, 33, 11.1, 9.0, 9.3, 8.8],
 [24, 'Maguire',True]]

def jugComKm(lst:list, x:float)-> list:
    
    list_comunitario = []
    for i in lst:
        if i[2] == True:
            list_comunitario.append(i)
            
    output = []
    to_sum = []
    
    for i in list_comunitario:
        if 4 == len(i):
            to_sum = [0] ##Hacemos este truco por si hay jugadores sin jugar ningún partido (Le damos un valor de 0 a al suma)
        else:  
            for k in range(4,len(i)):
                to_sum.append(i[k]) #Aqui vamos escogiendo todos los km de los partidos jugados para cada jugador (Desde la posición 3 en la lista, hasta la posición len(i))
        suma_km=sum(to_sum)
        if len(i) <5:
            matches=1
        elif len(i) > 4:
            matches=len(i)-4
        output.append([i[1],suma_km/matches]) ## Aquí no reiniciamos nada. Queremos recoger todos los resultados de hacer la suma (Y luego la media)
        to_sum = [] ## Iniciamos cada vez to_sum (=[]), ya que solo queremos que nos recoja todos los items de una lista dentro de la lista y no que vaya acumulando todo
    
    jugadores=[]
    for i in output:
        if i[1] > x:
            jugadores.append(i[0])
    
    jugadores.sort()
    
    
    
    return jugadores
         

            




 



# In[ ]:


lst_equipo = [[3, 'Pique', True, 33, 10.2, 9.0], \
[4, 'Ramos', True, 34, 11.0, 11.1, 9.8, 8.5], \
[6, 'Koke', True, 27, 7.5, 9.6, 10.3, 6.5, 5.6], \
[7, 'Joao', True, 25, 10.5, 8.4, 9.0, 8.6], \
[8, 'Saul', True, 24, 9.5, 8.9, 10.0, 9.6], \
[9, 'Suarez', False, 33, 8.6, 7.5], \
[10, 'Lionel', False, 33, 10.0, 11.1, 9.8, 8.5,10.1], \
[19, 'Odriozola', True, 25, 9.5], \
[14, 'Araujo', False, 21, 8.9, 9.5], \
[15, 'Valverde', False, 22, 9.9, 10.2], \
[16, 'Pedri', True, 18, 10.5, 11, 9.5, 10.6], \
[22, 'Hermoso', False, 23, 10, 7.5, 6.6], \
[23, 'Iago', True, 33, 11.1, 9.0, 9.3, 8.8],[35, 'Maguire', True, 33, 24.2, 2.0, 3.3, 8.8]]
   
print(jugComKm(lst_equipo, 10),jugComKm(lst_equipo, 10.2),jugComKm(lst_equipo, 10.5),jugComKm(lst_equipo, 9.5),jugComKm(lst_equipo, 9.4))
   


