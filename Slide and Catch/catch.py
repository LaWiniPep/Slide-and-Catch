import pygame, simpleGE, random

"""
catch.py
slide and catch game
Alex
"""

class Egg(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Egg.png")
        self.setSize(35,25)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
        
    def reset(self):
        #move it to the top
        self.y = 10
        
        #x is random 0 - scrren width
        self.x = random.randint(0, self.screenWidth)
        
        #dy is random minSpeed to maxSpeed
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
        
class Duck(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Duck.png")
        self.setSize(80,50)
        self.position = (250, 350)
        self.moveSpeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Olympic.jpg")
        
        self.sndEgg = simpleGE.Sound("Quack.wav")
        self.numEggs = 6
        
        self.duck = Duck(self)
        
        self.eggs = []
        
        for i in range(self.numEggs):
            self.eggs.append(Egg(self))
        
        self.sprites = [self.duck,
                        self.eggs]
    def process(self):
        for egg in self.eggs:
            if egg.collidesWith(self.duck):
                egg.reset()
                self.sndEgg.play()
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()