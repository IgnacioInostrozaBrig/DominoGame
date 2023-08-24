class Table:
    def __init__(self):
        self.tiles = []
    
    def add_tile(self, tile, position):
        
        if position == -1:
            self.tiles.append(tile)
        else:
            self.tiles.insert(position, tile)
    
    def __str__(self):
        return ' '.join(map(str, self.tiles))