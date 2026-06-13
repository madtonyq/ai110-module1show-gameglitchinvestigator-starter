import pytest
from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score

def test_get_range_for_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 200)

def test_parse_guess_valid():
    ok, val, err = parse_guess("42")
    assert ok == True
    assert val == 42
    assert err is None

def test_parse_guess_invalid():
    ok, val, err = parse_guess("abc")
    assert ok == False
    assert val is None
    assert err == "That is not a number."

def test_check_guess_win(): 
    outcome, msg = check_guess(50, 50)
    assert outcome == "Win"

def test_check_guess_too_high():
    outcome, msg = check_guess(75, 50)
    assert outcome == "Too High"

def test_check_guess_too_low():
    outcome, msg = check_guess(25, 50)
    assert outcome == "Too Low"

def test_update_score_win():
    score = update_score(0, "Win", 1)
    assert score == 90  # 100 - 10*1

def test_update_score_wrong():
    score = update_score(100, "Too High", 3)
    assert score == 95