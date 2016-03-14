# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 20:33:38 2016

@author: Adrian
"""
import os #Se importa la librería os que permite leer y escribir documentos
import matplotlib.image as mpimg #Se importa la librería matplotlib.image para obtener la imagen a través de su dirección
import csv #Se importa la libreriía csv para leer y escribir archivos con extención csv
from tkinter.filedialog import askopenfilename  #Se importa la librería tkinter.filedialog para abrir el explorador de archivos
from math import sqrt #Se importa la librería math sqrt para obtener la raíz en la distancia euclidean

file_name = askopenfilename() #Se obtiene el nombre del la imagen
img_to_class = mpimg.imread(file_name) #Se obtiene la imagen a través de su nombre con el método mping.imread que recive como parametro la dirección en la imagen

#Nombre Función:euclidean
#Descripción: Obtiene la distancia euclidiana de las características de la imagen a reconocer con las de el dataset
#Argumentos de entrada: arreglo de características de imagen a reconocer, arreglo de características de imagen en dataset
#Retorno: Distancia euclidiana entre los parametros de entrada,es flotante
def euclidean(x, y): #Inicialización de la función
    return sqrt( sum( [ (xi - yi)**2 for xi, yi in zip(x, y) ] ) ) #Operación para obtener la distancia.
    

#Nombre Función:carImg
#Descripción: Obtiene las característicasde la imagen : numero de 1's de la imagen,numero de 1's en las columnas y filas que están a un cuarto, a la mitad y a tres cuartos y los cortes que se generan en estos vectores 
#Argumentos de entrada: Imagen a analizar y opción para saber si se trada de una imagen del dataset o imagen a clasificar
#Retorno: Lista que contiene las características de la imagen
def carImg(imagen,opcion):  #Inicialización de la función  
    im=imagen.size #Se obtiene el tamaño de la imagen en píxeles
    num_unos=0 #Se inicializa la variable de número de 1's que hay en la imagen
    alto=len(imagen) #Se obtiene el alto de la imagen en píxeles
    ancho=int(im/alto) #Se ontiene el ancho de la imagen en píxeles
    total=alto/ancho #Se obtiene la relación entre filas y columnas de la imagen
    ancho_mitad=0 #Se inicializa la variable de 1's que se encuentran en la columna de la mitad 
    ancho_cuarto=0 #Se inicializa la variable de 1's que se encuentran en la columna de un cuarto de la imagen
    ancho_3cuartos=0 #Se inicializa la variable de 1's que se encuentran en la columna de tres cuartos de la imagen
    alto_mitad=0 #Se inicializa la variable de 1's que se encuentran en la fila de la mitad 
    alto_cuarto=0 #Se inicializa la variable de 1's que se encuentran en la fila de un cuarto de la imagen 
    alto_3cuartos=0 #Se inicializa la variable de 1's que se encuentran en la fila de tres cuartos de la imagen
    corte_1ancho=imagen[0][int(ancho/2)] #Se inicializa el valor a el primer pixel de la columna de la mitad
    corte_2ancho=imagen[0][int(ancho/4)] #Se inicializa el valor a el primer pixel de la columna de un cuarto de la imagen
    corte_3ancho=imagen[0][int(ancho/4)*3] #Se inicializa el valor a el primer pixel de las columna de tres cuartos de la imagen
    contador_c1=0 #Se inicializa en cero el contador de cortes de la columna de la mitad de la imagen
    contador_c2=0 #Se inicializa en cero el contador de cortes de la columna de un cuarto de la imagen
    contador_c3=0 #Se inicializa en cero el contador de cortes de la columna de tres cuartos de imagen
    corte_1alto=imagen[int(alto/2)][0] #Se inicializa el valor a el primer pixel de la fila de la mitad de la imagen
    corte_2alto=imagen[int(alto/4)][0] #Se inicializa el valor a el primer pixel de la fila de tres cuartos de la imagen
    corte_3alto=imagen[int(alto/4)*3][0] #Se inicializa el valor a el primer pixel de la fila de cuatro cuartos de la imagen
    contador_ca1=0  #Se inicializa en cero el contador de cortes de la fila de la mitad de la imagen
    contador_ca2=0  #Se inicializa en cero el contador de cortes de la fila de un cuarto de la imagen
    contador_ca3=0 #Se inicializa en cero el contador de cortes de la fila de tres cuartos de imagen
    
    for a in range(alto): #Se configura el for para leer las columnas
            for b in range(ancho): #Se configura el for para leer las filas
                nu=(int(imagen[a][b])) #nu indica la posción en la imagen
                
                if b==int(ancho/2): #Cuando se encuentre en la columna de la mitad 
                    if corte_1ancho != nu: #Revisa si la variable corte1ancho es diferente al apuntador
                        corte_1ancho=nu #Si se cumple adquiere el valor del apuntdador
                        contador_c1=contador_c1+1 # Y suma al contador de cortes en la columna de la mitad de la imagen
                    if nu==1: #Verifica si el apuntador tiene el valor de uno
                        ancho_mitad=ancho_mitad+1 #Si se cumple la condición el contador de unos en la columna de la mitad de la imagen aumenta
                        #ancho_mitad=ancho_mitad/im #Y se divide entre la relación de filas y columnas
                                                
                if b==int(ancho/4): #Cuando se encuentre en la columna de un cuarto de la imagen
                    if corte_2ancho != nu:#Revisa si la variable corte2ancho es diferente al apuntador
                        corte_2ancho=nu #Si se cumple adquiere el valor del apuntdador
                        contador_c2=contador_c2+1  # Y suma al contador de cortes en la columna de un cuarto de la imagen
                    if nu==1: #Verifica si el apuntador tiene el valor de uno
                        ancho_cuarto=ancho_cuarto+1 #Si se cumple la condición el contador de unos en la columna de un cuarto de la imagen aumenta
                        #ancho_cuarto=ancho_cuarto/im #Y se divide entre la relación de filas y columnas
                        
                if b==int(ancho/4)*3: #Cuando se encuentre en la columna de tres cuartos de la imagen
                    if corte_3ancho != nu:#Revisa si la variable corte3ancho es diferente al apuntador
                        corte_3ancho=nu #Si se cumple adquiere el valor del apuntdador
                        contador_c3=contador_c3+1 # Y suma al contador de cortes en la columna de tres cuartoa de la imagen
                    if nu==1:  #Verifica si el apuntador tiene el valor de uno
                        ancho_3cuartos=ancho_3cuartos+1 #Si se cumple la condición el contador de unos en la columna de tres cuartos de la imagen aumenta
                        #ancho_3cuartos=ancho_3cuartos/im #Y se divide entre la relación de filas y columnas
                        
                if a==int(alto/2): #Cuando se encuentre en la fila de la mitad 
                    if corte_1alto != nu: #Revisa si la variable corte1alto es diferente al apuntador
                        corte_1alto=nu #Si se cumple adquiere el valor del apuntdador
                        contador_ca1=contador_ca1+1 # Y suma al contador de cortes en la fila de la mitad de la imagen
                    if nu==1:  #Verifica si el apuntador tiene el valor de uno
                        alto_mitad=alto_mitad+1  #Si se cumple la condición el contador de unos en la fila de la mitad de la imagen aumenta
                        #alto_mitad=alto_mitad/im  #Y se divide entre la relación de filas y columnas
                        
                if a==int(alto/4): #Cuando se encuentre en la fila de un cuarto de la imagen
                    if corte_2alto != nu: #Revisa si la variable corte2alto es diferente al apuntador
                        corte_2alto=nu #Si se cumple adquiere el valor del apuntdador
                        contador_ca2=contador_ca2+1 # Y suma al contador de cortes en la fila de un cuarto de la imagen
                    if nu==1: #Verifica si el apuntador tiene el valor de uno
                        alto_cuarto=alto_cuarto+1 #Si se cumple la condición el contador de unos en la fila de un cuarto de la imagen aumenta
                        #alto_cuarto=alto_cuarto/im  #Y se divide entre la relación de filas y columnas
                                                
                if a==int(alto/4)*3: #Cuando se encuentre en la fila de tres cuartos de la imagen
                    if corte_3alto != nu:#Revisa si la variable corte3alto es diferente al apuntador
                        corte_3alto=nu #Si se cumple adquiere el valor del apuntdador
                        contador_ca3=contador_ca3+1 # Y suma al contador de cortes en la fila de tres cuartos de la imagen
                    if nu==1: #Verifica si el apuntador tiene el valor de uno
                        alto_3cuartos=alto_3cuartos+1 #Si se cumple la condición el contador de unos en la fila de tres cuartos de la imagen aumenta
                        #alto_3cuartos=alto_3cuartos/im  #Y se divide entre la relación de filas y columnas
                        
                if nu==1: #Verifica si el apuntador tiene el valor de uno
                    num_unos=num_unos+1   #Aumenta el contador de unos de la imagen 
                    
                long = int (len(dir_name))  #Se obtiene la longitud del nombre de la imagen              
                clas= dir_name[long-1] #Se obtiene el último valor de la cadena para obtener la clase
                clase=int(clas) #Se castea y convierte a int la clase debido a que s trata de puros números
    if opcion==1: #Si el parámetro de opción es igual a uno se obtienen las características de las imagenes del dataset
        return num_unos, total, ancho_mitad, ancho_cuarto, ancho_3cuartos, alto_mitad, alto_cuarto, alto_3cuartos, contador_c1, contador_c2, contador_c3, contador_ca1, contador_ca2, contador_ca3,clase #Se regresan las 14 características y la clase de la imagen
    if opcion==2: #Si el parámetro de opción es igual a dos, se obtienen las características de la imagen a clasificar
        return num_unos, total, ancho_mitad, ancho_cuarto, ancho_3cuartos, alto_mitad, alto_cuarto, alto_3cuartos, contador_c1, contador_c2, contador_c3, contador_ca1, contador_ca2, contador_ca3 #Se regresan solamente las 14 características sin la clase
    
#Generar DataSet
print("Generando dataset")
root_dir = 'numeros' #Se obtiene el nombre de la carpeta que contiene los número a analizar
name='' #Se declara una variable sin valor 
matriz_dataset=[] #Se declara una matriz que guardará los datos de las características de las imagenes
for dir_name, subdir_list, file_list in os.walk(root_dir):   #Se leen todos los directorios       
    for fname in file_list: #Se leen los archivos de los directorios
        name=dir_name+"/"+fname #Se obtiene el el nombre y dirección de la imagen
        img = mpimg.imread(name) #Se obtiene la imagen a través de su dirección y nombre
        arreglo=list(carImg(img,1)) #Se genera una lista que será agregada a la matriz y se utiliza la función carImg para optener las características y como es de las imagenes del dataset se le pone 1         
        matriz_dataset.append(arreglo) #Se agrega la lista  a la matriz que los conendrá 

datos = matriz_dataset #Datos obtine el valor de la matriz con las características de las imagenes
csv_salida = open('dataset.csv', 'w', newline='') #Crea y abre el archivo csv 
salida = csv.writer(csv_salida) #Índica que se escribirán datos en el csv
salida.writerows(datos) #Escribe los datos de la lista en el documento csv
del salida #Se finaliza la escritura
csv_salida.close() #Se cierra el archivo csv
print("DataSet generado") #Se imprime que el dataset esta listo 

#Leer características de la imgen
car_img_class=list(carImg(img_to_class,2)) #Se obtienen las características de la imagen a clasificar con la funcion carImg y la opción dos para no regresar una clase 
print(car_img_class) #Se imprimen las características de la imagen a clasificar
print("Características de imagen a clasificar leidos") #Se imprime que las características de la imagen están listas

#Pedir Vecinos
num_vecinos = int(input("Introduce el número de vecinos: "))#Se pide el número de vecinos

#Leer DataSet
size_matriz=0 #Se inicializa en cero esta variable para despues saber el total de elementos del dataset
matriz_data=[] #Se declara una matriz que recibirá los datos del dataset
f = open('dataset.csv') #Se abre el archivo csv que es el dataset
lns = csv.reader(f,delimiter=',') #Se declara el separador de las características, el cual es una coma","
lns = csv.reader(f) #Se declara el lector de las lineas
for line in lns:#Se inicializa el for que leera linea por linea del dataset
    matriz_data.append(line) #Se agregan las listas del dataset a la matriz 
    size_matriz=size_matriz+1 #Se aumenta el contador de elementos por cada linea insertada
 
#Obtener distancia
matriz_vecinos=[] #Se crea una matriz vacia que guardará los valores de la distancia, posición y clase de las imagenes analizadas 
for i in range(size_matriz): # Se crea un for para leer la matriz 
    for e in range(14):#Se declara un for para leer los datos de las listas de la matriz
        matriz_data[i][e]=float(matriz_data[i][e])#Se convierten los datos a flotantes para poder usarlos en la función de la distancia
   
for pos_mat in range(size_matriz): #Se crea un for que leera las filas de la matriz
    dist=(euclidean(matriz_data[pos_mat],car_img_class)) #Se manda a llamar la función de la distancia para optener la distancia de las imegenes del dataset con la que se va a clasificar     
    matriz_vecinos.append([dist,pos_mat,int(matriz_data[pos_mat][14])]) #Se guardan los datos en la matriz de vecinos
matriz_vecinos=sorted(matriz_vecinos) #Se ordenan de menor a mayor para obtener los de menor distancia

print("*********INFORMACIÓN GENERAL*********") #Se imprime título de información general
print("Número de instancias en el Dataset:",size_matriz)#Elementos del dataset
print("Número de características:",14) #Número de características recolectadas
print("Número de clases:",10) #Número de clases, debido a que son puros número, sólo son 10 clases
print("Clases: 0,1,2,3,4,5,6,7,8,9") #Se imprime cuales son las clases
print("*********INFORMACIÓN VECINOS*********") #Se imprime titulo de la información de vecinos
print("#Vecino\tDistancia\t\tPosición Clase")#Se imprime la cabecera de los elemtos que van a aparecer
for i in range(num_vecinos): #Se crea un for para imprimir la información de los vecinos mas cercanos 
    matriz_num_vecinos=i+1,matriz_vecinos[i][0],matriz_vecinos[i][1],matriz_vecinos[i][2]#Esta matriz tendra el numero de vecino, su distancia, posición en el dataset y su clase
    print(matriz_num_vecinos[0],"\t",matriz_num_vecinos[1],"\t",matriz_num_vecinos[2],"\t",matriz_num_vecinos[3])#Se imprime la matriz
print("***********RESUMEN VECINOS***********")#Se imprime el título de el resumen de los vecinos
print("Instancias\tClase")#Se imprime la cabecera de los datos que se mostrarán
cero=0 #Se inicializa el contador de los ceros
uno=0 #Se inicializa el contador de los uno
dos=0 #Se inicializa el contador de los dos_ins
tres=0 #Se inicializa el contador de los tres
cuatro=0 #Se inicializa el contador de los cuatro
cinco=0 #Se inicializa el contador de los cinco
seis=0 #Se inicializa el contador de los seis
siete=0 #Se inicializa el contador de los siete
ocho=0 #Se inicializa el contador de los ocho
nueve=0 #Se inicializa el contador de los nueve
cero_ins=0 #Se inicializa el contador de los ceros
uno_ins=0 #Se inicializa el contador de los uno para las instancias totales
dos_ins=0 #Se inicializa el contador de los dos para las instancias totales
tres_ins=0 #Se inicializa el contador de los tres para las instancias totales
cuatro_ins=0 #Se inicializa el contador de los cuatro para las instancias totales
cinco_ins=0 #Se inicializa el contador de los cinco para las instancias totales
seis_ins=0 #Se inicializa el contador de los seis para las instancias totales
siete_ins=0 #Se inicializa el contador de los siete para las instancias totales
ocho_ins=0 #Se inicializa el contador de los ocho para las instancias totales
nueve_ins=0 #Se inicializa el contador de los nueve para las instancias totales

for i in range(num_vecinos): #Se crea un for para ir almacenando el número de vecinos de cada clase
    if matriz_vecinos[i][2]==0: #Si el elemento señalado en dicha posición es igual a cero 
        cero=cero+1             # Se incrementa el contador de los ceros
    elif matriz_vecinos[i][2]==1:#Si el elemento señalado en dicha posición es igual a uno 
        uno=uno+1               # Se incrementa el contador de los unos
    elif matriz_vecinos[i][2]==2:#Si el elemento señalado en dicha posición es igual a dos
        dos=dos+1               # Se incrementa el contador de los dos
    elif matriz_vecinos[i][2]==3:#Si el elemento señalado en dicha posición es igual a tres
        tres=tres+1             # Se incrementa el contador de los tres
    elif matriz_vecinos[i][2]==4:#Si el elemento señalado en dicha posición es igual a cuatro
        cuatro=cuatro+1        # Se incrementa el contador de los cuatros
    elif matriz_vecinos[i][2]==5:#Si el elemento señalado en dicha posición es igual a cinco
        cinco=cinco+1           # Se incrementa el contador de los cincos
    elif matriz_vecinos[i][2]==6:#Si el elemento señalado en dicha posición es igual a seis
        seis=seis+1             # Se incrementa el contador de los seis
    elif matriz_vecinos[i][2]==7:#Si el elemento señalado en dicha posición es igual a siete
        siete=siete+1           # Se incrementa el contador de los sietes
    elif matriz_vecinos[i][2]==8:#Si el elemento señalado en dicha posición es igual a ocho
        ocho=ocho+1             # Se incrementa el contador de los ochos
    elif matriz_vecinos[i][2]==9:#Si el elemento señalado en dicha posición es igual a nueve
        nueve=nueve+1           # Se incrementa el contador de los nueves
        
for i in range(size_matriz): #Se crea un for para ir almacenando el número de instancias de cada clase
    if matriz_data[i][14]=='0': #Si el elemento señalado en dicha posición es igual a cero 
        cero_ins=cero_ins+1             # Se incrementa el contador de los ceros
    elif matriz_data[i][14]=='1':#Si el elemento señalado en dicha posición es igual a uno 
        uno_ins=uno_ins+1               # Se incrementa el contador de los unos
    elif matriz_data[i][14]=='2':#Si el elemento señalado en dicha posición es igual a dos
        dos_ins=dos_ins+1               # Se incrementa el contador de los dos
    elif matriz_data[i][14]=='3':#Si el elemento señalado en dicha posición es igual a tres
        tres_ins=tres_ins+1             # Se incrementa el contador de los tres
    elif matriz_data[i][14]=='4':#Si el elemento señalado en dicha posición es igual a cuatro
        cuatro_ins=cuatro_ins+1        # Se incrementa el contador de los cuatros
    elif matriz_data[i][14]=='5':#Si el elemento señalado en dicha posición es igual a cinco
        cinco_ins=cinco_ins+1           # Se incrementa el contador de los cincos
    elif matriz_data[i][14]=='6':#Si el elemento señalado en dicha posición es igual a seis
        seis_ins=seis_ins+1             # Se incrementa el contador de los seis
    elif matriz_data[i][14]=='7':#Si el elemento señalado en dicha posición es igual a siete
        siete_ins=siete_ins+1           # Se incrementa el contador de los sietes
    elif matriz_data[i][14]=='8':#Si el elemento señalado en dicha posición es igual a ocho
        ocho_ins=ocho_ins+1             # Se incrementa el contador de los ochos
    elif matriz_data[i][14]=='9':#Si el elemento señalado en dicha posición es igual a nueve
        nueve_ins=nueve_ins+1   
        
matriz_resumen=[[cero,cero_ins,0],[uno,uno_ins,1],[dos,dos_ins,2],[tres,tres_ins,3],[cuatro,cuatro_ins,4],[cinco,cinco_ins,5],[seis,seis_ins,6],[siete,siete_ins,7],[ocho,ocho_ins,8],[nueve,nueve_ins,9]] #Se guarda el la clase y el número de elementos de cada clase
for i in range(10): #For para imprimir los elementos
    print(matriz_resumen[i][1],"\t",matriz_resumen[i][0],"\t",matriz_resumen[i][2],) #Se imprimen las listas de la matriz con las datos de los vecinos y sus insidencias 

print("************CLASIFICACIÓN************") #Se imprime el título de clasificiación
clase=sorted(matriz_resumen,reverse=True) #Se obtiene la lista que tiene mas insidencias en los vecino seleccionados
print("La imagen es de clase:",clase[0][2]) #Se imprime la clase de la imagen
#The end
