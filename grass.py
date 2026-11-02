import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from pico2d import load_image


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass
