import itertools

def divisors(num):
	"""Gegeven een getal, zoek alle delers van dit getal"""
	divs = []
	for i in range(1, int(num ** 0.5)):
		if num % i == 0:
			divs.append(i)
	return divs

def product(lst):
	"""Gegeven een lijst met getallen, bereken hun product"""
	p = 1
	for el in lst:
		p *= el
	return p

# het alfabet (hoofdletters)
ALPH = "".join(chr(x) for x in range(ord("A")-1, ord("Z")+1))

# de sommen en producten uit de puzzel
sums = [22, 67, 59, 56, 77, 72, 30, 67]
prods = [216, 67200, 24840, 21450, 122892, 95760, 3150, 61560]

# itereer over zowel sommen als producten
for (SUM, PRODUCT) in zip(sums, prods):
	# maak combinaties van 5 getallen uit de delers van het product
	for com in itertools.combinations_with_replacement(divisors(PRODUCT), 5):
		# controleer voor de getallen in deze combinaties:
		# - alle getallen in het alfabet zitten
		# - de som van de getallen gelijk is aan de gezochte som
		# - het product van de getallen gelijk is aan het gezochte product
		if max(com) <= 26 and sum(com) == SUM and product(com) == PRODUCT:
			# laat de oplossing zien, maar stop niet want er zijn mogelijk meer opties
			print("".join([ALPH[i] for i in com]), end=" ")
	# zet de volgende som/product-combinatie op de volgende regel
	print()
