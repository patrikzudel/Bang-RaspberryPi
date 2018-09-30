# Bang!
Reflex based game for the RaspberryPi (GPIO)

To play one of the players needs to hold their button. 
The green LED will flash telling the players to get ready.
When the green LED flashes the second time players need to push the button as soon as they can.
After either of the players scored a point, the amount of points will be shown through the flashes of the green LED.
The point limit is 5 after which the game will return to the main menu.

You will need 
 - 2 red LEDs
 - 1 green LED
 - 2 Buttons
 
 Plug them into these GPIO pins:
- Player1 LED = 23
- Player1 Button = 18
- Green LED = 25
- Player2 LED = 12
- Player2 Button = 21
