class Animal(object): # in loc de object este obiect de la care mosteneste
	def __init__(self, age):
		self.age = age
		self.name = None

	def get_age(self):
		return self.age

	def get_name(self):
		return self.name

	def set_age(self, newAge):
		self.age = newAge

	def set_name(self, newName):
		self.name = newName

	def __str__(self):
		return "Animalul: " + self.name + " este de varsta " + str(self.age)

urs = Animal(10)
urs.name = "ionut"
print(urs)

class Cat(Animal): # mostenire
	def miau(self):
		print("meow")

	def __str__(self):
		return "miau miau, miau miau miau :("

cat = Cat(3)
cat.set_name("kitty")
cat.miau()
print(cat)

class Person(Animal):
	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.friends = []

	def get_friends(self):
		return self.friends

	def add_friend(self, friend):
		if friend not in self.friends:
			self.friends.append(friend)
			friend.add_friend(self)

	def age_dif(self, personTwo):
		return (((self.age - personTwo.age)**2)**0.5)

	def __str__(self):
		if len(self.friends) != 0:
			currentString = self.name + ", " + str(self.age) + " has many friends: "
			for friend in self.friends:
				currentString += friend.get_name()
				currentString += " "
			return currentString
		else:
			return self.name + ", " + str(self.age) + " has no friends :("

	def speak(self):
		print("Hello")

p1 = Person("ion", 10)
p2 = Person("mihai", 20)
p3 = Person("marcel", 21)

print(p1)
p1.add_friend(p2)
print(p1)
p1.add_friend(p2)
print(p1)
p1.add_friend(p3)
print(p1)
print(p1.age_dif(p2))
print(p2.age_dif(p1))
print(p3.age_dif(p1))
print(p2)

