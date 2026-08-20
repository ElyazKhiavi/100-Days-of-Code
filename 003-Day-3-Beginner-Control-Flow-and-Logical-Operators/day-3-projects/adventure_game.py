# Adventure Game

# visit https://ascii.co.uk/art for more ascii art 😎
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
    ''')
print("🌟 Welcome, brave adventurer, to the legendary Treasure Island!")
print("⚔️ Your mission: find the fabled treasure that no one has ever claimed.\n")

cross_road = input(
    "🌲 You stand at a dusty crossroads. A chilling breeze whispers through the pines.\n"
    "To your left, a shadowy forest stirs. To your right, a cliff path crumbles into the sea.\n"
    "Where will you go? Type 'left' or 'right'.\n"
)

if cross_road.lower() == "left":
    island = input(
        "🌊 You push through the underbrush and emerge at a serene, mist‑covered lake.\n"
        "An emerald island glimmers in the centre, wreathed in ancient vines.\n"
        "A rickety rowboat rocks at the water's edge, but no one is aboard.\n"
        "Do you wait for a ghostly ferryman, or swim across the dark waters?\n"
        "Type \"wait\" to wait for a boat, or \"swim\" to brave the depths.\n"
    )
    if island.lower() == "wait":
        door = input(
            "🛶 A cloaked figure silently rows you to the island. You step onto the shore, heart pounding.\n"
            "Before you looms a weathered manor, its windows like hollow eyes.\n"
            "Three doors stand before you: a fiery 🟥 RED, a sunlit 🟨 YELLOW, and an icy 🟦 BLUE.\n"
            "Which colour will you choose? Type 'red', 'yellow', or 'blue'.\n"
        )
        if door.lower() == "red":
            print("🔥 The door swings open and a torrent of dragon’s breath engulfs you!")
            print("💀 You are consumed by flames. Game Over.")
        elif door.lower() == "blue":
            print("🐾 The door creaks open, and a pack of ravenous wolves lunges from the shadows!")
            print("💀 You are torn apart. Game Over.")
        elif door.lower() == 'yellow':
            print("✨ You turn the golden handle and the door swings wide.")
            print("🏆 The room glitters with piles of gold, jewels, and ancient artefacts!")
            print("🎉 YOU WIN! The treasure is yours. Congratulations!")
        else:
            print("🚪 You hesitate... the door dissolves into mist and you fall into a void.")
            print("💀 Game Over.")
    else:
        print("🐟 You dive into the lake, but the water churns with razor‑toothed trout!")
        print("💢 They swarm you before you can reach the island. Game Over.")
else:
    print("🕳️ You take a step onto the crumbling cliff path – the ground gives way beneath you.")
    print("💀 You tumble into a bottomless pit. Game Over.")