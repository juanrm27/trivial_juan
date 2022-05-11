class Modo():
    def __init__(self, 
                tmax_juego= 60, 
                tmax_pregunta=20, 
                num_preguntas=15, 
                num_jugadores=1) -> None:
    
        self.__tmax_juego    = tmax_juego
        self.__tmax_pregunta = tmax_pregunta
        self.__num_preguntas = num_preguntas
        self.__num_jugadores = num_jugadores

    @property
    def tmax_juego(self):
        return self.__tmax_juego
    
    @tmax_juego.setter
    def tmax_juego(self, tj):
        self.__tmax_juego = tj

    @property
    def tmax_pregunta(self):
        return self.__tmax_pregunta
    
    @tmax_pregunta.setter
    def tmax_pregunta(self, tp):
        self.__tmax_pregunta = tp

    @property
    def num_preguntas(self):
        return self.__num_preguntas
    
    @num_preguntas.setter
    def num_preguntas(self, np):
        self.__num_preguntas = np
    
    @property
    def num_jugadores(self):
        return self.__num_jugadores

    @num_jugadores.setter
    def num_jugadores(self, nj):
        self.__num_jugadores = nj 