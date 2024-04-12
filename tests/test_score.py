import pytest

from final_solution.score import accuracy_score, macro_f1_score, team_score


def test_accuracy_score():
    y_true = [1, 0, 1, 0, 1]
    y_pred = [1, 0, 1, 0, 0]
    assert accuracy_score(y_true, y_pred) == 0.8


def test_macro_f1_score():
    y_true = [1, 0, 1, 0, 1]
    y_pred = [1, 1, 1, 0, 0]
    assert macro_f1_score(y_true, y_pred, 2) == 0.583


def test_team_score():
    y_true = [1, 0, 1, 0, 1]
    y_pred = [1, 1, 1, 0, 0]
    assert team_score(y_true, y_pred, 2) == 59.15


if __name__ == "__main__":
    pytest.main()
