from gui import MyGUI
from game import Game

if __name__ == '__main__':
    gui = MyGUI(None)
    game = Game(gui)
    gui.game = game
    gui.initialize_game_gui()
    gui.run_root()