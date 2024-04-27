import os
import time

# -- Variables --
continue_game = "Press Enter to continue"
valid_option = "Please Enter A Valid Option"
global SECRET_1
global SECRET_2
global WEAPON

# -- Functions --
#Clear terminal
def clear_terminal() :
  os.system('cls')

# -- Levels -- 
# Main Hall
def intro():
  clear_terminal()
  directions = ['Left', 'Forward','Right']
  print("You are stood in a large open area.")
  time.sleep(0.2)
  print("It is dimly lit, with rusted walls.") 
  time.sleep(0.2)
  print(
    "They are splattered in blood, "
    "the remains of your former regiment are scattered across the floor."
  )
  time.sleep(0.2)
  print("To your left you see a large staircase.")
  time.sleep(0.2)
  print("To your right you see a window over-looking a courtyard.")
  time.sleep(0.2)
  print("Behind you is the door you used to enter the facility.")
  time.sleep(0.2)
  print("Infront of you is a giant door made of steel.")
  time.sleep(0.2)
  user_input = ""
  while user_input.capitalize() not in directions:
    print("Options: left/right/backward/forward")
    user_input = input("Make your selection: ")
    if user_input.capitalize() == "Left":
      Stairs()
    elif user_input.capitalize() == "Right":
      Courtyard()
    elif user_input.capitalize() == "Forward":
      Enemy_room()
    elif user_input.capitalize() == "Backward":
      print("You can't chicken out now, Marine.")
    else :
      print(valid_option)

#Stairs
def Stairs():
  clear_terminal()
  directions = ['Forward', 'Backward', 'Right']
  print("You are stood at the foot of a large staircase. At the top you see a window. Beyond it, there is nothing but the harsh red wasteland of Mars.") 
  print("You wonder how on earth you're ever going to get home from this hell.")
  print("To your right there is hidden alcove next to the stairs.")
  print("Behind you is the door back to the main hall.")
  print("Infront of you is the staircase.")
  user_input = ""
  while user_input.capitalize() not in directions: 
    print("Options: right/backward/forward")
    user_input = input("Make your selection: ")
    if user_input.capitalize() == "Right":
      Secret_A()
    elif user_input.capitalize() == "Backward":
      print("You are travelling towards the Main Hall")
      input(continue_game)
      intro()
    elif user_input.capitalize() == "Forward":
      weapon_room()
    else :
      print(valid_option)  

#Secret A
def Secret_A():
  clear_terminal()
  directions = ['Backward']
  global SECRET_1
  SECRET_1 = True
  print("You find a skull shaped switch to the side of the stairs")
  print("You push the switch, its eyes glow red and a section of the wall lifts up")
  print("Infront of you there is a box of shotgun cartridges")
  print("You place them in your pocket and suddenly, Mars doesn't seem like such a bad place after all...")
  user_input = ""
  while user_input.capitalize() not in directions:
    print("Options: backward")
    user_input = input("Make your selection: ")
    if user_input.capitalize() == "Backward":
      print("You step back and the skull switch returns to its normal state")
      input(continue_game)
      Stairs()
    else:
      print(valid_option)

#Weapon Room
def weapon_room():
  clear_terminal()
  directions = ['Backward']
  global WEAPON
  WEAPON = True
  print("You climb the stairs to find a mezanine, in the center there is a platform. Floating in the middle is a sight that brings a tear to your eye.")
  print("Glistening in the red glow of the Martian landscape is a 12 bore double-barrelled shotgun.")
  print("You pick up the shotgun and for reasons unknown to man or God, a sinister grin creeps across your face")
  print("You close your eyes for a moment and hear the words 'Rip and Tear' echo through your mind")
  print("'What a time to be alive' you think to yourself as you exhale and load the shotgun 'malisciously'")
  print("Behind you is the staircase.")
  user_input = ""
  while user_input.capitalize() not in directions: 
    print("Options: backward")
    user_input = input("Make your selection: ")
    if user_input.capitalize() == "Backward":
      print("You walk down the stairs and are now at the foot of the stairs. Time to head into the base...")
      input(continue_game)
      Stairs()
    else: 
      print(valid_option)

