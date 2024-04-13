# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def intro():
  directions = ['Left', 'Forward','Right']
  print("You are stood in a large open area. It is dimly lit, with rusted walls. They are splattered in blood, the remains of your former regiment are scattered across the floor.")
  userInput = ""
  while userInput not in directions:
    print("Options: left/right/backward/forward")
    userInput = input()
    if userInput() == "Left":
      Stairs()
    elif userInput == "Right":
      Courtyard()
    elif userInput == "Forward":
      enemyRoom()
    elif userInput == "Backward":
      print("You can't chicken out now, Marine.")
    else :
      print("Please enter a valid direction")







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

    #Intro Scene

#Stairs Scene
  def stairs():
    directions = ['Forward', 'Backward', 'Right']
    #error
