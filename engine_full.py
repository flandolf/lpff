import chess
import chess.engine
from colorama import Fore, Back
import time
import pyperclip

def is_url(url):
    if url.startswith("https://lichess.org/training/"):
        return True
    else:
        return False
def is_san(move):
    try:
        chess.Move.from_uci(move)
        return True
    except chess.InvalidMoveError:
        return False
def is_id(id):
    if id.startswith("#"):
        return True
    else:
        return False
while True:
    url = None
    if is_id(pyperclip.paste().strip()) == True:
        url = "https://lichess.org/training/" + pyperclip.paste().strip()[1:]
        print(Fore.BLUE + "ID found: " + Fore.RED + pyperclip.paste()[1:])
    elif is_url(pyperclip.paste().strip()) == True:
        url = pyperclip.paste().strip()
        print(Fore.BLUE + "URL found: " + Fore.RED + url)
    else:
        url = input(Fore.CYAN + "Enter URL: " + Fore.RESET)
        try:
            if is_url(url) == False:
                raise ValueError
        except ValueError:
            print(Fore.RED + "Invalid URL!" + Fore.RESET)
            continue
    print(Fore.RED + "Searching for DB..." + Fore.RESET, end=" ")
    try:
        f = open("lichess_db_puzzle.csv", "r")
        f.close()
        print(Fore.GREEN + "DB found!" + Fore.RESET)
    except FileNotFoundError:
        print(Fore.RED + "lichess_db_puzzle.csv not found! Please download from here: https://database.lichess.org/lichess_db_puzzle.csv.zst" + Fore.RESET)
        input(Fore.GREEN + "Press enter to continue..." + Fore.RESET)
        exit(1)
    id = url.split("/")[-1]
    start_time = time.time()
    with open("lichess_db_puzzle.csv", "r") as f:
        for line in f:
            if id in line:
                fen = line.split(",")[1]
                print(Fore.BLUE + "FEN found: " + Fore.RED + fen)
                print(Fore.RED + "Copied FEN to clipboard!" + Fore.RESET)
                pyperclip.copy(fen)
                end_time = time.time()
                search_time = round((end_time - start_time) * 1000)
                print(Fore.BLUE + "Search time: " + Fore.RED + str(search_time) + " ms")
                break
        f.close()
    board = chess.Board(fen)
    turn = None
    if board.turn == True:
        turn = Back.BLACK + Fore.WHITE + "White"
    else:
        turn = Back.WHITE + Fore.BLACK + "Black"
    print(Fore.GREEN + "Turn: " + str(turn) + Fore.RESET + Back.RESET) 

    board = chess.Board(fen)
    engine = chess.engine.SimpleEngine.popen_uci("stockfish/stockfish15.exe")
    next_move_san = input(Fore.CYAN + "Enter next move: ")
    try:
        is_san(next_move_san)
    except:
        print(Fore.RED + "Invalid move!" + Fore.RESET)
        continue
    board.push_san(next_move_san)
    while True:
        result = engine.play(board, chess.engine.Limit(time=0.2))     
        print(Fore.GREEN + "Engine move: " + Fore.RED + board.san(result.move))
        board.push(result.move)   
        next_move_san = input(Fore.CYAN + "Enter next move: ")
        if next_move_san == "":
            break
        try:
            board.push_san(next_move_san)
        except:
            print(Fore.RED + "Invalid move!" + Fore.RESET)
            exit(1)
        # check if checkmate
        if board.is_checkmate() == True:
            print(Fore.GREEN + "Checkmate!" + Fore.RESET)
            break
    input("Press enter to continue...")

    


