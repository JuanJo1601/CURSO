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
