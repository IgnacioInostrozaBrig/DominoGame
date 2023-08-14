class UI:
    @staticmethod
    def display_message(message):
        input(message)
    
    @staticmethod
    def display_player(player):
        print(player)
    
    @staticmethod
    def display_table(table):
        print(table)

    def display_title():
        print('''
         _____                  _                  
        |  __ \                (_)                 
        | |  | | ___  _ __ ___  _ _ __   ___  ___  
        | |  | |/ _ \| '_ ` _ \| | '_ \ / _ \/ __| 
        | |__| | (_) | | | | | | | | | | (_) \__ \ 
        |_____/ \___/|_| |_| |_|_|_| |_|\___/|___/         
              \n''')
        
    def display_line():
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")