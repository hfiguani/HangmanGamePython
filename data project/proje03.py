#Project 03
#Created by Hafed, Hamida, Shirley, Sanjay
#November 7,2016
#CIT-125 Python

iscol=True
def headers(column):
      iscol=True
      headers=["Player name" ,"TeamId" , "Games", "At bats" ,"Runs scored", "Hits" ,"Doubles","Triples","Homeruns",column]
      header=''
      for hedr in headers:
           if hedr== headers[0]:
                header+='|'+hedr.center(22,' ')
           else:
                if hedr=='':
                      iscol=False
                      break
                header+='|'+hedr.center(11,' ')
      if iscol:
          print('-'.ljust(132, '-'))
          print(header+'|')
          print('-'.ljust(132, '-'))           
      else:
          print('-'.ljust(120, '-'))
          print(header+'|')
          print('-'.ljust(120, '-'))
    
Tids=[]
fcounter=1
while True:
      cmd=input(">> Please, Enter a command: ")
      wcmd=cmd
      if not cmd:
          print("Null value is not recognized as a valid command.")
          continue
      cmd=cmd.upper()
      CMD=cmd.split()
      cmd=CMD[0]
      if  cmd=='QUIT':
           if len(CMD)>1:
                print("Invalid command ! Try again.")
                continue
           else:
                quit()
      elif cmd=='HELP':
           if len(CMD)>1:
                print("Invalid command ! Try again.")
                continue
           else:
                print()
                print("HELP                Displays all available commands)")
                print("INPUT [filename]    Displays all players in the 'mlb.2013.txt' file.")
                print("TEAM [team id]      Displays a team with a specific identifier.")
                print("REPORT [int n][str] Displays all information about the top n players in a given category:") 
                print("                    HITS -- number of hits")
                print("                    BATTING -- batting average ")
                print("                    SLUGGING -- slugging percentage.")
                print("QUIT                Halts the execution.")
                print()
      elif cmd=='INPUT':
           if len(CMD)>2:
                print("Invalid command ! Try again.")
                continue
           elif CMD[1]!='MLB.2013.TXT':
                if fcounter==3:
                      print("Maximum of attempts exceeded.")
                      quit()
                else:
                      print("Invalid file name ! Try again.")
                      fcounter+=1
                      continue
           else:
                tline=()
                headers('')
                f=open('mlb.2013.txt')
                for lin in f:
                     tline=lin.strip().split(';')
                     header=''
                     for word in tline:
                             if word== tline[0]:
                                  header+='|'+word.ljust(22,' ')
                             elif word== tline[1]:
                                  header+='|'+'  '+word.center(4,' ')
                             else:
                                  header+='     |'+word.rjust(6,' ')
                     print(header+'     |')
                f.close()
                print('-'.ljust(120, '-')) 
      elif cmd=='TEAM':
           if len(CMD)>2 or len(CMD)==1 :
                print("Invalid command ! Try again.")
                continue
           else:
                f=open('mlb.2013.txt')
                for ln in f:
                     line=ln.strip().split(';')
                     if line[1].strip()  not in Tids:
                          Tids.append(line[1].strip() )
                f.close()
                CMD[1]=CMD[1].upper()
                if CMD[1] not in Tids:
                     print("Invalid Team ID !")
                     continue
                else:
                     headers('')
                     f=open('mlb.2013.txt')
                     for player in f:
                          pline=player.strip().split(';')
                          if pline[1].strip()==CMD[1]:
                               header=''
                               for word in pline:
                                   if word== pline[0]:
                                        header+='|'+word.ljust(22,' ')
                                   elif word== pline[1]:
                                        header+='|'+'  '+word.center(4,' ')
                                   else:
                                        header+='     |'+word.rjust(6,' ')
                               print(header+'     |')
                     f.close()
                     print('-'.ljust(120, '-'))
      elif cmd=='REPORT':
          if len(CMD)>4 or len(CMD)<3 :
                print("Invalid command ! Try again.")
                continue
          if len(CMD)==4:
                f=open('mlb.2013.txt')
                for ln in f:
                     line=ln.strip().split(';')
                     if line[1].strip() not in Tids:
                          Tids.append(line[1].strip() )
                f.close()
                CMD[3]=CMD[3].upper()
                if CMD[3] not in Tids:
                     print("Invalid Team ID !")
                     continue
                else:
                      allTeams=False
          else:
                allTeams=True

          if not CMD[1].isnumeric() or int(CMD[1])==0:
               print("REPORT command has to be followed by an integer greater than zero !")
               continue
          elif CMD[2] not in["HITS","BATTING","SLUGGING"]:
               print("Invalid identifier ! ")
               continue
          else:
              result=[]
              f=open('mlb.2013.txt')
              for player in f:
                    pline=player.strip().split(';')
                    if CMD[2]=='HITS':
                         column=''
                         iscol=False
                         if int(pline[5]) not in result:
                              if allTeams==False:
                                     if pline[1].strip()==CMD[3]:
                                            result.append(int(pline[5]))
                              else:
                                     result.append(int(pline[5]))
                    if CMD[2]=='BATTING':
                         column='Batting'
                         iscol=True
                         if allTeams==True:
                                btg='%.3f' %(int(pline[5])/int(pline[3]))
                         else:
                              if pline[1]==CMD[3]:
                                btg='%.3f' %(int(pline[5])/int(pline[3]))
                         if btg not in result:
                              result.append(btg)
                    if CMD[2]=='SLUGGING':
                         column='Slugging'
                         iscol=True
                         if allTeams==True:
                                   slg=(int(pline[4])+2*int(pline[6])+3*int(pline[7])+4*int(pline[8]))/int(pline[3])
                         else:
                             if pline[1]==CMD[3]:
                                   slg=(int(pline[4])+2*int(pline[6])+3*int(pline[7])+4*int(pline[8]))/int(pline[3])
                         if slg not in result:
                              result.append('%.3f' %slg)
              result.sort()
              result.reverse()
              result=result[:int(CMD[1])]
              f.close()
              i=0
              headers(column)
              for score in result:
                  if i==int(CMD[1]):
                       break 
                   
                  f=open('mlb.2013.txt')
                  for pl in f:
                      pls=pl.strip().split(';')
                      if CMD[2]=='HITS':
                          if allTeams==False:
                              if int(pls[5])==score and pls[1].strip()==CMD[3]:
                                  if i==int(CMD[1]):
                                       break
                                  header=''
                                  for word in pls:
                                         if word== pls[0]:
                                              header+='|'+word.ljust(22,' ')
                                         elif word== pls[1]:
                                              header+='|'+'  '+word.center(4,' ')
                                         else:
                                              header+='     |'+word.rjust(6,' ')
                                  print(header+'     |')
                                  i+=1
                          else:
                              if int(pls[5])==score: 
                                  if i==int(CMD[1]):
                                       break
                                  header=''
                                  for word in pls:
                                         if word== pls[0]:
                                              header+='|'+word.ljust(22,' ')
                                         elif word== pls[1]:
                                              header+='|'+'  '+word.center(4,' ')
                                         else:
                                              header+='     |'+word.rjust(6,' ')
                                  print(header+'     |')
                                  i+=1
                      elif CMD[2]=='BATTING':
                          if score=='%.3f' %(int(pls[5])/int(pls[3])):
                                if i==int(CMD[1]):
                                     break
                                header=''
                                pls.append(score)
                                for word in pls:
                                   if word== pls[0]:
                                        header+='|'+word.ljust(22,' ')
                                   elif word== pls[1]:
                                        header+='|'+'  '+word.center(4,' ')
                                   elif word== pls[9]:
                                        header+='     |'+'   '+word.center(6,' ')
                                   else:
                                        header+='     |'+word.rjust(6,' ')
                                print(header+'  |')
                                i+=1
                      else:
                         
                          if score=='%.3f'%((int(pls[4])+2*int(pls[6])+3*int(pls[7])+4*int(pls[8]))/int(pls[3])):
                                if i==int(CMD[1]):
                                     break
                                header=''
                                pls.append(score)
                                for word in pls:
                                   if word== pls[0]:
                                        header+='|'+word.ljust(22,' ')
                                   elif word== pls[1]:
                                        header+='|'+'  '+word.center(4,' ')
                                   elif word== pls[9]:
                                        header+='     |'+'   '+word.center(6,' ')
                                   else:
                                        header+='     |'+word.rjust(6,' ')
                                print(header+'  |')

                                i+=1

              f.close()
              if iscol:
                   print('-'.ljust(132, '-'))
              else:
                   print('-'.ljust(120, '-'))
      else:
          print("'"+wcmd+"' is not recognized as a valid command.")
          continue
