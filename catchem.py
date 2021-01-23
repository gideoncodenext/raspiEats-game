from sense_emu import SenseHat
from time import sleep
import random

sense = SenseHat()
sense.clear()




# catcher_x = 0

# berry_x = random.randint(0,7)
# berry_y = 0

# score = 0 

r = (255, 0, 0) #red
g = (0, 255, 0) #green
b = (0, 0, 255) #blue
k = (0, 0, 0) #blank
w = (255, 255, 255) #white
c = (0, 255, 255) #cyan
y = (255, 255, 0) #yellow
o = (255, 128, 0) #orange
n = (255, 128, 128) #pink
p = (128, 0, 128) #purple
d = (255, 0, 128) #darkPink
l = (128, 255, 128) #lightGreen

#Intro text or animation
# 3,2,1 countdown 

class Game:
  def __init__(self):
    self.catcher_x = 0
    self.score = 0 
    self.berries = [
      {
        "name": "potato",
        "color": y,
        "pos_x": 0,
        "pos_y": 0,
        "points": 10

      },
      {
        "name": "raspberry",
        "color": r,
        "pos_x": 3,
        "pos_y": 0,
        "points": 3
      },
      {
        "name": "grape",
        "color": p,
        "pos_x": 6,
        "pos_y": 0,
        "points": -3
      }

    ]

    self.berry = random.choice(self.berries)
    self.berry_x = self.berry["pos_x"]
    self.berry_y = self.berry["pos_y"]
    self.berry_color = self.berry["color"]

    self.game_over = False

  def info(self):
    print("Catcher_x = " + str(self.catcher_x))
    print("Berry_x = " + str(self.berry_x))
    print("Berry_y = " + str(self.berry_y))
  
  def move_left(self):
    if self.catcher_x >= 1:
      self.catcher_x -= 1 
    else:
      self.catcher_x = 7
    print("left")

  def move_right(self):
    if self.catcher_x < 7:
      self.catcher_x += 1
    else:
      self.catcher_x = 0
    print("right") 

  def make_berry(self):
    # self.berry_color = random.choice(self.berries)["color"]
    self.berry = random.choice(self.berries)
    self.berry_x = self.berry["pos_x"]
    self.berry_y = self.berry["pos_y"]
    self.berry_color = self.berry["color"]

  def catch(self):
    self.make_berry()
    self.score += self.berry["points"]
    sense.show_message(str(self.score))
    self.catcher_x = 3

  def gameOver(self):
      sense.clear()
      sense.show_message("GG")
      self.game_over = True
      print("Game Over")

  def update(self):
    sense.clear()
    if self.berry_y < 7:
      self.berry_y += 1
      sense.set_pixel(self.berry_x, self.berry_y, self.berry_color)
      print(self.berry_color)
    sense.set_pixel(self.catcher_x, 7, d)

    self.info()


  

  def gameRun(self):
    while self.game_over == False: 
      self.update()
    
      for event in sense.stick.get_events():
        print(event)
      
        if event.action == "pressed" and event.direction == "left":
          self.move_left()
      
        if event.action == "pressed" and event.direction == "right":
          self.move_right()

      if self.catcher_x != self.berry_x and self.berry_y == 7:
        self.gameOver()

      if self.catcher_x == self.berry_x and self.berry_y == 7:
        self.catch()



      
      sleep(1.3)
      
      # if self.catcher_x == self.berry_x and self.berry_y == 7:
      #   self.berry_x = random.randint(0,7)
      #   self.berry_y = 0
      #   print("got it!")
      # elif self.catcher_x != self.berry_x and self.berry_y == 7:
      #   sense.show_message("GG")
      #   sense.clear()
      #   self.game_over = True
        

    self.update()

G = Game()
G.gameRun()

  # def berry_fall():
  #   global berry_y
    # if berry_y < 7:
    #   berry_y += 1