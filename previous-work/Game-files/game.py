import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math
from Vector import Vector

#link to CodeSkulptor: https://py3.codeskulptor.org/#user306_IVUxy1Clvn_3.py

class Game:
    SPRITESHEET_URL = "http://personal.rhul.ac.uk/zjac/006/edit2.png"   
    BORDER_URL = "http://personal.rhul.ac.uk/zjac/006/border5.png" 
    BACKGROUND_URL = "http://personal.rhul.ac.uk/zjac/006/background4.png" 
    CANVAS_WIDTH = 400
    CANVAS_HEIGHT = 600
    WALL_THICKNESS = 10

    BALL_POS = Vector(100,300)
    BALL_VEL = Vector(5,2)
    BALL_POS2 = Vector(300,300)
    BALL_VEL2 = Vector(5,2)
    SCORE = 0
    LIVES = 3

class LRWall:
    def __init__(self, x, border, color):
        self.x = x
        self.border = border
        self.color = color
        self.normal = Vector(1,0)
        self.edge_r = x + self.border
        self.edge_l = x - self.border

    def draw(self, canvas):
        canvas.draw_line((self.x, 0),
                         (self.x, Game.CANVAS_HEIGHT),
                         self.border*2+1,
                         self.color)

    def hitL(self, ball):
        h = (ball.offset_l() <= self.edge_r)
        return h
    
    def hitR(self, ball):
        h = (ball.offset_r() >= self.edge_l)
        return h

class TBWall:
    def __init__(self, x, y, border, color):
        self.x = x
        self.y = y
        self.border = border
        self.color = color
        self.normal = Vector(0,1)
        self.edge_r = x + self.border
        self.edge_l = x - self.border
        

    def draw(self, canvas):
        canvas.draw_line((self.x, self.y),
                         (Game.CANVAS_WIDTH, self.y),
                         self.border*2+1,
                         self.color)
        
    def hitT(self, ball):
        h = (ball.offset_t() <= self.edge_r)
        return h
             
        
class Block:
    def __init__(self, pos1, pos2, size, colour):
        self.pos1 = pos1
        self.pos2 = pos2
        self.size = size
        self.colour = colour
        
        self.normal = Vector(0,1)
        self.top_edge = pos2.get_y()
        
    def draw(self, canvas):
        canvas.draw_polygon([self.pos1.get_p(),self.pos2.get_p()],self.size,self.colour,) 
        
    def hit(self, ball):
        h = (ball.offset_b() <= (self.top_edge+20)
        and ball.pos.get_x() >= self.pos1.get_x()
        and ball.pos.get_x() <= (self.pos1.get_x()+40))
        return h 
        

class Ball:
    def __init__(self, pos, vel, radius, border, color):
        self.pos = pos
        self.vel = vel
        self.radius = radius
        self.border = 1
        self.color = color

    def offset_l(self):
        return self.pos.x - self.radius
    
    def offset_r(self):
        return self.pos.x + self.radius
    
    def offset_t(self):
        return self.pos.y - self.radius
    
    def offset_b(self):
        return self.pos.y + self.radius

    def update(self):
        self.pos.add(self.vel)

    def draw(self, canvas):
        canvas.draw_circle(self.pos.get_p(),
                           self.radius,
                           self.border,
                           self.color,
                           self.color)

    def bounce(self, normal):
        self.vel.reflect(normal)

        
class Keyboard:
    def __init__(self, sprite):
        self.right = False
        self.left = False
        self.sprite = sprite

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = True
            self.sprite.frame_index = [0, 2]
        if key == simplegui.KEY_MAP['left']:
            self.left = True
            self.sprite.frame_index = [0, 1]

    def keyUp(self, key):
        self.sprite.frame_index = [0, 0]
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        if key == simplegui.KEY_MAP['left']:
            self.left = False
            
