#MEHMET TUGRUL SAVRAN
#MIT 2018

#THIS IS A SIMULATOR FOR THE MOTION OF A GAS PARTICLE IN A CONTAINER, POSSIBLY WITH WALLS 
#REPEATED CALLING OF THE STEP FUNCTION WILL SIMULATE COLLISION BETWEEN PARTICLES, PARTICLE-WALL AND PROPAGATION

def step(gas):
   #Mynotes:
   #Gas is a dictionary
   #the key "state" is a list of lists
	liste = gas["state"]
	width = gas["width"] 
	height = gas["height"]
	uzunluk = gas["width"] * gas["height"]
	newgas = []
	for i in range(uzunluk):
		newgas.append([]) #Constructing a new gas 

	for i in range(uzunluk):
		if "w" not in liste[i]: #So it is either a particle-particle collision or simple propagation
			if len(liste[i]) == 1: #simple propagation
				direction = liste[i][0]
				if direction == "d":
					if not i >= uzunluk - width: #Checking if this particle is at bottom
						newgas[i+width].append(direction)
				if direction == "u":
					if not i <= width - 1: #Checking if particle at top 
						newgas[i-width].append(direction)
				if direction == "l":
					if not i%width == 0: #Check if particle is at left-most cell
						newgas[i-1].append(direction)	
				if direction == "r":
					if not i%width == width -1: #Check if particle is at right-most cell 
						newgas[i+1].append(direction)
			else: #A particle-particle collision 
				if liste[i] == ["r","l"] or liste[i] == ["l","r"]:
					if i <= width - 1: #Check if particle is at top row 
						newgas[i+width].append("d")
					elif i >= uzunluk - width: #Check if particle is at bottom row
						newgas[i-width].append("u")
					else:
						newgas[i-width].append("u")
						newgas[i+width].append("d")
				elif liste[i] == ["u","d"] or liste[i] == ["d","u"]:
					if i%width == 0: #Check if particle at left-most cell 
						newgas[i+1].append("r")
					elif i%width == (width -1): #Check if particle at right-most cell 
						newgas[i-1].append("l")
					else: 
						newgas[i+1].append("r")
						newgas[i-1].append("l")	
				else: #When it doesn't obey 6.009 collision rules. The directions remain the same but just propagate
					for x in liste[i]:
						if x == "d":
							if not i >= uzunluk - width: #Checking if this particle is at bottom
								newgas[i+width].append(x)
						if x == "u":
							if not i <= width - 1: #Checking if particle at top 
								newgas[i-width].append(x)
						if x == "l":
							if not i%width == 0: #Check if particle is at left-most cell
								newgas[i-1].append(x)	
						if x == "r":
							if not i%width == width -1: #Check if particle is at right-most cell 
								newgas[i+1].append(x)
		else: #Wall collision
			newgas[i].append("w")
			if "u" in liste[i]:
				newgas[i+width].append("d")
			elif "d" in liste[i]:
				newgas[i-width].append("u")
			elif "l" in liste[i]:
				newgas[i+1].append("r")
			elif "r" in liste[i]:
				newgas[i-1].append("l")
	newgastate = {}
	newgastate["width"] = width
	newgastate["height"] = height
	newgastate["state"] = newgas
	return newgastate

#####Testing######   DELETE THIS PART BEFORE SUBMISSION

# gas_3 = { "width": 3,
# "height": 4,
# "state": [  ["w"], ["w"], ["w"],
# 			["w"], ["r","l"], ["w"],
# 			["w"], [ ], ["w"],
# 			["w"], ["w","d"], ["w"] ] }

# yenigaz = {
# "width": 2,
# "height": 2,
# "state": [ [""], ["d","u","r","l"], [""],
# [""]] }

# print step(yenigaz)























