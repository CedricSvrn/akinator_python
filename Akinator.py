import openpyxl
import unicodedata



# Function used to add an element
def addElement(elements, questions):
	l = [] #List of the new element
	exist = False #Boolean to know if the name already exists in the elements
	nom = raw_input("Enter a new element:").upper() #Name in capital letters
	l.append(nom) #Adding the name to the list

	for i in range (0,len(elements)): #Loop to check if the name already exists
		if (elements[i] == l[0]):
			print("This name already exists")
			exist = True

	if (not exist): #If it doesn't exists we ask the questions
		for i in range (0,len(questions)):
			l.append(int(input(questions[i]+" Yes = 1, No = 0 :")))

		elements.append(l) #We add the new element

	return elements #Return the elements with the new one


def addQuestions(elements,questions):
	exist = False

	questName = raw_input("Enter your question :").upper()

	for i in range (0,len(questions)):
		if (questions[i] == questName):
			print("This question already exists")
			exist = True

	if (not exist):
		questions.append(questName)
		print("Answer to this question for every Element :")

		for i in range(0,len(elements)):
			ans = int(input(elements[i][0]+", Yes = 1, No = 0 :"))
			elements[i].append(ans)

	return elements, questions





# Delete used to delete an element
def deleteElement(elements):
	name = raw_input("What is the name of the element you want to delete?").upper() #Ask the name of the element
	for i in range (0,len(elements)): #Searching the element
		if (elements[i][0] == name):
			elements.remove(elements[i]) #Remove

	return elements


# Print the name of all the elements
def printElement(elements):
	for i in range (0,len(elements)):
		print(elements[i][0] + " ")


# Start the game
def startGame(elements,questions):
	sort = elements #Creating a new variable to change its value

	for i in range (0,len(questions)): #Asking the questions
		ans = int(input(questions[i]+" Yes = 1, No = 0 :"))
		print("Answer = "+str(ans)) #Printing the answer

		j = 0

		while (j<len(sort)): #Loop to delete the element with a different answer
			
			if (sort[j][i+1] != ans): #If the answer is different
				print("Deleted :"+ sort[j][0])
				sort.remove(sort[j]) #Delete the element
			else: #Else we keep the element
				print("Kept :"+ sort[j][0])
				j=j+1
			

	print("\n--------- ANSWER : --------")
	for i in range (0,len(sort)):
		print(sort[i][0])

	if (len(sort) == 0):
		print("No Element found. You should create a new Element")
	elif (len(sort) > 1):
		print("You should create a new question to differentiate the Elements")


# Main
def main():

	#baseElements = [["THOMAS",1,1,0,0], ["ALEXIS",0,1,0,0],["CEDRIC",1,1,0,0],["FRED",1,1,0,1],
					#["YVES",0,1,0,1],["ESTELLE",0,0,0,0],["MARIE",0,0,0,0],["JEREM",0,1,0,0]]
	#baseQuestions = ["COMPUTER SCIENCES SPECIALIZED?","BOY?","BLOND?","HAVE CHILDREN?"]

	questionsRemaining = True
	nameRemaining = True
	i = 1
	j = 2
	letters = ["A","B","C","D","E","F","G","H"]
	baseElements = []
	baseQuestions = []

	doc = openpyxl.load_workbook('data.xlsx')
	sheet = doc.get_sheet_by_name('Sheet1')


	# GET THE DATA FROM XLSX
	while (questionsRemaining):
		case = letters[i]+"1"
		print(case)
		quest = sheet[case].value
		print(quest)
		i = i+1

		if (quest == None):
			print("End of the Database questions")
			questionsRemaining = False
		else:
			quest = unicodedata.normalize('NFKD', quest).encode('ascii','ignore') #Unicode to ASCII
			baseQuestions.append(quest)

	while (nameRemaining):

		case = "A"+str(j)
		print(case)
		nom = sheet[case].value
		print(nom)


		if (nom == None):
			print("End of the Database names")
			nameRemaining = False
		else:
			l = []
			nom = unicodedata.normalize('NFKD', nom).encode('ascii','ignore') #Unicode to ASCII
			l.append(nom)
			for i in range(1,len(baseQuestions)+1):
				val = sheet[letters[i]+str(j)].value
				#val = unicodedata.normalize('NFKD', val).encode('ascii','ignore') #Unicode to ASCII
				l.append(int(val))
			baseElements.append(l)

		j = j+1 #Next name
	
	print(baseElements)


	elements = list(baseElements)

	questions = list(baseQuestions)
	choice = 1


	while (choice != 6):
		print("What do you want to do ?")
		print("1 - Add an Element")
		print("2 - Delete an Element")
		print("3 - Print the Elements")
		print("4 - Add a question")
		print("5 - Start the Game !")
		print("6 - Quit")
		choice = int(input("What's your choice :"))
		print("\n")

		if (choice == 1):
			elements = addElement(elements, questions)
		elif (choice == 2):
			elements = deleteElement(elements)
		elif (choice == 3):
			printElement(elements)
		elif (choice == 4):
			elements, questions = addQuestions(elements,questions)
			print(elements)
			print(questions)
		elif (choice == 5):
			startGame(elements,questions)
			elements = list(baseElements)
			questions = list(baseQuestions)
			
		elif (choice != 6):
			print("You're kidding me !")

		print("\n")

	print("End, Thank you !")
	print("By, Cedric Souverain.")

if __name__ == "__main__":
	main()
