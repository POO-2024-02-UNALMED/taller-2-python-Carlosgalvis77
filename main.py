class Asiento:
    def __init__(self, color: str, precio: int, registro: int):
        self.color = color 
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, cambiar_color: str):
        colores_disponibles = ["rojo", "verde", "amarillo", "negro", "blanco"]
        for i in colores_disponibles:
            if i == cambiar_color:
                self.color = cambiar_color


class Motor:
    def __init__(self, numero_Cilindros: int, tipo: str, registro: int):
        self.numero_Cilindros = numero_Cilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, nuevo_registro: int):
        self.registro = nuevo_registro

    def asignarTipo(self, nuevo_tipo: str):
        if nuevo_tipo == "gasolina" or nuevo_tipo == "electrico":
            self.tipo = nuevo_tipo


class Auto:
    cantidadCreados = 0
    def __init__(self, modelo: str, precio: int, asientos :list, marca: str, motor:Motor, registro: int):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    
    def cantidadAsientos(self):
        contador = 0
        for i in self.asientos:
            if isinstance(i, Asiento):
                contador += 1
        return contador
    
    def verificarIntegridad(self):
        if self.registro != self.motor.registro:
            return "Las piezas no son originales"
        for i in self.asientos:
            if isinstance(i, Asiento):
                if self.registro != i.registro:
                    return"Las piezas no son originales"
        return "Auto original"