import random
from dataclasses import dataclass



# Room Class - defines a room's name, desc, and adjacent rooms(if any)
@dataclass
class Room:
  name: str
  description: str
  north: str
  east: str
  south: str
  west: str
  def __init__(self, name, description, north = None, east = None, south = None, west = None):
    self.name = name
    self.north = north
    self.east = east
    self.south = south
    self.west = west
    

# added this one line to get the description print working 
    self.description = description

# only have to define adjacency one way, this helps fill in reverse directions    
    if north:
      north.south = self
    if east:
      east.west = self
    if south:
      south.north = self
    if west:
      west.east = self

# the room decides what other rooms are legal to travel to
  def go_to(self, direction):
    if direction in ["north", "east", "south", "west"]:
      if not self.north and not self.east and not self.west and not self.south:
        return None
      return getattr(self, direction)
    else:
      return None

  def __str__(self):
    return self.name

  

# Takes all of our rooms and outputs a single object to call
class Layout:
    current_room: Room
    rooms: Room

    def __init__(self, current_room: Room, rooms: Room):
        self.current_room = current_room
        self.rooms = rooms

    def go_to(self, direction):
        if next_room := self.current_room.go_to(direction):
            self.current_room = next_room
        return next_room
    
    
# prints rooms that are next to current room
    def rooms_adjacent(self, current_room: Room) -> str:
      if current_room.north:
        print(f"\n[North]: {current_room.north}")
      if current_room.east:
        print(f"\n[East]: {current_room.east}")
      if current_room.south:
        print(f"\n[South]: {current_room.south}")
      if current_room.west:
        print(f"\n[West]: {current_room.west}")

    def print_description(self, current_room: Room) -> str:
      return self.current_room.description



commands = {
    "directions": ["north", "east", "south","west"],
    "quit": ['q', 'quit'],
    "explore": ['x', 'explore'],
    "escape": ['esc', 'escape'],
    "leave": ['l', 'leave']}

def cont() -> str:
  return input("\033[0;32m"+"\nPress Enter to continue... "+"\033[0m")

all_rooms = [prison_cell := Room("Your Cell", """You currently stand in your cell.
It is a standard-looking cell with a bed, sink, and toilet.

Would you like to explore your cell or leave?"""), 
             laundry := Room("Laundry Room", description = """You currently stand in the laundry.
There is a constant hum of machines and thuddunking of spinning wet clothes. 

Would you like to explore the laundry or leave?""", west = prison_cell),
             gym := Room("The Gymnasium", description = """You currently stand in the gym. 
The sticky smell of sweat hangs heavy in the air and is so thick you can feel it as you walk through.

Would you like to explore the gym or leave?""", south = laundry),
             kitchen := Room("The Kitchen", description = """You currently stand in the kitchen.
The smell of slop and three day old bread assults your nose along with the clanging of metal pots and pans.

Would you like to explore the kitchen or leave?""", north = laundry), 
             garden := Room("The Garden", description = """You currently stand in the garden.
The fresh scent of vegetables and dirt fills the air along with the grunts of men working the land. 

# Would you like to explore the garden or leave?""", west = kitchen),
              project_room := Room("Review Room", "You're in a room with all your classmates!", north = garden)]

area_layout = Layout(prison_cell, all_rooms)


