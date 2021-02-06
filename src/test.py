from tdge import *

game = Game(width=500, height=500, title="3D Game Engine Test", show_fps=True)

cube = Cube(size=[10, 10, 10], color=[255, 255, 255], position=[-100, 0, 100])
cube1 = Cube(size=[10, 10, 10], color=[255, 0, 0], position=[100, 0, 100])

display.draw(game, cube)
display.draw(game, cube1)

def code():
    rotate(cube)
    rotate(cube1)

start_game(game, code=code)
