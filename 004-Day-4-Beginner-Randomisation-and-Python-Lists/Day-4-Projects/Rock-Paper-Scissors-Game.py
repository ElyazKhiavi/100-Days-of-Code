from random import choice

#  Rock Paper Scissors Game

# Rock Paper Scissors ASCII Art

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
print("""
                                                8800000008                                          
                                          88 80GGCLfft111tfC08                                      
                                           80GGGCf1i;:,,,,,:itC8    8                               
                                          0GG0Gf1;:,..    ...,;t0                                   
                                         8CCCL1;:,.          .,,f0                                  
                                        8GCLf1;,.     .....   .,:L                                  
                                        8CLLti:. .   .,,,::.  ..,t8                                 
                                        8LLCCf;.    .;f00Ct:.  ..t0                                 
                                        8LG0CLL;   .10GtL00t, ...t0                                 
                                    8   8LGC;.f1. .;fL;..t0t,  ..t0                                 
                                        8fffi,1ti1i1ti,.iLG;. ...t0                                 
                                        8t;1CfLLLLfffft1LCt,. ...1G                                 
                                        8ttCGGGCLLLffffLLft1,....;L     8                           
                                        811tLCCCLLLLLfft1;;;,.::,,10  8                             
                                       8Gi,;tttttt111i;;:;1:.,i1;::10                               
                                       0f:,1Gfi;;::::;;;itLt,,ifti::t0                              
                                 8  8 0L;.:L8GLti;;;ii11fLGGi.,;i;:::1G8                            
                                 88  0Li,.t080GGLfftttfLCCG0Gi .,,,,::iL8      8                    
                                 88 0fi:.1G80000GGCLLLLGGG08 C;  ....,:;t0  8   8                   
                                   0t;,.i088888000GGGGG0000888G;. .  .,::iC8                        
                                  0t;,,i08888888800800800880888Gi,......,:if0                       
                          8  88  Gt;..t0888888888888888888888888Gi,,,.  .,:;t0   8                  
                               8Ct:.:L08 88         8888888880008G1,::,...,:;1G8 8                  
                              8C1:.:C888                8888800GG0G1:;;,...,:;1C                    
                             8C1;,;C8  88                 888800GGGGii1i:...,:;1C                   
                            8Cti:iL088  8                   8880GGGGLi1fi,..,,;itG                  
                        8  8CtiiifG888                      8880GCCGG1itt:.  ,:;1f0                 
                          8Gt1111L088                       8880GGCCGfi;i,.  .,;itG8                
                       8  8L111ttL088                       88800GLLCLi,:.   ..:i1C8                
                         8GL1;iftLG08                       8880GCLLCf;.,..  ..:itG8                
                      88 8GLtii1tfCG8888      88         888880GGLLLL1::;;;::::;1t0                 
                       880GLLftiiitL0888    8888888      888800GLfffLti:,,..,::;1L8                 
            8 8   8  8880CLLLfftt;:;tC08888888888888   8888800GCfLLLLLfttt111tttfLC0                
            888 8888880GCLLLLfffffi,,:1C08888888088888880000GGCftfffLffffffffffffftC8  8   88       
               80GGCCCCLfffLfffffff1,..:1L0880880088800000GGCLft1tffLLfffffffffffftfG8 88  88   88  
              8GLfLLffffffffffffffft1:.  ,1C00000G0000GGGCCLftt11tffffffffffffffffttLG088          8
              80LfLfffffffffffffffffft;.  ,1CCCGGCGGCCCCLffttt1;;1ffffffffttfffffftttfC088        88
              80Cffffffffffffffffffftft;,:ittffffffftttt111t1i:.,1ffffffftttttttttttffffL08        8
               0Cffffffffffffffffffffffti;;i1tttttt1111111i:,. .;tffffttttttttttttttfftitC8        8
              80Cffffffffftffftfffffffftt1;,,,:;;;;;;;::,..    .iffffftttttttttttttt11tfG088      88
              8GLffffffffffffttttfttffftt11i:....    .  .......:tffffffttttttttttttttLC008888     80
              80Lffffffffffffftttfftfffft11i:,,,,,,,,,,,,,::,.,;tfffffftttttfftt111tfLCG00888     80
               880GCCLLfftttttttttfffffftt1i:,,::::::::::::,,,,;1fffffftttfft1i;;i1tfLCGG0888     88
                   888800GGCLffttttttttt11iii1tffffffffffffffffffttffftttt1i;::;i1tfLCGG00888    888
                       8888800GGCLfttt1tttfLCGGGGGGGGGGG0000000GCftttt11ii;;;ittfLCGG00088888    88 
                            88888800GGGGG0000800888888888888888800CLLfffffLLCCG000000888888         
                              888888888888888  88888888        888800000000008888888888888 
""")
print("👋 Welcome, dear player, to the ultimate Rock‑Paper‑Scissors showdown!")
choices = ["r", "p", "s"]
art = {"r": rock, "p": paper, "s": scissors}

win = [
    "🎉 Victory! You crushed me this time!",
    "🏅 Well played! You’re a true RPS master.",
    "💪 You win! The machine bows to your skill.",
    "✨ Unbelievable! You actually beat me. (Don’t get used to it.)",
    "😎 Nice one! You’re on fire today.",
]
lose = [
    "💀 Ouch! I win – better luck next time!",
    "🤖 Ha! The machine reigns supreme.",
    "😈 You lose! Did you really think you could outsmart me?",
    "🏴‍☠️ Defeat! But every loss is a lesson…",
    "😝 Better luck next round, human!",
]
draw = [
    "🤝 It’s a draw! We’re evenly matched.",
    "😐 Stalemate – let’s go again!",
    "⚖️ Tie! Guess we think alike.",
    "🔄 No winner this time – rematch?",
    "🤨 Hmm, we chose the same thing. Spooky!",
]
invalid = [
    "😏 Nice try, but that's not how this game works. Stick to r, p, or s!",
    "🤦 Did you just make that up? r/p/s, please!",
    "😂 You think you can break me with that? Try r, p, or s.",
    "🙄 Come on, human. It's literally three letters: r, p, or s.",
    "💀 My circuits are confused. Just type r, p, or s!",
    "⚔️ That weapon isn't in our arsenal! Choose: (r)ock, (p)aper, or (s)cissors.",
    "🧙 The ancient scrolls only speak of three choices: r, p, and s.",
    "🎯 Aim better! Pick a valid option: r, p, or s.",
    "🚨 *Alarm sounds* Invalid input detected! Please enter r, p, or s.",
]

user = input("✊ Make your move: (r)ock, (p)aper, or (s)cissors? ").lower()
if user not in choices:
    print(choice(invalid))
    exit()

computer = choice(choices)

print(f"🎯 Your choose {art[user]}")
print(f"⚡ The machine throws {art[computer]}")

if user == computer:
    print(choice(draw))
else:
    # Find user's index and check if the next item in the list beats them
    user_wins = (choices.index(user) + 2) % 3 == choices.index(computer)
    if user_wins:
        print(choice(win))
    else:
        print(choice(lose))
