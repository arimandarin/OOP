class Vehiculos():

	def __init__(self, marca, modelo): #constructor

		self.marca=marca
		self.modelo=modelo

		self.marcha=False
		self.acelera=False
		self.frena=False
		
	def arrancar(self):
		self.marcha=True #cambia estado de variables del constructor

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.marcha,
			"\nAcelerando:", self.acelera,"\nFrenando:", self.frena)

class Furgoneta(Vehiculos):#hereda las caractericticas y comportamientos de vehiculos

	def carga(self, cargar):
		self.cargado=cargar

		if self.cargado:
			return "Furgoneta cargada"
		else:
			return "Furgoneta no cargada"


class Moto(Vehiculos): #hereda las caractericticas y comportamientos de vehiculos
	
	def caballito(self): #comportamiento especifico de la moto
		self.willie=False

	def estado(self):  #se sobreescribe, dentro de la clase moto, para poder agregar el estado de willie/caballito
		print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.marcha,
			"\nAcelerando:", self.acelera,"\nFrenando:", self.frena, "\nHaciendo la willie:", self.willie)

class Electricos(Vehiculos): 

  	def __init__(self, marca, modelo):

  		super().__init__(marca, modelo)
  		self.autonomia=100 #100km

  	def cargarEnergia(self):
  		self.cargando=True



miMoto=Moto("Kawasaki", "Ninja")

miMoto.caballito()

miMoto.estado() #llama al estado de moto, no de vehiculos, ya que se sobreescribe el estado y anula el anterior

print("----------")

miFurgon=Furgoneta("Volkswagen", "Transporter")

miFurgon.arrancar()

miFurgon.estado()

print(miFurgon.carga(True))


class BicicletaElectrica(Electricos, Vehiculos): #en herencia multiple, se da preferencia a la primera herencia, y entonces hereda el constructor de electricos
	pass


miBici=BicicletaElectrica("Orbea", "HQ1407")