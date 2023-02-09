import chess
from colorama import Fore
import time
import pyperclip
def is_url(url):
    if url.startswith("https://lichess.org/training/"):
        return True
    else:
        return False

# search for db
try:
    f = open("lichess_db_puzzle.csv", "r")
    f.close()
except FileNotFoundError:
    print(Fore.RED + "lichess_db_puzzle.csv not found! Please download from here: https://database.lichess.org/lichess_db_puzzle.csv.zst" + Fore.RESET)
    input(Fore.GREEN + "Press enter to continue..." + Fore.RESET)
    exit(1)

while True:
    url = None
    if is_url(pyperclip.paste()) == True:
        url = pyperclip.paste()
        print(Fore.BLUE + "URL found: " + Fore.RED + url)
    else:
        print(Fore.RED + "No URL found in clipboard!" + Fore.RESET)
        url = input(Fore.CYAN + "Enter URL: " + Fore.RESET)
        try:
            if is_url(url) == False:
                raise ValueError
        except ValueError:
            print(Fore.RED + "Invalid URL!" + Fore.RESET)
            input(Fore.GREEN + "Press enter to continue..." + Fore.RESET)
            continue

    print(Fore.RED + "Searching for ID..." + Fore.RESET)
    id = url.split("/")[-1]
    # Opening the file lichess_db_puzzle.csv and reading it line by line. If the id is in the line, it
    # splits the line by the comma and takes the second item in the list.
    start_time = time.time()
    with open("lichess_db_puzzle.csv", "r") as f:    
        for line in f:        
            # print search time
            if id in line:
                fen = line.split(",")[1]
                print(Fore.BLUE + "FEN found: " + Fore.RED + fen)
                end_time = time.time()
                search_time = (end_time - start_time) * 1000
                print(Fore.BLUE + "Search time: " + Fore.RED + str(search_time) + " ms")
                break
                
        f.close()

    board = chess.Board(fen)
    turn = None
    if board.turn == True:
        turn = Fore.WHITE + "White"
    else:
        turn = Fore.BLACK + "Black"
    print(Fore.GREEN + "Turn: " + str(turn))
    next_move = input(Fore.CYAN + "Enter next move: ")
    try:
        board.push_san(next_move)
    except ValueError:
        print(Fore.RED + "Invalid move!" + Fore.RESET)
        input(Fore.GREEN + "Press enter to continue..." + Fore.RESET)
        continue
    pyperclip.copy(board.fen())
    print(Fore.RED + "FEN copied to clipboard!" + Fore.RESET)
    input(Fore.GREEN + "Press enter to continue..." + Fore.RESET)

