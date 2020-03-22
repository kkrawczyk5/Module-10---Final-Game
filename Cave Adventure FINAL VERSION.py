#Name: Kamil Krawczyk
#University: National-Louis University
#Contact: kkrawczyk@my.nl.edu
#Course: CSS 225 Winter semester
#Language: Python3
#Name of game: Cave Adventure
#Version: Final version of game
#Type of game: Text based 

import random


def intro_screen(main):
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("~   CAVE ADVENTURE                                              ~")
  print("~             CAVE ADVENTURE                                    ~")
  print("~                        CAVE ADVENTURE                         ~")
  print("~                                   CAVE ADVENTURE              ~")
  print("~                                                CAVE ADVENTURE ~")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  answer = str(input("Press Enter to begin... "))
  if answer == "":
    main(chapter_1)

def main(chapter_1):
  name = str(input("\nHello adventurer, what is your name? - "))
  print("\nHello adventurer. By accepting this adventure, you promise to retrieved the antidote to your loved one!") 
  answer = str(input("ready to begin? (y/n) - "))
  if answer == "y":
    print("Okay let's begin!")
    print("\n")
    chapter_1(chapter_2)
  else:
    print("Okay your loss :(")
  
  

def chapter_1(chapter_2):
  print("Overview - You are an adventurer heading inside a dangerous cave. At the end of this cave lies the andidote that your loved one requires to recover from the plague. It is your job to get the antidote. \n")
  print("The adventurer walks into the cave and is ready to begin your adventure. \n")
  answer = input("As you walk deeper into the cave you are encountered by your first decision. Do you; \n\n1)attempt to leave cave \n2)pick up bow\n3)investigate the bones\n4)pick up sword \n\n(input number corresponding to your choice) - ")
  if answer == "4":
    chapter_2(chapter_1, chapter_3, chapter_4)
  elif answer == "2":
    chapter_2(chapter_1, chapter_3, chapter_4)
  elif answer == "3":
    print("You notice the bones of another adventurer that was not able to complete the task. However, you are not phased")
    answer_2 = input("What would you like to do now? \n\n1)attempt to leave cave \n2)pick up bow\n3)pick up sword\n\n(input number corresponding to your choice) - ")
    if answer_2  == "3":
      chapter_2(chapter_1, chapter_3, chapter_4)
    elif answer_2 == "2":
      chapter_2(chapter_1, chapter_3, chapter_4)
    elif answer_2 == "1":
       print("\nYou turn around and exit the cave. Your loved one dies at home later that night due to the lack of the antidote. :(") 
  elif answer == "1":
    print("\nYou turn around and exit the cave. Your loved one dies at home later that night due to the lack of the antidote. :(")
def chapter_2(chapter_1, chapter_3, chapter_4):
  print("\nCongratulations of making it to the second chapter. There are still a lot of challenges awaiting you. ")
  print("\nAs you walk deeper into the cave, you realize that the path splits into three. Which one will you take?")
  answer = str(input("\n\n1)path one \n2)path two \n3)path three\n\n(input number corresponding to your choice) - "))
  if answer == "1":
    print("\nCongrats, you have made the right choice. You will now advance to chapter 3")
    chapter_3(chapter_2, chapter_4)
  elif answer == "2":
    print("\nYou chose the secret path that lets the hero avoid the upcoming ravine. Skipping to chapter 4")
    chapter_4(chapter_5)
  elif answer == "3":
    print("\nThis path has taken the user outside of the cave without the antidote. Game Over.")
    answer_2 = str(input("\nwould you like to re-enter the cave and try again? \n\n1)yes\n2)no\n\n(input number corresponding to your choice) - "))
    if answer_2 == "1":
      chapter_1(chapter_2)
    elif answer_2 == "2":
      print("\nYou did not restart the game. Game Over.")

