import random 

class Player:
  name = ""
  score = 0

  def guessNumber(self):
    self.number = random.randint(0, 20)   #Generates a random number
    self.guessLimit = 7
    self.guess_list = []
    self.guesses = 0
    print()
    print("I have selected a number between 1 to 20")
    print("You have 7 chances to guess that number")
    print()
    
    while self.guessLimit > 0:
      print()
      self.user_guess = int(input("Enter a number between 1 and 20: "))

      if self.user_guess > 20 or self.user_guess < 0:
        print("-----------------------------")
        print(self.user_guess, "is not in the range of numbers.")
        print(self.name, ", You have", self.guessLimit, "guesses left.")
        print("Try again.")
        
      elif self.user_guess > self.number:
        print("------------------------------")
        print(self.user_guess, "is too high!")
        self.guesses += 1
        self.guessLimit -= 1
        print(self.name, ", You have", self.guessLimit, "guesses left.")
        self.guess_list.append(self.user_guess)
        
      elif self.user_guess < self.number:
        print("------------------------------")
        print(self.user_guess, "is too low")
        self.guesses += 1
        self.guessLimit -= 1
        print(self.name, ", You have", self.guessLimit, "guesses left.")
        self.guess_list.append(self.user_guess)
        
      else:
        self.score += 1
        self.guessLimit -= 1
        self.guess_list.append(self.user_guess)
        print("------------------------------")
        print(self.user_guess, "is the correct number!")
        print("You had", self.guessLimit, "guesses left over!")
        print("Great Job!", self.name)
        print("Here are all the numbers you guessed")
        
        for i in self.guess_list:
          print(i)
        self.guess_list.clear()
        
        self.play_again = input("Would you like to play again (y/n)? ")
        self.play_again = self.play_again.lower()

        
        if self.play_again == "n":
          print("Your overall score is", self.score)
          print("GOODBYE")
          self.guessLimit = -1
          
          
        else:
          user.guessNumber()
          
    
    
    while self.guessLimit == 0:
      print("You used up all your chances!")
      print("The correct number was", self.number)
        
      for i in self.guess_list:
        print(i)
      self.guess_list.clear()
      self.play_again = input("Would you like to play again (y/n)? ")
      self.play_again = self.play_again.lower()
      if self.play_again == "n":
        print("------------------------------")
        print("GOODBYE")
        print("Your overall score is", self.score)
        self.guessLimit -= 1
      else:
        user.guessNumber()

user = Player()
user.name = input("What is your name? ")
user.guessNumber()