#Enemy Room
def Enemy_room():
  clear_terminal()
  directions = ['Forward', 'Backward', 'Right']
  print("You walk up to a giant steel door with a red button in the middle")
  print("You push the button and the whole door raises with a 'whoosh' sound")
  print("You are stood in a corridoor that snakes around to the right, beyond the doors to your right and infront of you, you can hear all manner of demons awaiting your arrival")
  print("Infront of you is a door.")
  print("To your right is a corridor leading towards another giant steel door.")
  print("Behind you is the giant steel door heading back to the main hall.")
  user_input = ""
  while user_input.capitalize() not in directions:
    print("Options: forward/right/backward")
    user_input = input("Make your selection: ")
    if user_input.capitalize() == "Backward":
      print("You turn around and go back through the giant steel door. You are now travelling towards the Main Hall")
      input(continue_game)
      intro()
    elif user_input.capitalize() == "Forward":
      print("You walk towards the door infront of you. You can hear footsteps beyond the door. They sound like marching boots on a metal floor.")
      print("Could it be your team? Are they still alive?")
      input(continue_game)
      Soldier_room()
    elif user_input.capitalize() == "Right":
      print("You walk towards another giant steel door on your right. You go to press the button to open it, but as you do you hear the dintinct sound of flesh being tore from bone")
      print("A snarl is the only clue of what awaits behind the door. But whatever it is, it doesnt sound like anything born of Earth...")
      input(continue_game)
      Imp_room()
    else :
      print(valid_option)

# Soldier Room
def Soldier_room():
  global WEAPON
  clear_terminal()
  directions =['Fight', 'Run']
  print("You open the door to find a room with 2 marines inside. However, something isnt right...")
  print("They're your former unit, but they look possesed. Their eyes red and sunken in, the flesh rotting from their bones, their mouths dripping with blood")
  user_input = ""
  while user_input.capitalize() not in directions:
    print("Options: fight/run")
    user_input = input("Make your selection: ")
    if user_input.capitalize() == "Fight":
      if WEAPON:  # Liam - Remember this, 2 spaces before 1 after
        print("You pull the shotgun from you back, drop a cartridge in each barrel and unleash hell upon your former team-mates")
        print("After blowing a hole clean through the first soliders chest, you reload.")
        print("You run towards the second marine, shoving the end of the barrel in his snarling mouth. You squeeze the trigger and redecorate the east wall with whats left of his brains")
        print("Satisfied with your kills, you head back towards the square room. Let's find out whats behind door number 2...")
        input(continue_game)
        Enemy_room()
      else :
        print("You rookie. You went and brought a knife to a gun fight.")
        print("The soldiers charge at you and begin dismembering you whilst you're still alive...")
        print("It's dangerous to go alone, you should have found a weapon...")
        print("YOU HAVE DIED")
        input(continue_game)
        start()
    elif user_input.capitalize() == "Run":
      print("You know when you're out-gunned. Maybe you should arm yourself before taking these guys on.")
      input(continue_game)
      Enemy_room()
    else :
      print(valid_option)

