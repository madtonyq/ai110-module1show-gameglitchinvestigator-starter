# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
The purpose of the game is that there is a secret number and you have a number of attempts to guess
the number and when you get it wrong the output will indicate if you need to go higher or lower
- [ ] Detail which bugs you found.
1. I found was the difficulty range was set weirdly such that hard has a lower range that normal 
2. I found was when output indicate whether you need to go higher or lower it will tell you the opposite 
3. Update score is broken as if you guess too low it will only subtract 
4.  Attempt Count Starts at 1 not zero
5. Secret Number Changes for Even Attempts
6. Win Condition Message is Wrong as it compares str with an int 
7.  Score Calculation on Win is Wrong 
8. New Game Doesn't Reset Correctly
- [ ] Explain what fixes you applied.
1. set harder on a range of 1 to 200
2. fix the logic by when its too high go lower and when its too lower go higher 
3. whether outcome is too high or too low it will always be current score subtract 5
4. if the attempts are not in session state we set attempts to 0 
5. we remove the if else statement and keep the secret untouch 
6. covert guess to int 
7. we remove the +1 from win calculation formula 
8. if user call for new game we set sessions attempt at 1 and get the difficulty user sets along with getting the current game session secret number along with score set to zero along with status as playing

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step --> User choose their difficulty
2. <!-- Describe this step --> once user gets the diffculty they want start calling the secret number in the number of attempts given  
3. <!-- Describe this step --> if the user guess is lower than secret number the game will prompt user to go higher while if guess is higher than secret number the game will prompt user to go lower
4. <!-- Describe this step --> if the user guesses the number in the given amount of attempts the game will print a congrats message while if the user fails they will be given a out of attempts message 
5. <!-- Add more steps as needed -->

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```
test_game_logic.py::test_get_range_for_difficulty PASSED                                                                              [ 12%]
test_game_logic.py::test_parse_guess_valid PASSED                                                                                     [ 25%]
test_game_logic.py::test_parse_guess_invalid PASSED                                                                                   [ 37%]
test_game_logic.py::test_check_guess_win PASSED                                                                                       [ 50%]
test_game_logic.py::test_check_guess_too_high PASSED                                                                                  [ 62%]
test_game_logic.py::test_check_guess_too_low PASSED                                                                                   [ 75%]
test_game_logic.py::test_update_score_win PASSED                                                                                      [ 87%]
test_game_logic.py::test_update_score_wrong PASSED                                                                                    [100%]

============================================================ 8 passed in 0.03s =============================================================
## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
