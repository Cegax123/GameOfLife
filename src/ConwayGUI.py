import pygame
from conf import *


class GoLGUI:
    def __init__(self, surf, board, controller):
        self.surf = surf
        self.rows, self.cols = HEIGHT // SCALE, WIDTH // SCALE
        self.rect_board = [[pygame.Rect(SCALE * j, SCALE * i, SCALE, SCALE) for j in range(self.cols)] for i in range(self.rows)]

        self.board = board
        self.controller = controller
        
    def draw(self):
        # Draw board

        for i in range(self.rows):
            for j in range(self.cols):
                if self.board.get_cell_by_position((i, j)).is_live():
                    pygame.draw.rect(self.surf, COLOR_LIVE_CELL, self.rect_board[i][j])

        # Draw grid

        for i in range(self.rows+1):
            pygame.draw.line(self.surf, COLOR_LINE, (0, SCALE * i), (WIDTH, SCALE * i), 2)

        for i in range(self.cols+1):
            pygame.draw.line(self.surf, COLOR_LINE, (SCALE * i, 0), (SCALE * i, HEIGHT), 2)

    def get_pos_clicked(self, mouse_position):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.rect_board[i][j].collidepoint(mouse_position):
                    return (i, j)
        
        return (-1, -1)

    def action_performed(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.controller.quit_game()

            if event.type == pygame.KEYDOWN:
                self.controller.key_pressed(event.key)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()

                if event.button == LEFT_CLICK:
                    pos = self.get_pos_clicked(mouse_position)
                    self.controller.left_clicked_cell_with_pos(pos)

                if event.button == RIGHT_CLICK:
                    pos = self.get_pos_clicked(mouse_position)
                    self.controller.right_clicked_cell_with_pos(pos)
            
