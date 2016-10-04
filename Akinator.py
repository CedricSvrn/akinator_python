


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


# Main
def main():

	baseElements = [["THOMAS",1,1,0,0], ["ALEXIS",0,1,0,0],["CEDRIC",1,1,0,0],["FRED",1,1,0,1],
					["YVES",0,1,0,1],["ESTELLE",0,0,0,0],["MARIE",0,0,0,0],["JEREM",0,1,0,0]]
	baseQuestions = ["Computer Sciences Specialzed?","Boy?","Blond?","Have children?"]


	elements = list(baseElements)

	questions = list(baseQuestions)
	choice = 1


	while (choice != 5):
		print("What do you want to do ?")
		print("1 - Add an Element")
		print("2 - Delete an Element")
		print("3 - Print the Elements")
		print("4 - Start the Game !")
		print("5 - Quit")
		choice = int(input("What's your choice :"))
		print("\n")

		if (choice == 1):
			elements = addElement(elements, questions)
		elif (choice == 2):
			elements = deleteElement(elements)
		elif (choice == 3):
			printElement(elements)
		elif (choice == 4):
			startGame(elements,questions)
			elements = list(baseElements)
			questions = list(baseQuestions)
			
		elif (choice != 5):
			print("You're kidding me !")

		print("\n")

	print("End, Thank you !")
	print("By, Cedric Souverain.")

if __name__ == "__main__":
	main()
