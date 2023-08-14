class Table:
    def __init__(self):
        self.tiles = []
    
    def add_tile(self, tile):
        self.tiles.append(tile)
    
    def __str__(self):
        return ' '.join(map(str, self.tiles))