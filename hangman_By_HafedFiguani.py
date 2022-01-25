#Hangman Game
#Created by Hafed Figuani
#October 19,2016
#CIT-125 Python 

import random

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote \
crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard \
llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python \
rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider \
stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(words):
     wordIndex = random.randint(0, len(words) - 1)
     return words[wordIndex]

def drawHangmanPic(piclist):
    for rw in piclist:
       line=""
       l=0
       while l < len(rw):
          line=line+rw[l]
          l+=1
       print(line)
    print("==========")

play='y'
while play in ['y','yes','Y','YES']:
      secret_word=getRandomWord(words)
      life=6
      right_gusses=[]
      wrong_gusses=[]
      for ewrd in secret_word:
         right_gusses.append('-')
      pic=[[' ','+','-','-','-','-','+'],[' ','|',' ',' ',' ',' ','|'],\
          [' ',' ',' ',' ',' ',' ','|'],[' ',' ',' ',' ',' ',' ','|'],\
          [' ',' ',' ',' ',' ',' ','|'],[' ',' ',' ',' ',' ',' ','|']]  
      
      while '-' in right_gusses:
          print("Missed letters:")
          guesses=''
          for eachwrd in right_gusses:
              guesses+=eachwrd
          print(guesses)
          print("Guess a letter:")
          guess=input() 
          if guess in right_gusses or guess in wrong_gusses:
               print("You have already guessed that letter. Choose again.")
               continue
          elif guess not in 'abcdefghijklmnopqrstuvwxyz':
               print('Please enter a LETTER.')    
               continue
          elif guess in secret_word:
               i=0
               for letter in secret_word:
                  if guess==letter:
                     right_gusses[i]=guess
                  i+=1
               if '-' not in right_gusses:
                  print("Yes! The secret word is "+secret_word+"! You have won!")
                  play=input("Do you want to play again? (yes or no)")
                  break
          else:
              wrong_gusses.append(guess)
              life-=1

          if life==5:
              pic[2][1]='o'
          elif life==4:
              pic[3][1]='|'            
          elif life==3:
              pic[3][0]='/'
          elif life==2:
              pic[3][2]='\\'
          elif life==1:
              pic[4][0]='/'      
          elif life==0:
              pic[4][2]='\\'
              drawHangmanPic(pic)
              print("You lose ! The secret word is "+secret_word+" !")
              play=input("Do you want to play again? (yes or no)")
              break

          drawHangmanPic(pic)

       

