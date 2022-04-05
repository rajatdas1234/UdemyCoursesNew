print('''
*******************************************************************************
         ,----.    ,-.   ,----.,------. ,-.   ,-.,-. ,-.
    / ,-,_/  ,'  |  / /"P /`-, ,-','  |  / //  |/ /
   / / __  ,' ,| | / ,---'  / / ,' ,| | / // J P /
  / '-' /,' ,--. |/ /      / /,' ,--. |/ // /|  /
  `----''--'   `-'`'.--""""--.--'   `-'`' `' `-'
  nnnnnnnnnnnnnnnn,'.n*""""*N.`.#######################
  NNNNNNNNNNNNNNN/ J',n*""*n.`L \##### ### ### ### ####
                : J J___/\___L L :#####################
  nnnnnnnnnnnnnn{ [{ `.    ,' }] }## ### ### ### ### ##
  NNNNNNNNNNNNNN: T T /,'`.\ T J :#####################
                 \ L,`*n,,n*',J /
  nnnnnnnnnnnnnnnn`. *n,,,,n* ,'nnnnnnnnnnnnnnnnnnnnnnn
  NNNNNNNNNNNNNNNNNN`-..__..-'NNNNNNNNNNNNNNNNNNNNNNNNN
  ,-.    ,-.  ,-. ,----. ,----.,-. ,----.   ,-. 
  |  `.  \  `.|  \\  .--`\ \"L \\ \\ .-._\  |  `. o!0
  | |. `. \ \ ` L \\  __\ \ .  < \ \\ \  __ | |. `.
  | .--. `.\ \`-'\ \\ `---.\ \L `.\ \\ `-` \| .--. `. 
  `-'   `--``'    `-'`----' `-'`-' `' `----'`-'   `--'
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
c = input("You are at a crossroad, where do you want to go? Type 'left' or 'right'.").lower()
if c== "right" or c!="left":
  print("Sorry - you fall into a hole. GAME OVER!!!")
  print('''
        *******************************
        88                      88             
88                      88             
88                      88             
88,dPPYba,   ,adPPYba,  88  ,adPPYba,  
88P'    "8a a8"     "8a 88 a8P_____88  
88       88 8b       d8 88 8PP"""""""  
88       88 "8a,   ,a8" 88 "8b,   ,aa  
88       88  `"YbbdP"'  88  `"Ybbd8"'  
        ********************************
        ''')
else:
  r= input("Here comes the mighty river. Would you like to 'swim' or 'wait' ?").lower()
  if r== "swim" or r!="wait":
    print("Sorry, you are attacked by a trout. GAME OVER!!!")
    print('''
          ****************************************
          
                    .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
          snd                         (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-'
          ****************************************
          ''')
  else:
    d=input("You now arrive a 3 door location. You would need to choose only 1 door from 3 doors with different colors to go      to the next step. Choose the 'Red' or 'Yellow' or 'Blue' door").lower()
    if d=="red":
      print("Sorry, you have been burned by fire. GAME OVER!!!")
      print('''
            ***********************************
                         (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            ***********************************
            ''')
    elif d=="blue":
      print("Sorry, you have been eaten by beasts. GAME OVER!!!")
      print('''
            ********************************
            
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
            *********************************
            ''')
    elif d!="yellow":
      print("GAME OVER!!!")
    else:
      print("Congratulations, You Win!!!")
      print('''
                                                           888            
                                               888            
                                               888            
 .d8888b .d88b. 88888b.  .d88b. 888d888 8888b. 888888.d8888b  
d88P"   d88""88b888 "88bd88P"88b888P"      "88b888   88K      
888     888  888888  888888  888888    .d888888888   "Y8888b. 
Y88b.   Y88..88P888  888Y88b 888888    888  888Y88b.      X88 
 "Y8888P "Y88P" 888  888 "Y88888888    "Y888888 "Y888 88888P' 
                             888                              
                        Y8b d88P                              
                         "Y88P"                               
            ''')
  