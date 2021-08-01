# FreeCodeCamp course

# STEPS
# madlibs style introduction - goal: fill in the blank spaces with the users input
# create a game function called play_game
# write madlibs story with blank inputs
# accept user input and set it to a variable 
# repeat for all blank spaces
# call game function
# offer to play again -- create a check_play_again function that returns a Boolean
  # if True - replay play_game
  # if False - thanks for playing message and end game

def play_game():
  name = input("What's your name? ")
  occupation = input("What's your occupation? ")
  fun_fact = input("Fun fact about yourself that can start with 'I have...': ")

  story = f'Hello! My name is {name} and I am a {occupation}. Fun fact about me: I have {fun_fact}.'
  print(story)
  
  play_again_response = input("Want to play again? (y/n) ")
  
  if check_play_again(play_again_response) == True : play_game()
  if check_play_again(play_again_response) == False : print('Thanks for playing!')

# HELPER FUNCTIONS
def check_play_again(user_response):
  lower_case_response = user_response.lower()
  if lower_case_response.startswith('y'): return True
  if lower_case_response.startswith('n'): return False

# PLAY GAME
play_game()