class Border:
    def __init__(self):
        self.img = simplegui.load_image(Game.BORDER_URL)
        
    def draw(self, canvas):
        canvas.draw_image(self.img, (200, 300), (400, 600), (200, 300), (400, 600))
        
class Background:
    def __init__(self):
        self.img = simplegui.load_image(Game.BACKGROUND_URL)
        
    def draw(self, canvas):
        canvas.draw_image(self.img, (200, 300), (400, 600), (200, 300), (400, 600))
        
        
class Player:
    def __init__(self, columns, rows, clock):
        self.img = simplegui.load_image(Game.SPRITESHEET_URL)
        self.width = 1280
        self.height = 720
        self.rows = rows
        self.columns = columns
        self.clock = clock
        self.centre_dest = Vector(Game.CANVAS_WIDTH / 2 , Game.CANVAS_HEIGHT-25)
        self.dims_dest = (120, 240)
        self.transitionTime = 20
        self.vel = Vector()

        self.frame_width = self.width / columns
        self.frame_height = self.height / rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2

        self.frame_index = [0, 0]

    def draw(self, canvas):
        # makes sure the frame moves to the next when clock time modulo frame duration
        # are equal to 0
        self.clock.tick()
        if self.clock.transition(self.transitionTime):
            self.next_frame()
        
        # given the spritesheet, where is the centre of the cell that you want to draw
        centre_source = (self.frame_width * self.frame_index[0] + self.frame_centre_x,
                        self.frame_height * self.frame_index[1] + self.frame_centre_y,
                        )
        
        # how big is the cell that is being drawn
        dims_source = (self.frame_width, self.frame_height)
        
        # x and y coordinates of where to put the image on the screen
        #centre_dest = (150, 50)

        # how big the sprite should be on the screen
        #dims_dest = (120, 240)

        canvas.draw_image(self.img, centre_source, dims_source, self.centre_dest.get_p(), self.dims_dest)
  

    def next_frame(self):
        # if the number of columns is 6, as soon as it increments to frame 6,
        # it will reset to 0 
        # everytime the column index loops back to 0, the row index is incremented
        # using modulo for number of rows so that it wraps back to the first row
        self.frame_index[0] = (self.frame_index[0] + 1) % self.columns

    def update(self):
        self.centre_dest.add(self.vel)
        self.vel.multiply(0.60)
        
        
class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

        self.vel = Vector()
        self.normal = Vector(0,1)
        self.top_edge = point1.get_y() 

    def draw(self, canvas): 
        canvas.draw_line(self.point1.get_p(), self.point2.get_p(), 5, 'red')

    def hit(self, ball):
        h = (ball.offset_b() >= self.top_edge
            and ball.pos.get_x() >= self.point1.get_x()
            and ball.pos.get_x() <= self .point2.get_x())
        return h

    def update(self):
        self.point1.add(self.vel)
        self.point2.add(self.vel)
        self.vel.multiply(0.60)
        

class Clock:
    def __init__(self):
        self.time = 0

    def tick(self):
        self.time += 1
    
    def transition(self, frame_duration):
        if self.time % frame_duration == 0:
            return True
        else:
            return False
    
        
