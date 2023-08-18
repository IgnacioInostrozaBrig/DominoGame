class Player:
    def __init__(self, player_number, hand):
        self.player_number = player_number
        self.hand = hand
    
    def __str__(self):
        hand_str = ' '.join(str(card) for card in self.hand)
        return f'Jugador {self.player_number}: {hand_str}'