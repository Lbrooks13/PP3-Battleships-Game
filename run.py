
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# -- Variables --

userInput = input()
validOption = "Please Enter A Valid Option"
Secret_1 = False
Secret_2 = False
Weapon = False

# -- Levels --
# Main Hall
def intro():
  directions = ['Left', 'Forward','Right']
  print("You are stood in a large open area. It is dimly lit, with rusted walls. They are splattered in blood, the remains of your former regiment are scattered across the floor.")
  userInput = ""
  while userInput not in directions:
    print("Options: left/right/backward/forward")
  #userinput = input() ? Liam - Check this
    if userInput() == "Left":
      Stairs()
    elif userInput == "Right":
      Courtyard()
    elif userInput == "Forward":
      Enemy_room()
    elif userInput == "Backward":
      print("You can't chicken out now, Marine.")
    else :
      print(validOption())

#Stairs
def Stairs():
  directions = ['Forward', 'Backward', 'Right']
  print("You are stood at the foot of a large staircase. At the top you see a window. Beyond it, there is nothing but the harsh red wasteland of Mars.") 
  print("You wonder how on earth you're ever going to get home from this hell.")
  userInput = ""
  while userInput not in directions: 
    print("Options: right/backward/forward")
    if userInput == "Right":
      Secret_A ()
    elif userInput == "Backward":
      print("You are travelling towards the Main Hall")
      intro()
    elif userInput == "Forward":
      Weapon_room()
    else :
      print(validOption())  

#Secret A
def Secret_A():
  directions = ['Backward']
  global Secret_1
  print("You find a skull shaped switch to the side of the stairs")
  print("You push the switch, its eyes glow red and a section of the wall lifts up")
  print("Infront of you there is a box of shotgun cartridges")
  print("You place them in your pocket and suddenly, Mars doesn't seem like such a bad place after all...")
  userInput = ""
  while userInput not in directions:
    print("Options: backward")
    if userInput == "Backward":
      print("You step out and the skull switch returns to its normal state")
      Stairs()
  else:
    print(validOption())

#Weapon Room
def Weapon_room():
  directions = ['Backward']
  global Weapon
  print("You climb the stairs to find a mezanine, in the center there is a platform. Floating in the middle is a sight that brings a tear to your eye.")
  print("Glistening in the red glow of the Martian landscape is a 12 bore double-barrelled shotgun.")
  print("You pick up the shotgun and for reasons unknown to man or God, a sinister grin creeps across your face")
  print("You close your eyes for a moment and hear the words 'Rip and Tear' echo through your mind")
  print("'What a time to be alive' you think to yourself as you exhale and load the shotgun 'malisciously'")
  userInput = ""
  while userInput not in directions: 
    print("Options: backward")
    if userInput == "Backward":
      print("You walk down the stairs and are now at the foot of the stairs. Time to head into the base...")
      Stairs()
  else: 
    print(validOption())

#Enemy Room
def Enemy_room():
  directions = ['Forward', 'Backward', 'Right']
  print("You walk up to a giant steel door with a red button in the middle")
  print("You push the button and the whole door raises with a 'whoosh' sound")
  print("You are stood in a corridoor that snakes around to the right, beyond the doors to your right and infront of you, you can hear all manner of demons awaiting your arrival")
  userInput = ""
  while userInput not in directions:
    print("Options: forward/right/backward")
    if userInput == "Backward":
      print("You turn around and go back through the giant steel door. You are now travelling towards the Main Hall")
      intro()
    elif userInput == "Forward":
      print("You walk towards the door infront of you. You can hear footsteps beyond the door. They sound like marching boots on a metal floor.")
      print("Could it be your team? Are they still alive?")
      Soldier_room()
    elif userInput == "Right":
      print("You walk towards another giant steel door on your right. You go to press the button to open it, but as you do you hear the dintinct sound of flesh being tore from bone")
      print("A snarl is the only clue of what awaits behind the door. But whatever it is, it doesnt sound like anything born of Earth...")
      Imp_room()
  else :
    print(validOption())

#Soldier Room
def Soldier_room():
  directions =['Fight', 'Run']
  print("You open the door to find a room with 2 marines inside. However, something isnt right...")
  print("They're your former unit, but they look possesed. Their eyes red and sunken in, the flesh rotting from their bones, their mouths dripping with blood")
  userInput = ""
  while userInput not in directions:
    print("Options: fight/run")
    if userInput == "Fight":
      if Weapon:
        print("You pull the shotgun from you back, drop a cartridge in each barrel and unleash hell upon your former team-mates")
        print("After blowing a hole clean through the first soliders chest, you reload.")
        print("You run towards the second marine, shoving the end of the barrel in his snarling mouth. You squeeze the trigger and redecorate the east wall with whats left of his brains")
        print("Satisfied with your kills, you head back towards the square room. Let's find out whats behind door number 2...")
        Enemy_room()
      else :
        print("You rookie. You went and brought a knife to a gun fight.")
        print("The soldiers charge at you and begin dismembering you whilst you're still alive...")
        print("It's dangerous to go alone, you should have found a weapon...")
        print("YOU HAVE DIED")
        title()
    elif userInput == "Run":
      print("You know when you're out-gunned. Maybe you should arm yourself before taking these guys on.")
      Enemy_room()
    else :
      print(validOption())

#Imp Room -- NOT FINISHED
def Imp_room():
  directions = ['Forward', 'Backward', 'Right', 'Left']
  print)


#Secret B
def secret_B():
  directions = ['Backward']
  global Secret_2
  userInput = ""
  while userInput not in directions:
    print("You find a skull shaped switch on the wall. You press the skull and it's eyes glow red.")
    print("The area of wall to your left raises up revealing a secret area.")
    print("Inside you find a Medikit")
    print("The wall closes and the skull reverts back to normal")
    print("Options: backward")
    if userInput == "Backward":
      print("You turn around to face the tall room.")
      Imp_room()
    else:
      print(validOption())



#Poison Room
def Poison_room():
    print("You open the door to find a pitch black room.")
    print("You step out and fall into a poison filled void.")
    print("You look up in desperation but see no way out. The fumes and toxins envelop you.")
    print("You let out a final gasp as death takes its hold on you")
    print("YOU HAVE DIED")
    title()


#Courtyard
def Courtyard():
  print("You gaze out through the window to an open area. The red sun beaming down onto the harsh Martian landscape.")
  print("The whole area is filled with demons... Maybe you'd better sit this one out until you can find more substantial weaponry")
  intro()

#Exit
def Exit():
  print("Hangar : Finished")
  if Weapon == True :
    print("You found the shotgun.")
  elif Secret_1 == True :
    print("You found Secret A.")
  elif Secret_2 == True :
    print("You found Secret B.")
  else :
    print ("You didnt find any secrets or weapons. Back to basic training for you, Marine...")
  print("Thank you for playing MooD!")
  print("Redirecting to Main Menu...")
  title()          

# -- Title Card -- 
# Intro Scene
def title():
  if __name__ == "__main__":
    while True:
      print("Welcome to MooD")
      print("You are a space marine, stranded on Mars.")
      print("From behind a huge door you hear snarling and the cries of your former marine comrades being devoured by demons.")
      print("You must maneuver through the Mars base to find safety.")
      print("You can choose to walk in multiple directions to find a way out.")
      print("Let's start with your callsign: ")
      callsign = input()
      print("Good luck, " +callsign+ ".")
      print("Entering: 'The Hangar'...")
      print("For a truly immersive experience please follow this link 'https://www.youtube.com/watch?v=MEYxYcLi1lc' ")
      intro()