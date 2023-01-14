import os
import random
from time import sleep
from rooms import Room, Layout, all_rooms, area_layout, escape, explore, cont



# presentation link in canva.md


def prompt(text: str) -> None:
  print(text)

def ask(text: str) -> str:
  return input(text).strip





    
commands = {
    "directions": ["north", "east", "south","west"],
    "quit": ['q', 'quit'],
    "explore": ['x', 'explore'],
    "escape": ['esc', 'escape'],
    "leave": ['l', 'leave'],
    "restart": ["r", "restart"]}



#print("\033[1m" + "This is bold text!" + "\033[0m")

def game_loop() -> None:
  print("""Welcome to Basecamp Maximum Security Prison. You have been sentenced to 50 years to life for writing messy code. The facility has five main rooms which you are free to move between. 

- Your cell.
- The Laundry
- The Garden
- The Kitchen
- The Gym""")
  
  while True:
    print("\033[9m" + "\n|||||||||||||||||||||||" +"\033[0m" " ¯\_(ツ)_/¯ " + "\033[9m" "||||||||||||||||||||||||\n" + "\033[0m")
   
    
    prompt(f"\nLocation: {area_layout.current_room.name}\n")
    current_room = area_layout.current_room
    print(current_room.description)
    Layout.rooms_adjacent(area_layout, area_layout.current_room)
    print("\n[Explore]")
    print("\n[Restart]")
    print("\n[Quit]")
    command = input(f"\nWhat should you do? \n>  ").lower()
    if command in commands["directions"]:
      if not area_layout.go_to(command):
        prompt(f"\033[0;31m" + "\nYou cannot go that way."+"\033[0m")
        cont()
    elif command in commands["explore"]:
      exploration = explore(current_room)
      # prompt("[Quit]")
      if exploration in commands["escape"]:
        if escape(area_layout.current_room):
          cont()
          os.system("clear")
          command = ask("""\n[Restart]\
[Quit]

> """)
          if command in commands["restart"]:
            area_layout.current_room = all_rooms[0]
            cont()
            os.system("clear")
          elif command in commands["quit"]:
            break
              
      elif exploration in commands["quit"]:
        break
      elif exploration in commands["restart"]:
        area_layout.current_room = all_rooms[0]
        #cont()
        os.system("clear")
        
    # elif command in commands["escape"]:
    #   print("")
    elif command in commands["quit"]:
      break
    # elif command in commands["restart"]:
    #   area_layout.current_room = all_rooms[0]
    #   cont()
    #   os.system("clear")
    elif command in commands["restart"]:
      area_layout.current_room = all_rooms[0]
      cont()
      os.system("clear")
    else:
      prompt(f"\033[0;31m" + "\nI don't understand that command"+"\033[0m")
      sleep(1.2)
    #sleep(10)
    #cont()
    os.system("clear")
      
if __name__ == "__main__":
  game_loop()
  