class Interaction:
    def __init__(self, Lwall, Rwall, Twall, ball, ball2, sprite, keyboard,
                        blocks, line, border, background):
        self.ball = ball
        self.ball2 = ball2
        self.Lwall = Lwall
        self.Rwall = Rwall
        self.Twall = Twall
        self.in_collision = False
        self.sprite = sprite
        self.keyboard = keyboard
        self.blocks = blocks
        self.line = line
        self.touch_bottom = False
        self.border = border
        self.background = background
        
    def update(self):
        global LIVES
        global SCORE
        global twoBalls
        if self.Lwall.hitL(self.ball):
            if not self.in_collision:
                self.ball.bounce(self.Lwall.normal)
                self.in_collision = True
        if self.Lwall.hitL(self.ball2):
            if not self.in_collision:
                self.ball2.bounce(self.Lwall.normal)
                self.in_collision = True        
                
        if self.Rwall.hitR(self.ball):
            if not self.in_collision:
                self.ball.bounce(self.Rwall.normal)
                self.in_collision = True
        if self.Rwall.hitR(self.ball2):
            if not self.in_collision:
                self.ball2.bounce(self.Rwall.normal)
                self.in_collision = True
                
        if self.Twall.hitT(self.ball):
            if not self.in_collision:
                self.ball.bounce(self.Twall.normal)
                self.in_collision = True
        if self.Twall.hitT(self.ball2):
            if not self.in_collision:
                self.ball2.bounce(self.Twall.normal)
                self.in_collision = True    
                
        if self.line.hit(self.ball):
            if not self.in_collision:
                self.ball.bounce(self.line.normal)
                self.in_collision = True
                
        if self.line.hit(self.ball2):
            if not self.in_collision:
                self.ball2.bounce(self.line.normal)
                self.in_collision = True 
                
        for block in self.blocks:
            if block.hit(self.ball):
                Game.SCORE += 5
                if block == block50:
                    self.line.point1 = Vector(Game.CANVAS_WIDTH/2 - 35, 555)
                    self.line.point2 = Vector(Game.CANVAS_WIDTH/2 + 35, 555)
                    self.line.top_edge = self.line.point1.get_y() 
                    self.sprite.centre_dest = Vector(Game.CANVAS_WIDTH/2, Game.CANVAS_HEIGHT - 25)
                    self.sprite.dims_dest = (80, 160)
                if block == block29:
                    self.line.point1 = Vector(Game.CANVAS_WIDTH/2 - 22, 563)
                    self.line.point2 = Vector(Game.CANVAS_WIDTH/2 + 22, 563)
                    self.line.top_edge = self.line.point1.get_y() 
                    self.sprite.centre_dest = Vector(Game.CANVAS_WIDTH/2, Game.CANVAS_HEIGHT - 25)
                    self.sprite.dims_dest = (50, 100)  
                if not self.in_collision:
                    self.ball.bounce(block.normal)
                    self.in_collision = True
                    blocknum = blocks.index(block)
                    blocks.pop(blocknum)
            if block.hit(self.ball2):
                Game.SCORE += 5
                if block == block50:
                    self.line.point1 = Vector(Game.CANVAS_WIDTH/2 - 35, 555)
                    self.line.point2 = Vector(Game.CANVAS_WIDTH/2 + 35, 555)
                    self.line.top_edge = self.line.point1.get_y() 
                    self.sprite.centre_dest = Vector(Game.CANVAS_WIDTH/2, Game.CANVAS_HEIGHT - 25)
                    self.sprite.dims_dest = (80, 160)
                if block == block29:
                    self.line.point1 = Vector(Game.CANVAS_WIDTH/2 - 22, 563)
                    self.line.point2 = Vector(Game.CANVAS_WIDTH/2 + 22, 563)
                    self.line.top_edge = self.line.point1.get_y() 
                    self.sprite.centre_dest = Vector(Game.CANVAS_WIDTH/2, Game.CANVAS_HEIGHT - 25)
                    self.sprite.dims_dest = (50, 100)  
                if not self.in_collision:
                    self.ball2.bounce(block.normal)
                    self.in_collision = True
                    blocknum = blocks.index(block)
                    blocks.pop(blocknum)
                    
               
        else:
            self.in_collision = False
            
        if self.keyboard.right:
            self.sprite.vel.add(Vector(1, 0))
            self.line.vel.add(Vector(1, 0))
        if self.keyboard.left:
            self.sprite.vel.add(Vector(-1, 0))
            self.line.vel.add(Vector(-1, 0))
        
        if self.ball.pos.get_y() >= Game.CANVAS_HEIGHT:
            if not self.touch_bottom:
                self.ball.pos = Vector(100,300)
                self.ball.vel = Vector(5,2)
                self.touch_bottom = True
                Game.LIVES  -= 1
        
        if twoBalls == True:
            if self.ball.pos.get_y() >= Game.CANVAS_HEIGHT:
                if not self.touch_bottom:
                    self.ball.pos = Vector(100,300)
                    self.ball.vel = Vector(5,2)
                    self.touch_bottom = True
                    Game.LIVES  -= 1
            if self.ball2.pos.get_y() >= Game.CANVAS_HEIGHT:
                if not self.touch_bottom:
                    self.ball2.pos = Vector(100,300)
                    self.ball2.vel = Vector(5,2)
                    self.touch_bottom = True
                    Game.LIVES  -= 1
            else:
                self.touch_bottom = False
            self.ball2.update()
        else:
            self.touch_bottom = False
            
        if Game.LIVES == 0:
            frame.set_draw_handler(welcomeScreen)
            Game.LIVES = 3
            Game.SCORE = 0
        if len(blocks) == 0:
            frame.set_draw_handler(welcomeScreen)
            
        self.ball.update()
    
    def draw(self, canvas):
        self.update()
        self.sprite.update()
        self.line.update()
        self.background.draw(canvas)
        self.ball.draw(canvas)       
        self.sprite.draw(canvas)
        
        self.border.draw(canvas)
        
        canvas.draw_text('Score: ' + str(Game.SCORE), [30, 30], 20, 'White')
        canvas.draw_text('Lives: ' + str(Game.LIVES), [300, 30], 20, 'White')
        for block in self.blocks:
            block.draw(canvas)
        if twoBalls == True:
            self.ball2.draw(canvas)
