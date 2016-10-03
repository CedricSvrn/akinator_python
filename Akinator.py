



def ajoutElement(elements, questions):
	liste = []
	existe = False
	nom = raw_input("Entrez un nouvel element :").upper()
	liste.append(nom)

	for i in range (0,len(elements)):
		if (elements[i] == liste[0]):
			print("Il existe deja un element nomme :"+liste[0])
			existe = True
	if (not existe):
		for i in range (0,len(questions)):
			liste.append(int(input(questions[i]+" Oui = 1, Non = 0 :")))

		elements.append(liste)

	
	return elements


def supprimerElement(elements):
	suppr = raw_input("Quel element voulez vous supprimer?").upper()
	for i in range (0,len(elements)):
		if (elements[i][0] == suppr):
			elements.remove(elements[i])
	return elements


def afficherElement(elements):
	for i in range (0,len(elements)):
		print(elements[i][0] + " ")

def lancerPartie(elements,questions):
	tri = elements

	for i in range (0,len(questions)):
		rep = int(input(questions[i]+" Oui = 1, Non = 0 :"))
		print("Reponse = "+str(rep))

		j = 0

		while (j<len(tri)):
			# print("Verification des elements : \t Question:"+str(i)+"\t Nom:"+tri[j][0]+
			# 		"\t valeur:"+str(tri[j][i+1]))
			
			if (tri[j][i+1] != rep):
				print("On supprime :"+ tri[j][0])
				tri.remove(tri[j])
			else:
				print("On garde :"+ tri[j][0])
				j=j+1
			

	print("\n--------- REPONSE : --------")
	for i in range (0,len(tri)):
		print(tri[i][0])


def main():

	baseElements = [["SOFIANE",1,1,0], ["CLEMENT",0,1,0],["CEDRIC",1,1,0],["PAUL",0,1,1],
					["THEO",1,1,1],["ANASTASIA",0,0,1],["HORTENSE",0,0,0]]
	baseQuestions = ["Genie informatique?","Garcon?","Blond?"]


	elements = list(baseElements)

	questions = list(baseQuestions)
	choix = 1


	while (choix != 5):
		print("Que voulez-vous faire ?")
		print("1 - Ajouter un element")
		print("2 - Supprimer un element")
		print("3 - Afficher les elements")
		print("4 - Lancer une partie!")
		print("5 - Quitter")
		choix = int(input("Quel est votre choix :"))
		print("\n")

		if (choix == 1):
			elements = ajoutElement(elements, questions)
		elif (choix == 2):
			elements = supprimerElement(elements)
		elif (choix == 3):
			afficherElement(elements)
		elif (choix == 4):
			lancerPartie(elements,questions)
			elements = list(baseElements)
			questions = list(baseQuestions)
			
		elif (choix != 5):
			print("Te fou pas de ma gueule !")

		print("\n")

	print("Fin du programme")

if __name__ == "__main__":
	main()
