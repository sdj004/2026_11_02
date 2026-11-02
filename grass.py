import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from pico2d import load_image


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self, x, y):
        self.image.draw(400 + x, 30 + y)
        

    def update(self):
        pass
