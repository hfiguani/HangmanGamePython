import random

playAgain = 'yes'
statistics={'Equality':0,'User':0,'Computer':0,'User_Rock':0,'User_Sci':0,'User_Paper':0}
Weapons=['r','s','p']
def GetRandomMove(Weapons):
     MovesIndex = random.randint(0,2)
     return Weapons[MovesIndex]
def UserChoice():
     user_choice=''
     while user_choice not in ['r','s','p','q','Q']:
            user_choice=input("Enter your choice (r) for rock (s) for scissors (p) for paper (q) to end the round:")
            user_choice.lower()
     return user_choice       
def Comp_Choice_Rock(user_choice,statistics):
      if user_choice=='r':
             print("You tie, You chose rock and the computer chose rock")
             statistics['Equality']+=1
             statistics['User_Rock']+=1

      elif user_choice=='s':
             print("You lose, You chose scisors and the computer chose rock")
             statistics['Computer']+=1
             statistics['User_Sci']+=1
             
      elif user_choice=='p':
             print("You win, You chose paper and the computer chose rock")
             statistics['User']+=1
             statistics['User_Paper']+=1

def Comp_Choice_Scissors(user_choice,statistics):
      if user_choice=='s':
             print("You tie, You chose scissors and the computer chose scissors")
             statistics['Equality']+=1
             statistics['User_Sci']+=1

      elif user_choice=='p':
             print("You lose, You chose paper and the computer chose scissors")
             statistics['Computer']+=1
             statistics['User_Paper']+=1
             
      elif user_choice=='r':
             print("You win, You chose rock and the computer chose scissors")
             statistics['User']+=1
             statistics['User_Rock']+=1

def Comp_Choice_Paper(user_choice,statistics):
      if user_choice=='p':
             print("You tie, You chose paper and the computer chose paper")
             statistics['Equality']+=1
             statistics['User_Paper']+=1

      elif user_choice=='r':
             print("You lose, You chose rock and the computer chose paper")
             statistics['Computer']+=1
             statistics['User_Rock']+=1
             
      elif user_choice=='s':
             print("You win, You chose scissors and the computer chose paper")
             statistics['User']+=1
             statistics['User_Sci']+=1

while playAgain in ['yes','y','YES','Y']:
      playAgain = ''
      computer_choice=GetRandomMove(Weapons)
      user_choice=UserChoice()
      
      while user_choice not in ['q','Q']:
            computer_choice=GetRandomMove(Weapons)
            if computer_choice=='r':
                   Comp_Choice_Rock(user_choice,statistics)
            if computer_choice=='s':
                   Comp_Choice_Scissors(user_choice,statistics)
            if computer_choice=='p':
                   Comp_Choice_Paper(user_choice,statistics)
            user_choice=UserChoice()
            
      print('You won : '+str(statistics['User'])+' times.')
      print('You lose : '+str(statistics['Computer'])+' times.')
      print('You tie : '+str(statistics['Equality'])+' times.')
      print('You chose Rock : '+str(statistics['User_Rock'])+' times.')
      print('You chose Paper : '+str(statistics['User_Paper'])+' times.')
      print('You chose Scissors : '+str(statistics['User_Sci'])+' times.')

      while playAgain not in ['yes','y','YES','Y','no','NO','n','N']:
            playAgain = input('Do you want to play again? (yes or no)')
     
if playAgain in ['no','NO','n','N']:
     quit()
     