#Imp Room
def Imp_room():
  clear_terminal()
  directions = ['Forward', 'Backward', 'Right', 'Left']
  print("The giant door raises up. You are now stood in a tall room.")
  print("Above you there is a window overlooking the area. You can just make-out something wandering aimlessly through the room")
  print("Is it human?")
  print("Infront of you is a small door with a yellow sign on the door. 'BIOLOGICAL HAZZARD : BEWARE'.")
  print("To your left is a skull shaped switch on the door.")
  print ("To your right is a small door. A red EXIT sign is hung above.")
  print("Behind you is the door back to the previous room.")
  user_input = ""
  while user_input.capitalize() not in directions:
    print("Options : forward/backward/left/right")
    user_input = input("Make your selection: ")
    if user_input.capitalize() == "Forward":
      print("You walk up to the biohazard door. There is a small green button to your right. You press it and the door slides open.")
      input(continue_game)
      Poison_room()
    elif user_input.capitalize() == "Left":
      print("You turn to face the skull shaped switch.")
      input(continue_game)
      secret_B()
    elif user_input.capitalize() == "Right":
      print("You walk past a large drum of radioactive waste. This door must lead to the Nuclear Plant...")
      input(continue_game)
      Exit()
    elif user_input.capitalize() == "Backward":
      print("You turn around and head back towards the previous room.")
      input(continue_game)
      Enemy_room()
    else :
      print(valid_option)    

#Secret B
def secret_B():
  clear_terminal()
  directions = ['Backward']
  global SECRET_2
  SECRET_2 = True
  print("You press the skull and it's eyes glow red. You a hear a 'THUNK' from behind the switch.")
  print("The area of wall to your left raises up revealing a secret area.")
  print("Inside you find a Medikit.")
  print("The wall closes and the skull reverts back to normal.")
  print("Options: backward")
  user_input = ""
  while user_input.capitalize() not in directions:
    user_input = input("Make your selection: ")
    if user_input.capitalize() == "Backward":
      print("You turn around to face the tall room.")
      input(continue_game)
      Imp_room()
    else:
      print(valid_option)

#Poison Room
def Poison_room():
  clear_terminal()
  print("The door opens to reveal a pitch black room.")
  print("You step out and fall into a poison filled void.")
  print("You look up in desperation but see no way out. The fumes and toxins envelop you.")
  print("You let out a final gasp as death takes its hold on you.")
  print("YOU HAVE DIED")
  input(continue_game)
  start()

#Courtyard
def Courtyard():
  clear_terminal()
  print("You gaze out through the window to an open area. The red sun beaming down onto the harsh Martian landscape.")
  print("The whole area is filled with demons... Maybe you'd better sit this one out until you can find more substantial weaponry.")
  input(continue_game)
  intro()

# Exit
def Exit():
  global WEAPON
  global SECRET_1
  global SECRET_2
  clear_terminal()
  print("Hangar : Finished")
  if WEAPON:
    print("You found the Shotgun.")
  else:
    print("You didnt find any weapons.")
  if SECRET_1 and SECRET_2:
    print("Secrets : 100%")
  elif SECRET_1 or SECRET_2:  
    print("Secrets : 50%")
  else:
    print("Secrets : 0%")
    print ("You didnt find any secrets.")
  if not WEAPON and not SECRET_1 and not SECRET_2:
    print("Back to basic training for you marine.....")
  time.sleep(2) 
  print("Entering : Nuclear Plant...")
  time.sleep(2)
  print("ERROR : 404 'Liam hasn't bothered making anymore levels'")
  print("Thank you for playing MooD!")
  print("Redirecting to Main Menu")
   # TODO: Add timing to period on print
  #  ...")
  input(continue_game)
  start()          

# -- Title Card -- 
# Intro Scene
def start():
  global WEAPON
  global SECRET_1
  global SECRET_2
  WEAPON = False
  SECRET_1 = False
  SECRET_2 = False
  clear_terminal()
  print("Welcome to MooD")
  print("You are a space marine, stranded on Mars.")
  print("From behind a huge door you hear snarling and the cries of your former marine comrades being devoured by demons.")
  print("You must maneuver through the Mars base to find safety.")
  print("You can choose to walk in multiple directions to find a way out.")
  callsign = input("Let's start with your callsign: ")
  print("Good luck, " +callsign+ ".")
  print("Entering: 'The Hangar'...")
  print("For a truly immersive experience please open this link in your web browser whilst playing the game 'https://www.youtube.com/watch?v=MEYxYcLi1lc' ")
  input(continue_game)
  intro()

start()