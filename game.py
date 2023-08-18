import random
from player import Player
from domino import Domino
from table import Table
from ui import UI

class Game:
    # Creación del juego
    def __init__(self):
        self.players = []
        self.table = Table()
        self.dominoes = [Domino(i, j) for i in range(7) for j in range(i, 7)]
        random.shuffle(self.dominoes)
    
    # Repartir fichas
    def deal_tiles(self):
        tiles_per_player = len(self.dominoes) // len(self.players)
        for player in self.players:
            player.hand = self.dominoes[:tiles_per_player]
            self.dominoes = self.dominoes[tiles_per_player:]
    
    # Buscar chancho más alto
    def find_starting_player(self):
        max_double_value = -1
        starting_player = None
        
        for player in self.players:
            for tile in player.hand:
                if tile.side1 == tile.side2 and tile.side1 > max_double_value:
                    max_double_value = tile.side1
                    starting_player = player
        
        return starting_player
    
    def play(self):
        # Buscar jugador inicial
        current_player = self.find_starting_player()
        
        while True:
            UI.display_message("Press Enter to continue...\n")
            UI.display_player(current_player)
            
            if len(current_player.hand) == 0:
                UI.display_message(f"Player {current_player.player_number} wins!\n")
                break
            
            UI.display_message("Press Enter to make a move...\n")
            
            if len(self.table.tiles) == 0:
                played_tile = random.choice(current_player.hand)
            else:
                played_tile = None
                for tile in current_player.hand:
                    if tile.side1 == self.table.tiles[-1].side2:
                        played_tile = tile
                        break
                    elif tile.side2 == self.table.tiles[-1].side2:
                        tile.swap_sides()
                        played_tile = tile
                        break
                    elif tile.side2 == self.table.tiles[0].side1:
                        played_tile = tile
                        break
                    elif tile.side1 == self.table.tiles[0].side1:
                        tile.swap_sides()
                        played_tile = tile
                        break
            
            if played_tile is None:
                UI.display_message(f"Player {current_player.player_number} can't play. Press Enter to continue...\n")
            else:
                current_player.hand.remove(played_tile)
                if len(self.table.tiles) == 0:
                    self.table.add_tile(played_tile)
                else:
                    if played_tile.side1 == self.table.tiles[-1].side2:
                        self.table.add_tile(played_tile)
                    else:
                        self.table.add_tile(played_tile)
                UI.display_table(self.table)
            current_player = self.players[(current_player.player_number) % len(self.players)]
    
    def start(self):
        UI.display_title()
        UI.display_line()
        num_players = int(input("Welcome, please enter the number of players (2-14): \n"))
        
        if num_players < 2 or num_players > 14:
            UI.display_message("Invalid number of players.")
            return
        
        print("Starting game with ",num_players," players . . .\n")
        self.players = [Player(i, []) for i in range(1, num_players + 1)]
        self.deal_tiles()
        self.play()

# Start the game
if __name__ == "__main__":
    game = Game()
    game.start()
