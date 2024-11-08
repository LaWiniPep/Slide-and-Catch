import pygame, simpleGE, random

"""
catch.py
slide and catch game
Alex
"""

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
        self.duck = Duck(self)
        
        self.sprites = [self.duck]
        
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()