#if the user is exploring the room, they can decide to attempt to escape.
def escape(current_room: Room) -> bool:
  magic_num = random.randint(1,100)
  #print(magic_num)
  if magic_num <= 30 and area_layout.current_room.name == "Your Cell":
    print("\nYou spend the next week filing away at the loose bars. Once they are able to move easily, you prepare to escape. During guard change on a moonless night, you squeeze through the gap in your bars and, by some great amount of luck, make it over the fence and off to freedom. " +  "\033[0;32m"+ "\033[1m" + "\nESCAPE SUCCESSFUL" + "\033[0m")
    return True
    
  elif magic_num <= 30 and area_layout.current_room.name == "Laundry Room":
    print("\nYou change into the uniform, which by the grace of God somehow fits and try to leave but the new boss catches you. He gives you lots of work to do in a part of the prison you've never been to. You do a full days work before clocking out and walking right out the front door. "+  "\033[0;32m" + "\033[1m" + "\nESCAPE SUCCESSFUL" + "\033[0m")
    return True
    
  elif magic_num <= 30 and area_layout.current_room.name == "The Kitchen":
    print("\nYou decide to hide in the back of the truck where another delivery's goods are. No one notices you in the back as they close up the truck and you are driven right out of the prison. At the next stop you manage to sneak out of the truck while the delivery men are moving the goods. "+  "\033[0;32m" + "\033[1m" + "\nESCAPE SUCCESSFUL" + "\033[0m")
    return True
    
  elif magic_num <= 30 and area_layout.current_room.name == "The Gymnasium":
    print("""\nYou finally muster up the guts to approach the dirty guard. You threaten to turn him in unless he agrees to smuggle you out. You say you'll throw in some information on a rival coding gang to sweeten the deal. The guard pulls some strings and stages a fight between you and onother inmate. Convincing fake blood and some good acting get you sent to the infirmery where the guard smuggles you out in an ambulance with his EMT co-conspirators. You spill the tea on Basecamp's top code crew and all their dirty dealings after they let you go. A while later you hear on the news that several members of the rival coding gang were charged with smuggling bad code and sabotaging compeditors and consumers. """ + "\033[0;32m"+ "\033[1m" + "\nESCAPE SUCCESSFUL" + "\033[0m")
    return True
    
  elif magic_num <= 30 and area_layout.current_room.name == "The Garden":
    print("\nAs you decend into the dark tunnel you realize this must have been an old underground railroad tunnel. You walk for what feels like forever until at last you come to what looks like a dead end, except....a small breeze brushes across your cheek from above. You carefully push against what you now realize is a wooden hatch. It resists but finally gives way. You climb out and in the distance can barely make out the top edges of the prison. " +"\033[0;32m"+ "\033[1m" + "\nESCAPE SUCCESSFUL" + "\033[0m")
    return True
    
  elif area_layout.current_room.name == "Your Cell":
    print("""You spend the next week filing away at the bars, but a suprise cell check by an apparently competent guard causes you to loose the file, along with any good behavor perks you had accumulated."""+ "\033[0;31m" + "\033[1m" + "\nESCAPE FAILED" + "\033[0m")
    cont()
    area_layout.current_room = prison_cell   
    return  False
  elif area_layout.current_room.name == "Laundry Room":
    print("""You change into the uniform, which by the grace of God somehow fits and try to leave only to be met by the new boss and a guard that knows you. You make a run for it but don't get very far before being tackled. Now you can't go anywhere without supervision and you are definitly aren't allowed in the laundry. You are escorted back to your cell."""+ "\033[0;31m" + "\033[1m" + "\nESCAPE FAILED" + "\033[0m")
    cont()
    area_layout.current_room = prison_cell
    return False
  elif area_layout.current_room.name == "The Kitchen":
    print("""You never did like hiding. You hop in the cab and start the engine! Too bad that you're a horrible driver. You crash into the prison wall because you accidently put the truck into reverse. Guards and delivery men pour out of the building and you are surrounded. Maybe you should have gotten your drivers licence. You are escorted back to your cell. 
""" +"\033[0;31m"+ "\033[1m" + "\nESCAPE FAILED" + "\033[0m")
    cont()
    area_layout.current_room = prison_cell    
    return False
  elif area_layout.current_room.name == "The Gymnasium":
    print("""You finally muster up the guts to approach the dirty guard. You threaten to turn him in unless he agrees to smuggle you out. Unfortunatly for you it seems the talk at the gym was a set up by a rival coding gang. The guard quickly escorts you to the warden and it looks like you'll be in solitary confinement for a while. You are escorted back to your cell. 
""" +"\033[0;31m"+ "\033[1m" + "\nESCAPE FAILED" + "\033[0m")
    cont()
    area_layout.current_room = prison_cell
    return False
  elif area_layout.current_room.name == "The Garden":
    print("""You begin the decent into the tunnel but about 10 feet in you hear the tale-tell rattling of a rattlesnake. Having a healthy fear of snakes you turn and run back out of the tunnel, unfortunatly straight into a patrolling guard. After a good chewing out, you are escorted back to your cell. 
"""+ "\033[0;31m"+ "\033[1m" + "\nESCAPE FAILED" + "\033[0m")
    cont()
    
    area_layout.current_room = prison_cell
    return False


#describes the room in greater detail, and gives user opportunity to escape
def explore(current_room: Room) -> str:
  if area_layout.current_room.name == "Your Cell":
    userinput = input("""\nWhile poking through your cell you find a small file under the matress. You wonder how the guards haven't discovered it during routine cell checks. You remember that handfull of bars on your exterior window that might move with a little bit of help. Is this it? Is this your chance for escape?

[Escape]
[Leave]
> """).lower()
  if area_layout.current_room.name == "Laundry Room":
    userinput = input("""\nWhile digging through the laundry you find an old guard's uniform. A few small details have changed but otherwise it looks very similar to the current uniform. Is this it? Is this your chance for escape?

[Escape]
[Leave]

> """).lower()
  if area_layout.current_room.name == "The Kitchen":
    userinput = input("""\nWhile working in the kitchen you notice that the food delivery truck has been left unsupervised. You look around to see if anyone is watching the truck and decide to check it out. You find that the back of the truck is unlocked and the keys are still in the ignition. Is this it? Is this your chance for escape?
    
[Escape]
[Leave]

> """).lower()
  if area_layout.current_room.name == "The Gymnasium":
    userinput = input("""\nWhile working out in the gym you overhear some inmates talking about a dirty guard that will help inmates for a price. Further listening reveals the guard to be one that's usually gaurding your block. Is this it? Is this your chance for escape?
    
[Escape]
[Leave]

> """).lower()
  if area_layout.current_room.name == "The Garden":
    userinput = input("""\nWhile walking through the garden you see a glint of metal under a pile of leaves. Further inspection reveals a lid of some kind that, when lifted, leads to a mystery tunnel. It's dark and you can't see very far down. Is this it? Is this your chance for escape?
    
[Escape]
[Leave]

> """).lower()
  if userinput not in commands:
    print("\033[0;31m" + "I don't understand." + "\033[0m")
    cont()
  else:
    return userinput

# BLACK = "\033[0;30m"
#     RED = "\033[0;31m"
#     GREEN = "\033[0;32m"
#     BROWN = "\033[0;33m"
#     BLUE = "\033[0;34m"
#     PURPLE = "\033[0;35m"
#     CYAN = "\033[0;36m"
#     LIGHT_GRAY = "\033[0;37m"
#     DARK_GRAY = "\033[1;30m"
#     LIGHT_RED = "\033[1;31m"
#     LIGHT_GREEN = "\033[1;32m"
#     YELLOW = "\033[1;33m"
#     LIGHT_BLUE = "\033[1;34m"
#     LIGHT_PURPLE = "\033[1;35m"
#     LIGHT_CYAN = "\033[1;36m"
#     LIGHT_WHITE = "\033[1;37m"
#     BOLD = "\033[1m"
#     FAINT = "\033[2m"
#     ITALIC = "\033[3m"
#     UNDERLINE = "\033[4m"
#     BLINK = "\033[5m"
#     NEGATIVE = "\033[7m"
#     CROSSED = "\033[9m"
#     END = "\033[0m"