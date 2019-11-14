# functii

def helloWorld():
	print("\n\tHello world\t\n");

#nr = input("Va rugam introduceti un nr\n") # input returneaza de tip string
nr = 1
try:
	int(nr)+7
	print(nr)
	helloWorld()
except:
	print("A aparut o eroare")
else:
	print("Nu a aparut nici o eroare")

#functiile pot lua orice fel de parametrii -> grija la input

def adunare(param1, param2): 
	return param1+param2
def scadere(param1, param2):
	return param1-param2

print(f"scadere si adunare: {scadere(adunare(3,5),10)}")
print(f"adunare str: {adunare('A','B')}")

x = 2
y = 10
def test():
	global x # nu folosi asta
	print(x)
	# print(y) <- genereaza eroare, nu poate accesa variabila de mai sus y = 10
	x = 3
	print(x)
test()

def parametriiOptionali(a, b, *c): #cel putin 2 parametrii
	x = a + b
	if c: # c este o tupla
		print(f"c => {c}")
		for e in c:
			x += e
	return x
print(f"fara parametrii optionali: {parametriiOptionali(1, 1)}")
print(f"cu parametrii optionali: {parametriiOptionali(0, 0, 1, 2, 3, 4)}")

# nume = lambda lista_parametrii_intare: expresie
adunareLambda = lambda a,b: a+b
print(adunareLambda(3,4))
# functiile lambda sunt utilizate pt algoritmi de marime mica
putere = lambda a,b: a**b
print(putere(2,3))