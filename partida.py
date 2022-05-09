

class Partida():
    def __init__(self, obj_jugador, obj_modo,col_preguntas) -> None:
        self.__jugador = obj_jugador
        self.__modo = obj_modo
        self.__col_preguntas = col_preguntas
        self.__marcador = self.iniciar
        
    
    @property
    def jugador(self):
        return self.__jugador
    
    @property
    def modo(self):
        return self.__modo
    
    @property
    def col_preguntas(self):
        return self.__col_preguntas
    
    @property
    def marcador(self):
        return self.__marcador
    
    def iniciar(self):
        print(self.__jugador)
        print(self.__modo)
        print(self.__col_preguntas)
        print(self.__col_preguntas[0].respuestas)
        print(self.__marcador)
    
    def estetica(self):
        print("--------TRIVIAL--------")
        print(" -Jugadores: ")

        for jug in self.__jugador:
            print("{0}".format(jug))

        print("  -Parametros:  ")  
        print("     -Preguntas = {0}".format(self.__modo.num_jugadores))  
        print("     -Tiempo partida = {0}".format(self.__modo.tmax_juego))
        print("     -Tiempo respuestas = {0}".format(self.__modo.tmax_pregunta))
        print("------------------------")


    def finalizar(self):
        pass

    def barajar(self):
        pass

    def comprobar_resp(self, id_pregunta, id_respuesta):
        comprobar = self.pregunta[id_pregunta].respuestas[id_respuesta].correcta
        return comprobar == 1
        
    
    def actualizar_puntos(self):
        # if comprobar_resp()
        # self.__jugador.resultado += 1
        pass

    


