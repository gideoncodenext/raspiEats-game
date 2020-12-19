from sense_hat import SenseHat
import time
import random

sense = SenseHat()
sense.clear()

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

colors = [g, b, k, w, c, y, o, n, p, d, l]


#new code

class Game:
    ### initializes the class
    def __init__(self):
      ### calling our important variables
      self.score = 0
      self.player_color = d
      self.player_x = 0
      self.player_y = 0
      self.food_x = 6
      self.food_y = 6
      self.is_hungry = True
    
    def down(self):
        if self.player_y <7:
            self.player_y += 1
            print("y:" + str(self.player_y))

    def up(self):
        if self.player_y > 0:
            self.player_y -= 1
            print("y:" + str(self.player_y))
    
    def right(self):
        if self.player_x <7:
            self.player_x += 1
            print("x:" + str(self.player_x))
            
    def left(self):
        if self.player_x > 0:
            self.player_x -= 1
            print("x:" + str(self.player_x))

    def middle(self):
        # sense.clear()
        self.player_color = random.choice(colors)
        sense.set_pixel(self.player_x, self.player_y, self.player_color)
        print("press")

    def update(self):
        sense.clear()
        sense.set_pixel(self.player_x,self.player_y, self.player_color)
        sense.set_pixel(self.food_x,self.food_y, l)

    def reset(self):
        sense.clear()
        self.player_x = random.randint(0,7)
        self.player_y = random.randint(0,7)
        same_spot = True
        while same_spot:
            self.food_x = random.randint(0,7)
            self.food_y = random.randint(0,7)
            if self.player_x != self.food_x and self.player_y != self.food_y:
                same_spot = False
                break
            sense.set_pixel(self.player_x, self.player_y, y)
            sense.set_pixel(self.food_x, self.food_y, g)
            print("reset")
    
    def run(self):
        self.is_hungry = True
        self.update()
        while self.is_hungry:
            for event in sense.stick.get_events():
                # print(event)
        
                if event.direction == "down" and event.action =="released":
                    print("down")
                    self.down()
                    self.update()
                elif event.direction == "up" and event.action == "released":
                    print("up")
                    self.up()
                    self.update()

                elif event.direction == "right" and event.action =="released":
                    
                    print("right")
                    self.right()
                    self.update()
                elif event.direction == "left" and event.action =="released":
                    print("left")
                    self.left()
                    self.update()
                
                elif event.direction == "middle" and event.action =="pressed":
                    # print("press")
                    self.middle()
                    # self.update()
                
               
                # elif self.player_color == l and self.player_x == self.food_x and self.food_y ==self.player_y:
                #     sense.show_message("VERY CLEVER")
                #     self.player_color = d
                #     self.player_x = random.choice(range(8))
                #     self.player_y = random.choice(range(8))
                #     self.food_x = random.choice(range(8))
                #     self.food_y = random.choice(range(8))
                #     self.run()

                elif self.player_x == self.food_x and self.food_y == self.player_y:
                    self.score += 1
                    sense.show_letter(str(self.score))
                    time.sleep(.5)
                    
                    self.reset()


                elif self.player_color == l and self.player_x == self.food_x and self.food_y ==self.player_y:
                    sense.show_message("VERY CLEVER")
                    self.score = 10
                    sense.show_letter(str(self.score))
                    self.player_color = d

                    self.player_x = random.choice(range(8))
                    self.player_y = random.choice(range(8))
                    self.food_x = random.choice(range(8))
                    self.food_y = random.choice(range(8))
                    self.run()


                    


                # elif self.player_x == self.food_x and self.food_y == self.player_y:
                #     sense.show_message("GAME OVER!")
                #     self.is_hungry = False

                # elif self.player_x == self.food_x and self.food_y ==self.player_y and self.player_color == l:
                #     sense.show_message("VERY CLEVER")
                    
                


    

# my_game = Game()
# my_game.run()


#old code
#variables for player and food position
"""
player_x = 0
player_y = 0
sense.set_pixel(player_x, player_y,d)

food_x = 6
food_y = 6
sense.set_pixel(food_x, food_y, l)


is_hungry = True

def down():
    global player_y
    if player_y <7:
        player_y += 1
        print("y:" + str(player_y))


def update():
    sense.clear()
    sense.set_pixel(player_x,player_y, d)
    sense.set_pixel(food_x,food_y, l)

while is_hungry:
    for event in sense.stick.get_events():
        # print(event)

        if event.direction == "down" and event.action == "released":
            print("down")
            down()
        update()
"""
