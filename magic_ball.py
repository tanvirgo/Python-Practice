import random
#variables
name = input("What is your name?\n")
asker = name + " asks: "
question = ''

#Actual program
#The function
def magic_8_ball():
  random_number = random.randint(1, 12)
  if random_number == 1:
    answer = 'Yes-obviously'
  elif random_number == 2:
    answer = 'Hell no!'
  elif random_number == 3:
    answer = 'Without a doubt'
  elif random_number == 4:
    answer = 'What kind of question is that? OF COURSE!'
  elif random_number == 5:
    answer = 'Probably'
  elif random_number == 6:
    answer = 'Probably not'
  elif random_number == 7:
    answer = 'My sources say no'
  elif random_number == 8:
    answer = 'DUHHHH'
  elif random_number == 9:
    answer = 'Very doubtful'
  elif random_number == 10:
    answer = 'Not happening'
  elif random_number == 11:
    answer = "Hell yeah!"
  elif random_number == 12:
    answer = "Nah bro"
  else:
    answer = 'Error'
  return answer
#Function break
while question != "Stop" or question != "stop": 
  question = input("Ask a question! It has to be yes or no!\nSay 'Stop' when you are done asking questions\n")
  if question == "Stop" or question == "stop":
    print("Ok! You were asking too many questions anyway!")
    break
#Print
  answer = magic_8_ball()
  print(asker + question + '\n')
  print("Magic 8-Ball's answer: " + answer)
  print()