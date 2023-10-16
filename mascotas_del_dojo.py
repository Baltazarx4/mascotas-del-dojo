class Ninja:
    def __init__( self, nombre, apellido, premios, comida_mascota, mascota ):
        self.nombre= nombre
        self.apellido= apellido
        self.premios= premios
        self.comida_mascota= comida_mascota
        self.mascota= mascota
# implementa los siguientes métodos:
# caminar(): pasea a la mascota del ninja invocando el método de mascota jugar()
    def  caminar(self):
        self.mascota.jugar()
# alimentar(): alimenta a la mascota del ninja invocando el método de mascota comer()
    def alimentar(self):
        self.mascota.comer()
# bañar(): limpia la mascota del ninja invocando el método de mascota sonido()
    def bañar(self):
        self.mascota.sonido()




class Mascota:
    def __init__( self, name , tipo , golosinas ):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = 100
        self.energia = 100
# implementa los siguientes métodos:
# dormir() - incrementa la energía de la mascota en 25
    def dormir(self):
        self.energia += 25
# comer() - incrementa la energía de la mascota en 5 y la salud en 10
    def comer(self):
        self.energia += 5
        self.salud += 10
# jugar() - incrementa la salud de la mascota en 5
    def jugar(self):
        self.salud += 5
# ruido() - imprime el sonido que produce la mascota
    def sonido(self):
        print(f"{self.name} hace un ruido.")
class Gato(Mascota):
    def sonido(self):
        print(f"{self.name} hace un ruido de 'Miau'.")

class Perro(Mascota):
    def sonido(self):
        print(f"{self.name} hace un ruido de 'Guau'.")


# Ejemplo de uso:
mascota1 = Mascota("Luna", "Perro", 3)
ninja1 = Ninja("Naruto", "Uzumaki", "Campeón", "Croquetas", mascota1)

ninja1.caminar()
ninja1.alimentar()
ninja1.bañar()

print(f"Salud de {mascota1.name}: {mascota1.salud}")
print(f"Energía de {mascota1.name}: {mascota1.energia}")