#This is a template for the python story
def begin_story():
	user_response = 0
	print("You walk into an abandoned hospital and can't see anything, what do you do?")
	user_response = int(input("1.You turn on the flashlght on your phone to help you see.\n2.You explore in the dark to avoid anyone outside catching you.\n3.You leave."))
	decision1(user_response)
	
def decision1(user_response):
	if user_response == 1:
		print("You notice someone walking around outside.What do you do next?")
		user_response = int(input("1.Head towards the door to see who it is.\n2.Hide.\n3.Walk towards the window to see who it is."))
		decision2_1(user_response)
	elif user_response == 2:
		print("You bump into a table and make a loud noise.What do you do next?")
		user_response = int(input("1.You keep the light off and stand up.\n2.You keep the light on and stand up.\n3.Try to crouch and hide"))
		decision2_2(user_response)
	elif user_response == 3:
		print("User selected 3. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
		decision2_3(user_response)
	
def decision2_1(user_response):
	print("This would be the story continuing after the user's second response")
	if user_response == 1:
		print("User selected 1. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
	elif user_response == 2:
		print("User selected 2. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
	elif user_response == 3:
		print("User selected 3. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))

def decision2_2(user_response):
	print("This would be the story continuing after the user's second response")
	if user_response == 1:
		print("User selected 1. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
	elif user_response == 2:
		print("User selected 2. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
	elif user_response == 3:
		print("User selected 3. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))

def decision2_3(user_response):
	print("This would be the story continuing after the user's second response")
	if user_response == 1:
		print("User selected 1. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
		decision3_1(user_response)
	elif user_response == 2:
		print("User selected 2. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
		decision3_2(user_response)
	elif user_response == 3:
		print("User selected 3. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
		decision3_3(user_response)
		
def decision3_1(user_response):
  print("This would be the story continuing after the user's third response")
  if user_response == 1:
    print("User selected 1. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_1(user_response)
  elif user_response == 2:
    print("User selected 2. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_2(user_response)
  elif user_response == 3:
    print("User selected 3. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_3(user_response)

def decision3_2(user_response):
  print("This would be the story continuing after the user's third response")
  if user_response == 1:
    print("User selected 1. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_1(user_response)
  elif user_response == 2:
    print("User selected 2. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_2(user_response)
  elif user_response == 3:
    print("User selected 3. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_3(user_response)
    
def decision3_3(user_response):
  print("This would be the story continuing after the user's third response")
  if user_response == 1:
    print("User selected 1. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_1(user_response)
  elif user_response == 2:
    print("User selected 2. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_2(user_response)
  elif user_response == 3:
    print("User selected 3. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_3(user_response)
	
#This runs the game
user_name = input("Enter your name")
begin_story()
