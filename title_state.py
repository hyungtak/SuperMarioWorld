import game_framework
import main_state
from pico2d import *


name = "TitleState"
image = None
def enter():
    global image
    image = load_image('resource/title.png')

