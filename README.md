# Lichess Puzzle FEN Finder (LPFF)
This script finds the FEN of a puzzle on lichess.org. It is useful for ~~cheating~~ **solving puzzles**.
## Dependencies
- Python 3
- chess
- colorama
- pyperclip
- stockfish (included)
- [Lichess Puzzle Database](https://database.lichess.org/lichess_db_puzzle.csv.zst)
## Usage
- Run `python3 export_board.py` to retrieve the FEN of a puzzle.
- Run `python3 engine_full.py` to solve a puzzle.
## Licence
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
## NOTE
This script is not affiliated with lichess.org in any way. Use at your own risk. If you do decide to use this for cheating, don't blame me if you get banned.
## FAQ
- **Q:** Why is the script so slow?
- **A:** The script is slow because it has to search the database for the FEN.
- **Q:** Is the code safe?
- **A:** Look at it yourself!
## Roadmap
- GUI Version.
## Acknowledgements / Credits
- [chess](https://pypi.org/project/chess/)
- [colorama](https://pypi.org/project/colorama/)
- [Stockfish](https://stockfishchess.org/) [LICENCE](stockfish/Copying.txt)