def chapter_3(chapter_2, chapter_4):
  print("\nAnother hard decision ended up being another victory for the hero. There is nothing stopping you from getting the antidote")
  print("\nBefore you get the antidote, you are tasked with another challenge. As you walk deeper into the cave you discover that your path is blocked by a very large ravine. As the hero, you must decide what to do next.")
  answer = str(input("\n\n1)attempt to jump the ravine\n2)walk back using the previous path\n3)throw a rock down the ravine \n\n(input number corresponding to your choice) - "))
  if answer == "1":
    ravine_jump = random.randint(0,1)
    if ravine_jump == 0:
      print("\nYou made the jump. Move on to chapter 4")
      chapter_4(chapter_5)
    elif ravine_jump == 1:
      print("\nThe hero was unable to make the jump and has died. Game Over")
      retry = str(input("Would you like to try again? \n\n1)Yes \n2)No\n\n(input number corresponding to your choice) - "))
      if retry == "1":
        chapter_3(chapter_2, chapter_4)
      elif retry == "2":
        print("You did not to decide to save your loved one. GAME OVER")
  elif answer == "2":
    print("\nIt is clear that the hero is afraid to tackle the challenge ahead and turns back around. Back to chapter 2")
    chapter_2(chapter_1, chapter_3, chapter_4)
  elif answer == "3":
    print("\nYou throw a rock down the ravine and it takes 15 seconds before you hit it hit the ground. What is the next move?")
    print("\n\n1)attempt to jump the ravine\n2)walk back using the previous path \n\n(input number corresponding to your choice) -")
    answer_2 = input()
    if answer_2 == "1":
      ravine_jump = random.randint(0,1)
      if ravine_jump == 0:
        print("You made the jump. Move on to chapter 4")
        chapter_4(chapter_5,)
      elif ravine_jump == 1:
        print("\nThe hero was unable to make the jump and has died. Game Over")
        retry_2 = str(input("Would you like to try again? \n\n1)Yes \n2)No\n\n(input number corresponding to your choice) - "))
        if retry_2 == "1":
          chapter_4(chapter_5)
        elif retry_2 == "2":
          print("You did not to decide to save your loved one. GAME OVER")
    elif answer_2 == "2":
      print("\nIt is clear that the hero is afraid to tackle the challenge ahead and turns back around. Back to chapter 2")
      chapter_2(chapter_1, chapter_3, chapter_4)

def chapter_4(chapter_5):
  print("\nAs the hero adventures deeper into the cave looking for the cure, the biggest challenge was right ahead of the hero.")
  print("\nAs the hero walked into the open area, he sees as the Minotaur wakes up and ready to defend the final treasure(the antidote)")
  choice = str(input("\nThe hero must make the ultimate choice here; fight the minotaur or attempt to run past him for the antidote. \n\n1)Attack\n2)Run Away \n\n(input number corresponding to your choice) - "))
  if choice == "1":
    boss_fight = random.randint(0,1)
    if boss_fight == 0:
      print("\nYou managed to defeat the boss and grab the antidote. You run out of the cave with the antidote")
      chapter_5()
    elif boss_fight == 1:
      print("\nThe minotaur squishes the hero like a bug. Game Over.")
      retry = str(input("\n\nWould you like to try again? \n\n1)yes \n2)no \n\n(input number corresponding to your choice) "))
      if retry == "1":
        chapter_4(chapter_5,)
      else:
        print("\nGAME OVER")
  elif choice == "2":
    print("\nThe hero attempted to run past the minotaur to grab the antidote but got swiped and killed by the beast. Game Over.")

def chapter_5():
  print("\nThe hero did it, he was able to recover the antidote and will now be able to save his loved one")
  print("\nAs the hero was running to his loved one, he is stopped by a mysterious old man. The man offered the hero a choice")
  answer = str(input("\nThe hero could either keep the antidote and save the loved one or he could had over the antidote to the man for so much gold that the hero would never have to move a finger again. What will the hero choose? \n\n1)Keep \n2)Give \n\n(input number corresponding to your choice) - "))
  
  if answer == "1":
    print("The hero made the right choice. The hero told the mysterious old man to scram and was able to deliver the antidote to the dying loved one")
    print("\n"* 50, "Thank you for playing. :)")
  elif answer == "2":
    print("The hero was rewarded with wealth but in result his wife passed away with no antidote. The hero felt guilty about not saving his loving wife until the day he passed away")
    print("\n"* 50, "THE END.")


intro_screen(main)

