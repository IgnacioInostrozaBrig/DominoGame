class Domino:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
    
    def swap_sides(self):
        self.side1, self.side2 = self.side2, self.side1
        
    def __str__(self):
        return f'[{self.side1};{self.side2}]'
