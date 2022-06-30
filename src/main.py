import pygame 
from conf import *
from Board import Board
from Controller import Controller

pygame.display.set_caption("Conway's Game of Life")


class Game:
    def __init__(self):
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.running_game = True
        self.paused = True

        self.board = Board(HEIGHT // SCALE, WIDTH // SCALE)
        self.controller = Controller(self.board, self.WIN, self)

    def run(self):
            
        while self.running_game:
            self.clock.tick(FPS)
            self.controller.action_performed_in_view(pygame.event.get())

            if not self.paused:
                self.controller.move_board_to_next_iteration()

            self.WIN.fill(COLOR_BG)
            self.controller.draw_game()

            pygame.display.update()
            
        pygame.quit()

    def is_paused(self):
        return self.paused

    def quit_game(self):
        self.running_game = False

    def change_paused_status(self):
        self.paused = not self.paused


if __name__ == "__main__":
    game = Game()
    game.run()
