
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# -- Variables --
import os


validOption = "Please Enter A Valid Option"
Secret_1 = False
Secret_2 = False
Weapon = False


def Clear_terminal() :
  os.system('cls')

# Main Hall
def intro():
  Clear_terminal()
  directions = ['Left', 'Forward','Right']
  print("You are stood in a large open area. It is dimly lit, with rusted walls. They are splattered in blood, the remains of your former regiment are scattered across the floor.")
  userInput = ""
  while userInput.capitalize() not in directions:
    print("Options: left/right/backward/forward")
    userInput = input("Make your selection: ")
    if userInput.capitalize() == "Left":
      Stairs()
    elif userInput.capitalize() == "Right":
      Courtyard()
    elif userInput.capitalize() == "Forward":
      Enemy_room()
    elif userInput.capitalize() == "Backward":
      print("You can't chicken out now, Marine.")
    else :
      print(validOption)





# -- Levels --


#Stairs
def Stairs():
  Clear_terminal()
  directions = ['Forward', 'Backward', 'Right']
  print("You are stood at the foot of a large staircase. At the top you see a window. Beyond it, there is nothing but the harsh red wasteland of Mars.") 
  print("You wonder how on earth you're ever going to get home from this hell.")
  userInput = ""
  while userInput.capitalize() not in directions: 
    print("Options: right/backward/forward")
    userInput = input("Make your selection: ")
    if userInput.capitalize() == "Right":
      Secret_A()
    elif userInput.capitalize() == "Backward":
      print("You are travelling towards the Main Hall")
      intro()
    elif userInput.capitalize() == "Forward":
      Weapon_room()
    else :
      print(validOption)  

#Secret A
def Secret_A():
  Clear_terminal()
  directions = ['Backward']
  global Secret_1
  Secret_1 = True
  print("You find a skull shaped switch to the side of the stairs")
  print("You push the switch, its eyes glow red and a section of the wall lifts up")
  print("Infront of you there is a box of shotgun cartridges")
  print("You place them in your pocket and suddenly, Mars doesn't seem like such a bad place after all...")
  userInput = ""
  while userInput.capitalize() not in directions:
    print("Options: backward")
    userInput = input("Make your selection: ")
    if userInput.capitalize() == "Backward":
      print("You step out and the skull switch returns to its normal state")
      Stairs()
    else:
      print(validOption)

#Weapon Room
def Weapon_room():
  Clear_terminal()
  directions = ['Backward']
  global Weapon
  Weapon = True
  print("You climb the stairs to find a mezanine, in the center there is a platform. Floating in the middle is a sight that brings a tear to your eye.")
  print("Glistening in the red glow of the Martian landscape is a 12 bore double-barrelled shotgun.")
  print("You pick up the shotgun and for reasons unknown to man or God, a sinister grin creeps across your face")
  print("You close your eyes for a moment and hear the words 'Rip and Tear' echo through your mind")
  print("'What a time to be alive' you think to yourself as you exhale and load the shotgun 'malisciously'")
  userInput = ""
  while userInput.capitalize() not in directions: 
    print("Options: backward")
    userInput = input("Make your selection: ")
    if userInput.capitalize() == "Backward":
      print("You walk down the stairs and are now at the foot of the stairs. Time to head into the base...")
      Stairs()
    else: 
      print(validOption)

#Enemy Room
def Enemy_room():
  Clear_terminal()
  directions = ['Forward', 'Backward', 'Right']
  print("You walk up to a giant steel door with a red button in the middle")
  print("You push the button and the whole door raises with a 'whoosh' sound")
  print("You are stood in a corridoor that snakes around to the right, beyond the doors to your right and infront of you, you can hear all manner of demons awaiting your arrival")
  userInput = ""
  while userInput.capitalize() not in directions:
    print("Options: forward/right/backward")
    userInput = input("Make your selection: ")
    if userInput.capitalize() == "Backward":
      print("You turn around and go back through the giant steel door. You are now travelling towards the Main Hall")
      intro()
    elif userInput.capitalize() == "Forward":
      print("You walk towards the door infront of you. You can hear footsteps beyond the door. They sound like marching boots on a metal floor.")
      print("Could it be your team? Are they still alive?")
      Soldier_room()
    elif userInput.capitalize() == "Right":
      print("You walk towards another giant steel door on your right. You go to press the button to open it, but as you do you hear the dintinct sound of flesh being tore from bone")
      print("A snarl is the only clue of what awaits behind the door. But whatever it is, it doesnt sound like anything born of Earth...")
      Imp_room()
    else :
      print(validOption)