#All block positions
block1 = Block(Vector(60, 60), Vector(60, 70), 40, 'red')
block2 = Block(Vector(102, 60), Vector(102, 70), 40, 'red')
block3 = Block(Vector(144, 60), Vector(144, 70), 40, 'red')
block4 = Block(Vector(186, 60), Vector(186, 70), 40, 'red')
block5 = Block(Vector(228, 60), Vector(228, 70), 40, 'red')
block6 = Block(Vector(270, 60), Vector(270, 70), 40, 'red')
block7 = Block(Vector(312, 60), Vector(312, 70), 40, 'red')
block8 = Block(Vector(354, 60), Vector(354, 70), 40, 'red')

block9 = Block(Vector(60, 72), Vector(60, 82), 40, 'red')
block10 = Block(Vector(102, 72), Vector(102, 82), 40, 'red')
block11 = Block(Vector(144, 72), Vector(144, 82), 40, 'red')
block12 = Block(Vector(186, 72), Vector(186, 82), 40, 'red')
block13 = Block(Vector(228, 72), Vector(228, 82), 40, 'red')
block14 = Block(Vector(270, 72), Vector(270, 82), 40, 'red')
block15 = Block(Vector(312, 72), Vector(312, 82), 40, 'red')
block16 = Block(Vector(354, 72), Vector(354, 82), 40, 'red')

block17 = Block(Vector(60, 84), Vector(60, 94), 40, 'orange')
block18 = Block(Vector(102, 84), Vector(102, 94), 40, 'orange')
block19 = Block(Vector(144, 84), Vector(144, 94), 40, 'orange')
block20 = Block(Vector(186, 84), Vector(186, 94), 40, 'orange')
block21 = Block(Vector(228, 84), Vector(228, 94), 40, 'orange')
block22 = Block(Vector(270, 84), Vector(270, 94), 40, 'orange')
block23 = Block(Vector(312, 84), Vector(312, 94), 40, 'orange')
block24 = Block(Vector(354, 84), Vector(354, 94), 40, 'orange')

