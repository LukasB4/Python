# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 4: Pokedex                    |
# Lukas Bernard(, Colby Roberts)        |
# Last Modified: October 28, 2020       |
# ---------------------------------------
# A brief overview of the program.
# ---------------------------------------

# Your solution goes here ...

# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

import string
class Pokemon:
  

  def __init__ (self, name, number, combat_points, types):
    self.number = number
    self.name = name
    self.combat_points = combat_points
    self.types = types

  def get_name(self):
    return self.name

  def get_number(self):
    return self.number

  def get_types(self):
    return self.types

  def get_combat_points(self):
    return self.combat_points

  def __repr__(self):
    return 'Number: {pnumber}, Name: {pname}, CP: {pcp}, Type: {ptypes}'.format(pnumber = int(self.number), pname = str(self.name), pcp = str(self.combat_points), ptypes = str(' and '.join(self.types)))

def total_by_type(pokedex, ptype):
  count = 0
  for i in range(len(pokedex)):
    if ptype in pokedex[i].get_types():
      count += 1
  print("Number of Pokemon that contain type " + ptype + " = " + str(count))
  
  
def lookup_by_name(pokedex, name): 
  found = False
  for i in range(len(pokedex)):
    if (name == pokedex[i].get_name()):
      found = True
      num = i
  if found == True:
    print(pokedex[num].__repr__())
  elif found == False:
    print("There is no Pokemon Named " + str(name))
  
def lookup_by_number(pokedex, number): 
  found = False
  for i in range(len(pokedex)):
    if (number == pokedex[i].get_number()):
      found = True
      num = i
  if found == True:
    print(pokedex[num].__repr__())
  elif found == False:
    print("There is no Pokemon number " + str(number))
  
def average_hit_points(pokedex):
  hitpoints = 0
  counter = 0
  for i in range(len(pokedex)):
    hitpoints += int(pokedex[i].get_combat_points())
    counter += 1
  avhitpoints = hitpoints/counter
  avhitpoints = round(avhitpoints, 2)
  print("Average pokemon combat points: ", avhitpoints)

def print_pokedex(pokedex): 
  for i in range(len(pokedex)):
    print(pokedex[i])
			
def print_menu():
  print("1. Print Pokedex")
  print("2. Print Pokemon by Name")
  print("3. Print Pokemon by Number")
  print("4. Count Pokemon with Type")
  print("5. Print Average Pokemon Combat Points")
  print("6. Quit")

  





# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def create_pokedex(filename):
  pokedex = []
  file = open(filename, "r")
  
  for pokemon in file:
    pokelist = pokemon.strip().split(",")
    number = int(pokelist[0])               # number
    name = pokelist[1]                      # name
    combat_points = int(pokelist[2])        # hit points
    types = []
    for position in range(3, len(pokelist)):
      types += [pokelist[position]]       # type
    pokedex += [Pokemon(name, number, combat_points, types)]

  file.close()
  return pokedex

# ---------------------------------------

def get_choice(low, high, message):
  legal_choice = False
  while not legal_choice:
      legal_choice = True
      answer = input(message)
      for character in answer:
          if character not in string.digits:
              legal_choice = False
              print("That is not a number, try again.")
              break 
      if legal_choice:
          answer = int(answer)
          if (answer < low) or (answer > high):
              legal_choice = False
              print("That is not a valid choice, try again.")
  return answer

# ---------------------------------------

def main():
  pokedex = create_pokedex("pokedex.txt")
  print(Pokemon)
  choice = 0
  while choice != 6:
      print_menu()
      choice = get_choice(1, 6, "Enter a menu option: ")
      if choice == 1:    
          print_pokedex(pokedex)
      elif choice == 2:
          name = input("Enter a Pokemon name: ").lower()
          lookup_by_name(pokedex, name)
      elif choice == 3:
          number = get_choice(1, 1000, "Enter a Pokemon number: ")
          lookup_by_number(pokedex, number)
      elif choice == 4:
          pokemon_type = input("Enter a Pokemon type: ").lower()
          total_by_type(pokedex, pokemon_type)
      elif choice == 5:
          average_hit_points(pokedex)
      elif choice == 6:
          print("Thank you.  Goodbye!")
      print()

# ---------------------------------------

main()
