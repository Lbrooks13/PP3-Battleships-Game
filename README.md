# MooD

In MooD, you are a space marine for the UaC (United Aerospace Corporation). You are based on Mars, providing security for the facility. You arrive for your look-out shift, when you hear screams coming from inside the base. An experiment has gone wrong and you are witnessing first hand what happens when man plays god. A portal to Hell has opened up in the base and demons are flooding the facility. It's time to lock and load and travel through the base.


## Gameplay

MooD is a text-based adventure recreation of the classic 1993 hit DooM from id software. The game will begin by taking your name, and then you are thrown into the game. Each area is described to you and you are presented a series of controls (directions) to determine where you go. There are secrets and weapons to find, enemy encounters and traps.

![Gameplay](https://i.ibb.co/KFLDPvv/input-Directions.png)

## Features

- Name Input - Here the player can input their name to add a more personal gameplay experience.

![Name input](https://i.ibb.co/jGsrGcS/name-Input.png)
- Controls - The game relies on text input for control. Each area is described to the player and then a list of directions the player can go is presented. This is then checked to ensure their input is valid with the room they are in.
- Secrets and weapons - Throughout the level there are 2 secret pickups to find, and a weapon. The weapon is essential for surviving a fight with an enemy.

![Secret A](https://i.ibb.co/F5F8sGL/secretA.png)

- End of Level Score - When the played finds the exit, the game will tally up how many secrets have been found and if the weapon is in the players possession. They will then have a completion percentage displayed.

![End of level](https://i.ibb.co/3WhtfyF/end-OFLevel.png)

- Exit Game - When allowed, and not caught in a trap, the game will display the exit direction to allow the player to quit to the main menu.
- Clear Screen - To prevent the excess build up of information on the screen, a function called clear screen is triggered up on each move into a new area. The user has no control over this function and is merely to prevent the terminal from flooding the user with information.

## Testing

- Validation Testing - All areas for user input must have validation to ensure only the required input can be considered before moving onto the next area.

All direction fields checked, PASS.

All user input fields checked, PASS.

![valid option](https://i.ibb.co/kHkdp2Z/secret-Validation.png)

![name input validation](https://i.ibb.co/gzNbxH4/input-Verify.png)

- End of Level Tally - All outcomes from acquiring Secret A, Secret B and the Weapon must be able to display at the end of level screen. Scenarios tested :

Weapon - True
Secret A - False
Secret B - False

Weapon - True
Secret A - True
Secret B - False

Weapon - True
Secret A - True
Secret B - True

Weapon - False
Secret A - True
Secret B - True

Weapon - False
Secret A - False
Secret B - True

Weapon - False
Secret A - False
Secret B - False

Weapon - False
Secret A - True
Secret B - False

Weapon - False
Secret A - False
Secret B - True

All scenarios, PASS.

![tally testing](https://i.ibb.co/3WhtfyF/end-OFLevel.png)

- Exit Game - When displayed in the directions, the exit function allows the player to exit the game. The exit direction will not always show, this is to prevent the player from skipping out of traps or deaths.

All occurrences checked, PASS.
- Enemy Encounter - The player will come across enemies whilst playing the game,  if the player has not discovered a weapon and they choose to fight the enemy then they lose and the game over screen is displayed.

Player death forced with fight command, PASS.

![game over validation](https://i.ibb.co/rGpwjtm/end-Of-Game.png)

- Secret Discovery - The player can come across 2 secrets in the level. To add a level of realism the secrets can only be discovered once. Once a secret is found the directions from the previous level will change and the user can no longer discover the secret. A message will appear telling the user they have already found this secret.

Function tested, PASS.

## Development
The map is inspired by level 1 of Doom - "Hangar". I initially recreated the level into rooms for me to base my code around. Once the rooms were created I could add the relevant dialogue into print statements describing each area.

![map](https://i.ibb.co/Mp50vps/Map.png)

Instead of using a traditional North, South, East, West control scheme, I opted for "tank" controls. Forward resulting in moving you forward from the way you entered the room and backward being used to back you out of a room.

### Imports
I have used the following Python packages and/or external imported packages.

- import os

This package is used to create the clear screen function used throughout the game.

- import time

This package is used to create a pause between terminal print outs. I felt that this added a certain level of suspense and theatrics into a game with a horror theme.

## Bugs

- Input Validation - The user could insert any character into the name input field. Bug fixed with isalpha() method on name input line.
- Direction Validation - The user had to use capital letters as the first character when typing directions in. Bug fixed with capitalize() method used on directions input line.

## Validator Testing

The program successfully passed through Python Linter with 0 warnings returned.
![Linter](https://i.ibb.co/6gknhS4/linter.png)

## Deployment

Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser. This is to improve the accessibility of the project to others.

The code is stored in the following repository on my [Github page.](https://github.com/Lbrooks13/PP3-MooD)
The app is deployed via Heroku. To run MooD in Heroku's cloud-based environment, please follow [this link.](https://mood-86e4a23b6660.herokuapp.com/)

## Credits
README generation created using [Stack Edit](stackedit.io).

Basic framework help courtesy of [Stack Overflow.](https://stackoverflow.com)

Imp character name used from DooM 1993 (id software).

A huge thank you to Tim Nelson for helping me with my code and for helping me with testing procedure and principles.
