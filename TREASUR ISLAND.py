print(''' ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
''')
print("WELCOME TO THE TREASURE ISLAND")
print("YOUR MISSION IS TO FIND THE TREASURE")
choice1 = input('YOU ARE AT A CROSSROAD WHERE DO YOU WANT TO GO? Type "right" or "left"\n').lower()

if choice1 == "left":
    choice2 = input('YOU HAVE GOT TO A LAKE. THERE IS AN ISLAND IN THE MIDDLE OF THE LAKE. Type "wait" to wait for a boat type "swim" to swim across\n').lower()
    if choice2 == "wait":
        choice3 = input('YOU ARRIVED AT THE ISLAND UNHARMED. THERE IS A HOUSE WITH THREE DOORS. ONE RED, ONE YELLOW ONE, ONE BLUE. WHICH COLOUR DO YOU CHOOSE?\n').lower()
        if choice3 == "YELLOW":
            print("ITS A ROOM FULL OF FIRE. GAME OVER")
        elif choice3 == "RED":
            print("YOU FOUND THE TREASURE YOU WIN")
        elif choice3 == "BLUE":
            print("YOU ENTERED A ROOM FULL OF BEASTS. GAME OVER")
        else:
            print("YOU CHOSE A DOOR THAT DOES NOT EXIST. GAME OVER")

    else:
        print("YOU GOT ATTACKED BY AN ANGRY ALLIGATOR. GAME OVER")
else:
    print("YOU FELL INTO A HOLE. GAME OVER")


