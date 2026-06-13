import random 



def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100 
    if difficulty == "Hard":
        return 1, 200 
    return 1, 100 
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        # Handle decimal inputs (like "5.0" -> 5)
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
        # FIXED: Ensure both are integers for comparison
    # Convert guess to int if it's not already
    if not isinstance(guess, int):
        try:
            guess = int(guess)
        except (ValueError, TypeError):
            pass
    
    # Secret should always be int in this function now
    # But handle if it somehow isn't
    if not isinstance(secret, int):
        try:
            secret = int(secret)
        except (ValueError, TypeError):
            pass
    
    if guess == secret:
        return "Win", "🎉 Correct!"
    
    # FIXED: Clear, correct hints
    if guess > secret:
        return "Too High", "📉 Too high! Go LOWER!"
    else:
        return "Too Low", "📈 Too low! Go HIGHER!"


    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
    # FIXED: Remove the +1 offset (attempt 1 = 90 points, attempt 8 = 20 points)
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points
    
    # FIXED: Symmetrical scoring for wrong guesses
    # Both "Too High" and "Too Low" now subtract 5 points
    if outcome in ["Too High", "Too Low"]:
        return current_score - 5
    
    return current_score
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