#Soldier Room
def Soldier_room():
  Clear_terminal()
  directions =['Fight', 'Run']
  print("You open the door to find a room with 2 marines inside. However, something isnt right...")
  print("They're your former unit, but they look possesed. Their eyes red and sunken in, the flesh rotting from their bones, their mouths dripping with blood")
  userInput = ""
  while userInput.capitalize() not in directions:
    print("Options: fight/run")
    userInput = input("Make your selection: ")
    if userInput.capitalize() == "Fight":
      if Weapon == True:
        print("You pull the shotgun from you back, drop a cartridge in each barrel and unleash hell upon your former team-mates")
        print("After blowing a hole clean through the first soliders chest, you reload.")
        print("You run towards the second marine, shoving the end of the barrel in his snarling mouth. You squeeze the trigger and redecorate the east wall with whats left of his brains")
        print("Satisfied with your kills, you head back towards the square room. Let's find out whats behind door number 2...")
        input("Press enter to continue")
        Enemy_room()
      else :
        print("You rookie. You went and brought a knife to a gun fight.")
        print("The soldiers charge at you and begin dismembering you whilst you're still alive...")
        print("It's dangerous to go alone, you should have found a weapon...")
        print("YOU HAVE DIED")
        input("Press Enter to continue")
        start()
    elif userInput.capitalize() == "Run":
      print("You know when you're out-gunned. Maybe you should arm yourself before taking these guys on.")
      input("Press Enter to continue")
      Enemy_room()
    else :
      print(validOption)

#Imp Room -- NOT FINISHED
def Imp_room():
  Clear_terminal()
  directions = ['Forward', 'Backward', 'Right', 'Left']


#Secret B
def secret_B():
  Clear_terminal()
  directions = ['Backward']
  global Secret_2
  Secret_2 = True
  print("You find a skull shaped switch on the wall. You press the skull and it's eyes glow red.")
  print("The area of wall to your left raises up revealing a secret area.")
  print("Inside you find a Medikit")
  print("The wall closes and the skull reverts back to normal")
  print("Options: backward")
  userInput = ""
  while userInput.capitalize() not in directions:
    userInput = input("Make your selection: ")
    if userInput.capitalize() == "Backward":
      print("You turn around to face the tall room.")
      Imp_room()
    else:
      print(validOption)



#Poison Room
def Poison_room():
  Clear_terminal()
  print("You open the door to find a pitch black room.")
  print("You step out and fall into a poison filled void.")
  print("You look up in desperation but see no way out. The fumes and toxins envelop you.")
  print("You let out a final gasp as death takes its hold on you")
  print("YOU HAVE DIED")
  start()


#Courtyard
def Courtyard():
  Clear_terminal()
  print("You gaze out through the window to an open area. The red sun beaming down onto the harsh Martian landscape.")
  print("The whole area is filled with demons... Maybe you'd better sit this one out until you can find more substantial weaponry")
  intro()

#Exit
def Exit():
  Clear_terminal()
  print("Hangar : Finished")
  if Weapon == True :
    print("You found the shotgun.")
    print("Kills : 100%")
  elif Secret_1 == True :
    print("You found Secret A.")
    print("Secrets : 50%")
  elif Secret_2 == True :
    print("You found Secret B.")
    print("Secrets : 100%")
  else :
    print("Kills : 0%")
    print("Secrets : 0%")
    print ("You didnt find any secrets or weapons. Back to basic training for you, Marine...")
  print("Entering : Nuclear Plant...")
  print("ERROR : 404 'Liam hasn't bothered making anymore levels'")
  print("Thank you for playing MooD!")
  print("Redirecting to Main Menu...")
  input("Press Enter to continue")
  start()          

# -- Title Card -- 
# Intro Scene

def start():
  Clear_terminal()
  print("Welcome to MooD")
  print("You are a space marine, stranded on Mars.")
  print("From behind a huge door you hear snarling and the cries of your former marine comrades being devoured by demons.")
  print("You must maneuver through the Mars base to find safety.")
  print("You can choose to walk in multiple directions to find a way out.")
  callsign = input("Let's start with your callsign: ")
  print("Good luck, " +callsign+ ".")
  print("Entering: 'The Hangar'...")
  print("For a truly immersive experience please follow this link 'https://www.youtube.com/watch?v=MEYxYcLi1lc' ")
  input("Press Enter to continue")
  intro()

start()