import random



def intro_screen(main):
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("~                                                               ~")
  print("~                                                               ~")
  print("~                        CAVE ADVENTURE                         ~")
  print("~                                                               ~")
  print("~                                                               ~")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  answer = str(input("Press the key 'y' to begin - "))
  if answer == "y":
    main(chapter_1)

def main(chapter_1):
  name = str(input("\nHello adventurer, what is your name? - "))
  print("\nHello", name, "ready to begin? (y/n)")
  answer = str(input())
  if answer == "y":
    print("Okay let's begin!")
    print("\n")
    chapter_1(chapter_2, name)
  else:
    print("Okay your loss :(")
  
  

def chapter_1(chapter_2, name):
  print("Overview - You are an adventurer heading inside a dangerous cave. At the end of this cave lies the andidote that your loved one requires to recover from the plague. It is your job to get the antidote. \n")
  print(name, "walks into the cave and are ready to begin your adventure. \n")
  answer = input("As you walk deeper into the case you are encountered by your first decision. Do you; attempt to leave cave/pick up bow/investigate the bones/pick up sword? - ")
  if answer == "pick up sword":
    chapter_2(chapter_1, chapter_3, chapter_4)
  elif answer == "pick up bow":
    chapter_2(chapter_1, chapter_3, chapter_4)
  elif answer == "investigate the bones":
    print("You notice the bones of another adventurer that was not able to complete the task. However, you are not phased")
    answer_2 = input("What would you like to do now? - (pick up sword/pick up bow/attempt to leave the cave) - ")
    if answer_2  == "pick up sword":
      chapter_2(chapter_1, chapter_3, chapter_4)
    elif answer_2 == " pick up bow":
      chapter_2(chapter_1, chapter_3, chapter_4)
    elif answer_2 == "attempt to leave cave":
       print("\nYou turn around and exit the cave. Your loved one dies at home later that night due to the lack of the antidote. :(") 
  elif answer == "attempt to leave cave":
    print("\nYou turn around and exit the cave. Your loved one dies at home later that night due to the lack of the antidote. :(")
def chapter_2(chapter_1, chapter_3, chapter_4):
  print("\nCongratulations of making it to the second chapter. There are still a lot of challenges awaiting you. ")
  print("\nAs you walk deeper into the cave, you realize that the path splits into three. Which one will you take?")
  answer = str(input("(path one/path two/path three?) - "))
  if answer == "path one":
    print("\nCongrats, you have made the right choice. You will now advance to chapter 3")
    chapter_3(chapter_2, chapter_4)
  elif answer == "path two":
    print("\nYou chose the secret path that lets the hero avoid the upcoming ravine. Skipping to chapter 4")
    chapter_4(chapter_5)
  elif answer == "path three":
    print("\nThis path has taken the user outside of the cave without the antidote. Game Over.")
    print("\nwould you like to re-enter the cave and try again? yes/no")
    answer_2 = input()
    if answer_2 == "yes":
      chapter_1(chapter_2)
    elif answer_2 == "no":
      print("You did not restart the game. Game Over.")

def chapter_3(chapter_2, chapter_4):
  print("\nAnother hard decision ended up being another victory for the hero. There is nothing stopping you from getting the antidote")
  print("\nBefore you get the antidote, you are tasked with another challenge. As you walk deeper into the cave you discover that your path is blocked by a very large ravine. As the hero, you must decide what to do next.")
  print("\n(attempt to jump the ravine/walk back using the previous path/throw a rock down the ravine) - ")
  answer = input()
  if answer == "attempt to jump the ravine":
    ravine_jump = random.randint(0,1)
    if ravine_jump == 0:
      print("\nYou made the jump. Move on to chapter 4")
      chapter_4(chapter_5)
    elif ravine_jump == 1:
      print("\nThe hero was unable to make the jump and has died. Game Over")
  elif answer == "walk back using the previous path":
    print("\nIt is clear that the hero is afraid to tackle the challenge ahead and turns back around. Back to chapter 2")
    chapter_2(chapter_1, chapter_3, chapter_4)
  elif answer == "throw a rock down the ravine":
    print("\nYou throw a rock down the ravine and it takes 15 seconds before you hit it hit the ground. What is the next move?")
    print("\nattempt to jump the ravine/walk back using the previous path?")
    answer_2 = input()
    if answer_2 == "attempt to jump the ravine":
      ravine_jump = random.randint(0,1)
      if ravine_jump == 0:
        print("You made the jump. Move on to chapter 4")
        chapter_4(chapter_5,)
      elif ravine_jump == 1:
        print("\nThe hero was unable to make the jump and has died. Game Over")
    elif answer_2 == "walk back using the previous path":
      print("\nIt is clear that the hero is afraid to tackle the challenge ahead and turns back around. Back to chapter 2")
      chapter_2(chapter_1, chapter_3, chapter_4)

def chapter_4(chapter_5, ):
  print("\nAs the hero adventures deeper into the cave looking for the cure, the biggest challenge was right ahead of the hero.")
  print("\nAs the hero walked into the open area, he sees as the Minotaur wakes up and ready to defend the final treasure(the potion)")
  print("\nThe hero must make the ultimate choice here; fight the minotaur or attempt to run past him for the potion. (attack/run past)")
  choice = input()
  if choice == "attack":
    boss_fight = random.randint(0,1)
    if boss_fight == 0:
      print("\nYou managed to defeat the boss and grab the antidote. You run out of the cave with the antidote")
      chapter_5()
    elif boss_fight == 1:
      print("\nThe minotaur squishes the hero like a bug. Game Over.")
      retry = str(input("\n\nWould you like to try again? (y/n) - "))
      if retry == "y":
        chapter_4(chapter_5,)
      else:
        print("\nGAME OVER")
  elif choice == "run past":
    print("\nThe hero attempted to run past the minotaur to grab the potion but got swiped and killed by the beast. Game Over.")

def chapter_5():
  print("\nThe hero did it, he was able to recover the antidote and will now be able to save his loved one")
  print("\nAs the hero was running to his loved one, he is stopped by a mysterious old man. The man offered the hero a choice")
  answer = str(input("\nThe hero could either keep the potion and save the loved one or he could had over the potion to the man for so much gold that the hero would never have to move a finger again. What will the hero choose? (keep/give)"))
  
  if answer == "keep":
    print("The hero made the right choice. The hero told the mysterious old man to scram and was able to deliver the antidote to the dying loved one")
    print("\n Thank you for playing. :)")
  elif answer == "give":
    print("The hero was rewarded with wealth but in result his wife passed away with no potion. The hero felt guilty about not saving his loving wife until the day he passed away")
    print("THE END.")



intro_screen(main)