block25 = Block(Vector(60, 96), Vector(60, 106), 40, 'orange')
block26 = Block(Vector(102, 96), Vector(102, 106), 40, 'orange')
block27 = Block(Vector(144, 96), Vector(144, 106), 40, 'orange')
block28 = Block(Vector(186, 96), Vector(186, 106), 40, 'orange')
block29 = Block(Vector(228, 96), Vector(228, 106), 40, 'orange')
block30 = Block(Vector(270, 96), Vector(270, 106), 40, 'orange')
block31 = Block(Vector(312, 96), Vector(312, 106), 40, 'orange')
block32 = Block(Vector(354, 96), Vector(354, 106), 40, 'orange')

block33 = Block(Vector(60, 108), Vector(60, 118), 40, 'green')
block34 = Block(Vector(102, 108), Vector(102, 118), 40, 'green')
block35 = Block(Vector(144, 108), Vector(144, 118), 40, 'green')
block36 = Block(Vector(186, 108), Vector(186, 118), 40, 'green')
block37 = Block(Vector(228, 108), Vector(228, 118), 40, 'green')
block38 = Block(Vector(270, 108), Vector(270, 118), 40, 'green')
block39 = Block(Vector(312, 108), Vector(312, 118), 40, 'green')
block40 = Block(Vector(354, 108), Vector(354, 118), 40, 'green')

block41 = Block(Vector(60, 120), Vector(60, 130), 40, 'green')
block42 = Block(Vector(102, 120), Vector(102, 130), 40, 'green')
block43 = Block(Vector(144, 120), Vector(144, 130), 40, 'green')
block44 = Block(Vector(186, 120), Vector(186, 130), 40, 'green')
block45 = Block(Vector(228, 120), Vector(228, 130), 40, 'green')
block46 = Block(Vector(270, 120), Vector(270, 130), 40, 'green')
block47 = Block(Vector(312, 120), Vector(312, 130), 40, 'green')
block48 = Block(Vector(354, 120), Vector(354, 130), 40, 'green')

block49 = Block(Vector(60, 132), Vector(60, 142), 40, 'yellow')
block50 = Block(Vector(102, 132), Vector(102, 142), 40, 'yellow')
block51 = Block(Vector(144, 132), Vector(144, 142), 40, 'yellow')
block52 = Block(Vector(186, 132), Vector(186, 142), 40, 'yellow')
block53 = Block(Vector(228, 132), Vector(228, 142), 40, 'yellow')
block54 = Block(Vector(270, 132), Vector(270, 142), 40, 'yellow')
block55 = Block(Vector(312, 132), Vector(312, 142), 40, 'yellow')
block56 = Block(Vector(354, 132), Vector(354, 142), 40, 'yellow')

block57 = Block(Vector(60, 144), Vector(60, 154), 40, 'yellow')
block58 = Block(Vector(102, 144), Vector(102, 154), 40, 'yellow')
block59 = Block(Vector(144, 144), Vector(144, 154), 40, 'yellow')
block60 = Block(Vector(186, 144), Vector(186, 154), 40, 'yellow')
block61 = Block(Vector(228, 144), Vector(228, 154), 40, 'yellow')
block62 = Block(Vector(270, 144), Vector(270, 154), 40, 'yellow')
block63 = Block(Vector(312, 144), Vector(312, 154), 40, 'yellow')
block64 = Block(Vector(354, 144), Vector(354, 154), 40, 'yellow')

#List of blocks
blocks = [
        block1, block2, block3, block4, block5, block6, block7, block8,
        block9, block10, block11, block12, block13, block14, block15, block16,
        block17, block18, block19, block20, block21, block22, block23, block24,
        block25, block26, block27, block28, block29, block30, block31, block32,
        block33, block34, block35, block36, block37, block38, block39, block40,
        block41, block42, block43, block44, block45, block46, block47, block48,
        block49, block50, block51, block52, block53, block54, block55, block56,
        block57, block58, block59, block60, block61, block62, block63, block64        
        ]

