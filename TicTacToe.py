import time
from collections import defaultdict


class Game:
    def __init__(self):
        self.players = []
        self.num_players = 0
        self.grid_size = 0
        self.symbol_pool = ['x', 'o', '#', '$', '%', '&', '*']
        self.len_adj = defaultdict(list)
        
        self.setup_game()
        self.main_logic()
    
    @staticmethod
    def error_message(msg):
        print(f"\033[91m{msg}\033[0m") # using ANSI escape codes for coloured text in terminal output
    
    @staticmethod
    def animate_text(text, delay=0.0003):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def check_win_condition(self, symbol):
        for row in self.board.grid:
            if all(item == symbol for item in row):
                return True
            
            return False
    
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
        
        valid_input = True
        while valid_input:
            while self.grid_size < 3:
                try:
                    self.grid_size = int(input("Enter size of grid eg. 3, 4 etc.. : "))
                    
                    if self.grid_size < 3:
                        Game.error_message("Grid size must be at least 3x3.")
                    
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
                valid_input = False
            
        self.board = Board(self.grid_size, self.grid_size)
        
        player_names = set()
        
        for i in range(self.num_players):
            while True:
                player_name = input(f"Enter the name of Player {i+1}: ").strip()
                
                if player_name and player_name not in player_names:
                    player_names.add(player_name)
                    self.players.append(Player(player_name))
                    break
                else:
                    Game.error_message("Invalid input or name already taken. Please enter a unique name.")

        Game.animate_text(welcome_screen)
        input("Press Enter to continue... \n")
    
    def main_logic(self):
        
        # while grid is not full, or no one has won
        win = False
        new_x = new_y = 0
        
        while not win:
            for i, player in enumerate(self.players):
                x = y = -1
                print(f"Player {player.name}'s Turn! Your symbol is {self.symbol_pool[i]} \n")
                self.board.print_update_grid()
                
                while True:
                    try:
                        location = input("Enter location you want to tag. eg. 4 2: ")
                        x, y = map(int, location.split())
                        
                        valid_position = (0 <= x < self.grid_size and 0 <= y < self.grid_size)
                        
                        if valid_position:
                            if not self.board.grid[x][y]:
                                self.board.grid[x][y] = self.symbol_pool[i]
                                self.board.print_update_grid(x, y, self.symbol_pool[i])
                                # # self.len_adj[self.symbol_pool[i]].append((x, y))
                                
                                # # counts symbol occurrence
                                # symbol_counts = {}
                                # for ls in self.board.grid:
                                #     for symbol in ls:
                                #         if symbol:
                                #             symbol_counts[symbol] = symbol_counts.get(symbol, 0) + 1
                                
                                # if any(v > 2 for v in symbol_counts.values()):
                                # for i in 
                                

                            else:
                                Game.error_message("Position is already occupied! ")

                        else:
                            Game.error_message("Invalid position. Position exceeds allowable range. Try again. ")
                        
                    except ValueError:
                        Game.error_message("Invalid input. Please enter a location in the same format as the example. ")
                
        # 4 2
        # determine which player is active (boolean)

        # check adjacency ie. diagonal / straight lines
        
        
        
        
    
class Board:
    def __init__(self, cols: int, rows: int):
        assert cols == rows, "cols and rows must be same dimensions"
        
        self.rows = rows
        self.cols = cols
        self.grid = [['' for _ in range(cols)] for _ in range(rows)]
    
    def print_update_grid(self, row_pos="", col_pos="", symbol=""):
        connect = ""
        for i in range(self.rows):
            k = 0
            for j in range(self.cols):
                
                # update grid when new element is seen
                if row_pos and col_pos and symbol: 
                    if i == row_pos and j == col_pos:
                        self.grid[i][j] = symbol
                
                cell_content = self.grid[i][j] if self.grid[i][j] else '_'
                
                print(cell_content, end=' | ' if j < self.cols-1 else " ")
                k += 1
                
            print()

            if i < self.rows-1:
                print('--x' + ('---x' * (self.cols-2)) + '--')
                
        print()
    
class Player:
    def __init__(self, name):
        self.name = name
        
    
    

Game()