class Player:
    def __init__(self, player_number, hand):
        self.player_number = player_number
        self.hand = hand
    
    def __str__(self):
        return f'Jugador {self.player_number}: {self.hand}'