b = Ball(Game.BALL_POS, Game.BALL_VEL, 10, 50, 'pink')
b2 = Ball(Game.BALL_POS2, Game.BALL_VEL2, 10, 50, 'pink')
twoBalls = False
border = Border()


Lw = LRWall(0, Game.WALL_THICKNESS, 'red')
Rw = LRWall(Game.CANVAS_WIDTH, Game.WALL_THICKNESS, 'red')
Tw = TBWall(0, 0, Game.WALL_THICKNESS, 'green')

clock = Clock()

background = Background()
sheet = Player(5, 3, clock)

line = Line(Vector(Game.CANVAS_WIDTH/2 - 53, 545), 
            Vector(Game.CANVAS_WIDTH/2 + 53, 545))

kbd = Keyboard(sheet)


def startGame():
    i = Interaction(Lw, Rw, Tw, b, b2, sheet, kbd, blocks, line, border, background)
    frame.set_draw_handler(i.draw)
def ballTwo():
    global twoBalls
    twoBalls = True
    i = Interaction(Lw, Rw, Tw, b, b2, sheet, kbd, blocks, line, border, background)
    frame.set_draw_handler(i.draw)
def welcomeScreen(canvas):
    frame.set_canvas_background('Black')
    welcome = "Welcome To Brick Breaker!"
    score = "Get points by hitting blocks with the ball"
    instructions = "Use left and right arrows to move your paddle"
    life = "You have 3 lives, once they are gone you lose!"
    start = "To start the game click the button"
    canvas.draw_text(welcome, [6,130], 35, "Red")
    canvas.draw_text(score, [40,190], 20, "White")
    canvas.draw_text(instructions, [20,240], 20, "White")
    canvas.draw_text(life, [20,290], 20, "White")
    canvas.draw_text(start, [65,340], 20, "White")

    canvas.draw_line([0,0], [400,0], 5,  "Red")
    canvas.draw_line([0,40], [400,40], 5,  "Red")
    canvas.draw_line([0,80], [400,80], 5,  "Red")
    canvas.draw_line([20,0], [20,40], 5,  "Red")
    canvas.draw_line([100,0], [100,40], 5,  "Red")
    canvas.draw_line([180,0], [180,40], 5,  "Red")
    canvas.draw_line([260,0], [260,40], 5,  "Red")
    canvas.draw_line([340,0], [340,40], 5,  "Red")
    canvas.draw_line([60,40], [60,80], 5,  "Red")
    canvas.draw_line([140,40], [140,80], 5,  "Red")    
    canvas.draw_line([220,40], [220,80], 5,  "Red")
    canvas.draw_line([300,40], [300,80], 5,  "Red")
    canvas.draw_line([380,40], [380,80], 5,  "Red")
    
    canvas.draw_line([0,520], [400,520], 5,  "Red")
    canvas.draw_line([0,560], [400,560], 5,  "Red")
    canvas.draw_line([0,600], [400,600], 5,  "Red")
    canvas.draw_line([20,520], [20,560], 5,  "Red")
    canvas.draw_line([100,520], [100,560], 5,  "Red")
    canvas.draw_line([180,520], [180,560], 5,  "Red")
    canvas.draw_line([260,520], [260,560], 5,  "Red")
    canvas.draw_line([340,520], [340,560], 5,  "Red")
    canvas.draw_line([60,560], [60,600], 5,  "Red")
    canvas.draw_line([140,560], [140,600], 5,  "Red")    
    canvas.draw_line([220,560], [220,600], 5,  "Red")
    canvas.draw_line([300,560], [300,600], 5,  "Red")
    canvas.draw_line([380,560], [380,600], 5,  "Red")
    
frame = simplegui.create_frame("Block Game", Game.CANVAS_WIDTH, Game.CANVAS_HEIGHT)

button = frame.add_button("Click here to start!", startGame)
button = frame.add_button("Two Balls!", ballTwo)
frame.set_draw_handler(welcomeScreen)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)

frame.start()