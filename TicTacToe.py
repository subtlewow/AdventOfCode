class Game:
    def __init__(self):
        self.players = []
        self.num_players = 0
        self.grid_size = 0
        self.setup_game()
    
    @staticmethod
    def error_message(msg):
        print(f"\033[91m{msg}\033[0m")
    
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
        
            # Checking valid inputs for Grid Size and Number of Players.
        
        valid_input = False
        while not valid_input:
            while self.grid_size < 2:
                try:
                    self.grid_size = int(input("Enter size of grid eg. 2, 3 etc.. : "))
                    
                    if self.grid_size < 2:
                        Game.error_message("Grid size must be at least 2x2.")
                    
                except ValueError:
                    Game.error_message("Invalid input. Please enter a valid number for grid size.")
            
            while self.num_players < 2 or self.num_players % 2 == 1:
                try:
                    self.num_players = int(input("How many players to play?: "))
                    
                    if self.num_players < 2:
                        Game.error_message("Number of players must be more than 1.")
                    elif self.num_players % 2:
                        Game.error_message("There can only be an even number of players.")
                    
                except ValueError:
                    Game.error_message('Invalid input. Please enter a valid number for number of players.')
            
            if self.grid_size < self.num_players:
                Game.error_message(f"Grid Size of {self.grid_size}x{self.grid_size} cannot accommodate for {self.num_players} players.\nPlease adjust your grid size, or number of players.")
                
                self.grid_size = 0
                self.num_players = 0
            else:
                valid_input = True
            
        self.board = Board(self.grid_size, self.grid_size)
        
        # check if grid size can accommodate chosen players
        # if self.grid_size > self.num_players:
            
        
        
        # 2x2, 2 players
        # 3x3, at most 3 players 
        
        
                
        for i in range(self.num_players):
            player_name = input(f"Enter the name of Player {i+1}: ")
            self.players.append(Player(player_name))
        
        print(welcome_screen)
        input("Press Enter to continue.. ")
        Board().print_grid()
    
    def main_logic():
        pass
    
class Board:
    def __init__(self, cols: int = 3, rows: int = 3):
        assert cols == rows, "cols and rows must be same dimensions"
        
        self.rows = rows
        self.cols = cols
        self.grid = [['' for _ in range(cols)] for _ in range(rows)]
        
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
    
    def update_grid():
        pass
        
    
class Player:
    def __init__(self, name):
        self.name = name
    
    

Game()