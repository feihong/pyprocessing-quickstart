class Walker:
    def __init__(self):
        self.x = floor(width / 2)
        self.y = floor(height / 2)
    
    def show(self):
        stroke(0)
        point(self.x, self.y)
        
    def step(self):
        choice = floor(random(4))
        if choice == 0:
            self.x += 1
        elif choice == 1:
            self.x -= 1
        elif choice == 2:
            self.y += 1
        else:
            self.y -= 1
            
        self.x = constrain(self.x, 0, width-1)
        self.y = constrain(self.y, 0, height-1)

def setup():
    size(640, 240)
    background(255)
    walker = Walker()
    
def draw():
    walker.step()
    walker.show()
