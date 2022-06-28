from enum import Enum


class Cell:
    def __init__(self):
        self.neighbors = []
        self.status = CellStatus.DEAD
        self.next_status = None

    def is_live(self):
        return self.status == CellStatus.LIVE

    def is_dead(self):
        return self.status == CellStatus.DEAD

    def revive(self):
        self.status = CellStatus.LIVE

    def kill(self):
        self.status = CellStatus.DEAD

    def number_of_live_neighbors(self):
        live_neighbors = 0

        for cell in self.neighbors:
            live_neighbors += cell.is_live()

        return live_neighbors

    def move_to_next_status(self):
        self.status = self.next_status
        
    def update_next_status(self):
        live_neighbors = self.number_of_live_neighbors()

        if self.is_live():
            if live_neighbors == 2 or live_neighbors == 3:
                self.next_status = CellStatus.LIVE
            else:
                self.next_status = CellStatus.DEAD

        else:
            if live_neighbors == 3:
                self.next_status = CellStatus.LIVE
            else:
                self.next_status = CellStatus.DEAD

    def add_neighbor(self, cell):
        self.neighbors.append(cell)

    def clear_neighbors(self):
        self.neighbors.clear()


class CellStatus(Enum):
    DEAD = 0
    LIVE = 1

