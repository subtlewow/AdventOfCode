
class Board:
    def __init__(self, cols: int = 3, rows: int = 3):
        assert cols == rows, "cols and rows must be same dimensions"
        
        self.rows = rows
        self.cols = cols
        
    def print_grid(self):
        i = j = 0
        connect = ""
        breaker = False
        while i < self.rows:
            while j < self.cols:
                if j == 0:
                    print(' ', end='')
                
                if j == self.cols-1:
                    print("_", end=" ")
                else:
                    print('_', end=" | ")
                
                j += 1
                
            j = 0
            i += 1
            
            print() # new line
            
            if not breaker:
                for k in range(self.cols):
                    if k == self.cols-1:
                        connect += ('-' * 3) 
                    else:
                        connect += ('-' * 3) + 'x'
                
            print(connect)
            breaker = True
        
        
class Game:
    def __init__(self):
        self.players = []
        self.setup_game()
        
    def setup_game(self):
        welcome_screen = """
        \033[32m
            ╔════════════════════════════════════════════════════════════════════════════════════════╗
            ║                                                                                        ║
            ║                                                                                        ║
            ║                                                                                        ║
            ║        ████████╗██╗ ██████╗ ████████╗ █████╗  ██████╗ ████████╗ ██████╗ ███████╗       ║
            ║        ╚══██╔══╝██║██╔════╝ ╚══██╔══╝██╔══██╗██╔════╝ ╚══██╔══╝██╔═══██╗██╔════╝       ║
            ║           ██║   ██║██║         ██║   ███████║██║         ██║   ██║   ██║█████╗         ║
            ║           ██║   ██║██║         ██║   ██╔══██║██║         ██║   ██║   ██║██╔══╝         ║
            ║           ██║   ██║╚██████╗    ██║   ██║  ██║╚██████╗    ██║   ╚██████╔╝███████╗       ║
            ║           ╚═╝   ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚══════╝       ║
            ║                                                                                        ║
            ║                                                                                        ║
            ║                                Welcome to Tic Tac Toe!                                 ║
            ║                            Press Enter to start the game                               ║
            ║                                                                                        ║
            ║                                                                                        ║
            ╚════════════════════════════════════════════════════════════════════════════════════════╝
        \033[0m
        """
        
        self.num_players = int(input("How many players to play?: "))
        
        for i in range(self.num_players):
            self.player_name = input(f"Enter the name of Player {i+1}: ")
            # self.players.append(Player(self.player_name))
        
        print(welcome_screen)
        input("Press Enter to continue.. ")
    
# class Player:
#     def __init__(self):
        
    
    
    
# Ask number of players, ask for player names

Game()