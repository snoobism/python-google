class Coordinate(object):

	# init este constructorul
	def __init__(self, x, y): # self e this din java
		self.x = x
		self.y = y

	def __str__(self): # __str__ poate fi folosit in a descrie clasa de obiect
		# returnam self ca si string
		return "<" + str(self.x) + "," + str(self.y) + ">"

	def __add__(self, other): # self + other
 		return

	def __sub__(self, other): # self - other
		return

	def __eq__(self, other): # verifica daca 2 obiecte sunt egale
		return (self.x == other.x and self.y == other.y)

	def distance(self, other): # other este tot o coordonata
		# returnare distanta euclidiana
		x_diff_sq = (self.x - other.x)**2
		y_diff_sq = (self.y - other.y)**2
		return (x_diff_sq + y_diff_sq)**0.5

	def new():
		print("sth")

c = Coordinate(3, 4)
origin = Coordinate(0, 0)

print(c)

Coordinate.new()

print(c.distance(origin))

print("\n")

class Fraction(object):

	def __init__(self, numarator, numitor):
		if (numitor == 0):
			print("Numitorul e 0, invalid")
		self.numitor = numitor
		self.numarator = numarator

	def __str__(self):
		if (self.numitor == 0):
			return ("Numitorul e 0, invalid")
		else:
			return f"{self.numarator}/{self.numitor}"

	def sum(self, other):
		if (self.numitor == 0):
			print("Numitorul e 0, invalid")
		else:
			result = Fraction(self.numarator * other.numitor + other.numarator * self.numitor, self.numitor * other.numitor)
			return result

	def mul(self, other):
		if (self.numitor == 0):
			print("Numitorul e 0, invalid")
		else:
			result = Fraction(self.numarator * other.numarator, self.numitor * other.numitor) 
			return result

	def dif(self, other):
		if (self.numitor == 0):
			print("Numitorul e 0, invalid")
		else:
			result = Fraction(self.numarator * other.numitor - other.numarator * self.numitor, self.numitor * other.numitor)
			return result

	def div(self, other):
		if (self.numitor == 0):
			print("Numitorul e 0, invalid")
		else:
			result = Fraction(self.numarator * other.numitor, self.numitor * other.numarator) 
			return result

	def __eq__(self, other):
		if (self.numitor == 0):
			print("Numitorul e 0, invalid")
		else:
			return (self.numitor == other.numitor and self.numarator == other.numarator)

	def _float(self):
		if (self.numitor == 0):
			print("Numitorul e 0, invalid")
		else:
			return self.numarator/self.numitor

sfert = Fraction(1, 4)
jum = Fraction(1, 2)

print(sfert)
print(jum)

print(sfert.sum(jum))
print(sfert.dif(jum))
print(sfert.mul(jum))
print(sfert.div(jum))
print(sfert.__eq__(jum))
print(sfert._float())
print(jum._float())

invalid = Fraction(3, 0)
print(invalid)

class intSet(object):
	def __init__(self):
		self.members = []

	def __str__(self):
		return f"{sorted(self.members)}"
	def insert(self, other):
		if isinstance(other, int):
			if other not in self.members:
				self.members.append(other)

	def remove(self, other):
		if other in self.members:
			self.members.remove(other)

	def member(self, other):
		return other in self.members


s = intSet()
print(s)
s.insert(3)
print(s)
s.insert(1)
s.insert(4)
s.insert(3)
print(s)
print(s.member(5))
print(s.member(3))
s.remove(4)
print(s)
s.insert(3.4)
print(s)

