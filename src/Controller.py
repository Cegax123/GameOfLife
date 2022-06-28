import pygame
from ConwayGUI import GUI


class Controller:
    def __init__(self, board, WIN, game):
        self.board = board
        self.gui = GUI(WIN, board, self)
        self.game = game

    def get_gui(self):
        return self.gui

    def move_board_to_next_iteration(self):
        self.board.move_to_next_iteration()

    def quit_game(self):
        self.game.quit_game()

    def key_pressed(self, key):
        if key == pygame.K_ESCAPE:
            self.quit_game()

        elif key == pygame.K_SPACE:
            self.game.change_paused_status()

        elif key == pygame.K_a:
            self.board.change_limited_by_wall()

        elif key == pygame.K_c:
            self.board.clear()
    
    def left_clicked_cell_with_pos(self, pos):
        self.board.revive_cell_by_position(pos)

    def right_clicked_cell_with_pos(self, pos):
        self.board.kill_cell_by_position(pos)
