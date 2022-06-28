from Cell import Cell


class Board:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (-1, -1), (-1, 1), (1, -1)]

    def __init__(self, rows, cols, limited_by_wall=True):
        self.rows = rows
        self.cols = cols
        self.limited_by_wall = limited_by_wall

        self.cell_board = [[Cell() for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                self.set_neighbors_to_cell(i, j)

    def change_limited_by_wall(self):
        self.limited_by_wall = not self.limited_by_wall
        self.update_neighbors()

    def update_neighbors(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cell_board[i][j].clear_neighbors()

                self.set_neighbors_to_cell(i, j)

    def set_neighbors_to_cell(self, x, y):
        for dx, dy in Board.directions:
            nx = x + dx
            ny = y + dy

            if not self.limited_by_wall:
                nx = (nx + self.rows) % self.rows
                ny = (ny + self.cols) % self.cols

            if not self.valid_position((nx, ny)): continue

            self.get_cell_by_position((x, y)).add_neighbor(self.get_cell_by_position((nx, ny)))

    def move_to_next_iteration(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cell_board[i][j].update_next_status()

        for i in range(self.rows):
            for j in range(self.cols):
                self.cell_board[i][j].move_to_next_status()

    def valid_position(self, pos):
        return 0 <= pos[0] < self.rows and 0 <= pos[1] < self.cols

    def revive_cell_by_position(self, pos):
        if not self.valid_position(pos):
            return

        self.get_cell_by_position(pos).revive()

    def kill_cell_by_position(self, pos):
        if not self.valid_position(pos):
            return

        self.get_cell_by_position(pos).kill()

    def get_cell_by_position(self, pos):
        return self.cell_board[pos[0]][pos[1]]

    def clear(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cell_board[i][j].kill()
