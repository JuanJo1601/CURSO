class Curso:

    """-------------------------------
    # Atributos
    -------------------------------"""

    nota = [4, 5, 3, 2, 3.5, 1, 3.5, 4, 3.5, 5, 4.5, 4.2]

    """-------------------------------
    # Metodos
    -------------------------------"""
    def __init__(self):
        self.__nota = [4, 5, 3, 2, 3.5, 1, 3.5, 4, 3.5, 5, 4.5, 4.2]

    def numeroDeArreglos (self):
        numeroDeArreglos = len (self.nota)
        return numeroDeArreglos    

    def promedio (self):

        suma = 0.0
        indice = 0

        while indice <= 12:
            suma = suma + self.__nota[indice]
            indice += 1 

    def hayAlgunCinco_uno(self):
        i=0
        hayCinco = False
        
        while (i < len(self.__nota)) and not hayCinco:
            if (self.__nota[i] == 5):
                hayCinco = True
            i+=1

        return hayCinco
    
    def hayAlgunCinco__dos(self):
        hayCinco = False

        for i in range(len(self.__nota)):
            if (self.__nota[i] == 5):
                hayCinco = True
                break

        return hayCinco

    def hayAlgunCinco_tres(self):
        hayCinco = False
        for nota in self.__nota:
            if nota is 5:
                hayCinco = True
                break

        return hayCinco

#Encontrar a las 3 primeras notas de 1.5 y asignar 2.5
    def asignarNotas(self):
        
#Retornar la posición de la secuecia de la secuencia de la 3 nota con valor 5, si dicha nota no aparece 3 veces el metodo debe retornar el valor de -1
    def retronarPosicion(self):
        for i in range(len(self.__nota)):
            if self.__nota[i] == 5:
                return i
            
