# x-infinity

## Instructions

### Running the Project
First, clone this repository.

After navigating to the project directory, run the following commands:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

### Managing Crosswords
You can access the crossword management window by clicking the **Select Wordlist** button at the bottom of the main screen:  
![select button](assets/select_button.png)

In this window, you can add word lists and entries with their definitions, as well as delete and modify them.  
![wordlist window](assets/wordlist_window.png)

There is also an option to generate word lists, which allows you to create a new list of entries with predefined definitions ("Generate" on the left side).

Additionally, you can automatically assign definitions to certain words (from the list in `full_data.json`). This is done using the "Generate definitions" button, located further to the right.

Clicking the "Use this wordlist" button closes the window and selects the appropriate word list.

### Solving the Crossword  
![crossword](assets/crossword.png)

To fill in the crossword, first select the appropriate cell with the mouse cursor, then type letters on the keyboard.

#### Controls
- Any letter from A to Z (English alphabet) – enters the letter into the current cell and moves the cursor to the next cell.
- Spacebar – moves the cursor to the next cell.
- Backspace – deletes the letter from the current cell.
- Arrow keys – move the cursor to an adjacent cell.
- Double-clicking a cell – reveals the letter. This letter becomes frozen and cannot be modified.

#### Checking the Crossword
To check the crossword, click the "Check your answer" button at the bottom of the main window. Correct cells are highlighted in green, while incorrect ones turn red. To exit the checking mode, click the same button again.

#### Generating Based on a Key Word
Entering any non-empty word in the bar at the bottom of the main window will cause subsequent crosswords to be generated based on this word as the key entry.

### Data Download Script
Run:
```
python3 data.py
```

**WARNING: Downloading data takes several dozen seconds. The raw data itself is approximately 300 MB in total.**

This script fetches data from websites and saves it to the `full_data.json` file. Theoretically, it should contain up to 5000 entries with definitions. In practice, it holds around 3450 entries (as of 12.01.25) because not all words have corresponding definitions in the Oxford Learner's Dictionary.
