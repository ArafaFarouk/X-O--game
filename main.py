import os 

# clear screen 
def clear_screen():
    os.system("cls" if os.name =="nt" else "clear" )

class Player:
    def __init__(self):
        self.name = ""
        self.sympol = ""

    def choose_name(self):
        while True:
            name = input("Enter your name (letters only): ")
            if name.isalpha():
                self.name = name 
                break
            print("Invalid name. please use letters only: ")

    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, choose your symbol(a single letteer): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.sympol = symbol.upper()
                break
            print("Invalid symbol please choose a single letter: ")


class Menu :
    def display_main_menu(self):
        print("Welcom to my X-O game!")
        print("1- Start game")
        print("2- Quit game")
        choice = input("Enter your choice(1 or 2): ") # i need if condition for check input 
        return choice

    def display_endgame_menu(self):
        meun_text = """
        Game over!
        1- restart game
        2- quit game 
        Enter your choice(1 or 2): """
        choice = input(meun_text) # need check for input 
        return choice
    

class Board :
    def __init__(self):
        self.board = [str(i) for i in range(1,10)] # power of python code 
        # for i in range(1,10):
        #     self.board.append(str(i))
    def display_board(self):
        for i in range(0,9,3):
            print('|'.join(self.board[i:i+3]))
            if i < 6:
                print('-'*5)
    def update_board(self, choice , symbol):
        if self.is_valid_move(choice):
            self.board[choice -1] = symbol
            return True
        return False

     # helper function for check cill 
    def is_valid_move(self, choice):
        return self.board[choice -1].isdigit() 
        # if self.board[choice -1].isdigit()== True:
        #     return True 
        def reset_board(self):
            self.board = [str(i) for i in range(1,10)]


# main game logic 
class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    # set player details
    def setup_players(self):
        for number, player in enumerate (self.players, start=1):
            print(f"player{number}, enter your details:")
            player.choose_name()
            player.choose_symbol()
            clear_screen()

    # main game loop
    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restar_game()
                else:
                    self.quit_game()
                    break


                
    def restart_game(self):
        self.board.reset_board() 
        self.current_player_index = 0
        self.play_game()
     
    def check_win(self):
        win_ombinations = [
            [0,1,2],[3,4,5],[6,7,8], # rows 
            [0,3,6],[1,4,7],[2,5,8], # columns
            [0,4,8],[2,4,6]          # diagonals
        ]
        for combo in win_ombinations:
            if (self.board.board[combo[0]]) == self.board.board[combo[1]] == self.board.board[combo[2]]:
                return True
            return False


    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)


    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.sympol})")
        while True: # check valid input 
            try:
                cell_choice = int (input("choose a cell (1-9): "))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.sympol):
                   break
                else:
                    print("invalid move, try again: ")
            except ValueError:
                print("please enter a number between 1 and 9: ")
        # switch player 
        self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 -self.current_player_index


    def quit_game(self):
        print("thank you for playing! ")

game = Game()
game.start_game()      


 



    