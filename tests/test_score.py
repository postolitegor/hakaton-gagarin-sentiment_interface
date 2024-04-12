import pytest
from sklearn.metrics import f1_score, accuracy_score

from final_solution.score import macro_f1_score, team_score, accuracy_score as your_accuracy_score


def test_accuracy_score():
    y_true = [1, 0, 1, 0, 1]
    y_pred = [1, 0, 1, 0, 0]

    your_accuracy = your_accuracy_score(y_true, y_pred)
    sklearn_accuracy = round(accuracy_score(y_true, y_pred), 3)

    assert round(your_accuracy, 3) == round(sklearn_accuracy, 3)


def test_macro_f1_score():
    y_true = [1, 0, 1, 0, 1]
    y_pred = [1, 1, 1, 0, 0]

    your_f1_score = macro_f1_score(y_true, y_pred, 2)
    sklearn_f1_score = round(f1_score(y_true, y_pred, average='macro'), 3)

    assert round(your_f1_score, 3) == round(sklearn_f1_score, 3)


def test_team_score():
    y_true = [1, 0, 1, 0, 1]
    y_pred = [1, 1, 1, 0, 0]

    your_team_score = team_score(y_true, y_pred, 2)
    sklearn_score = 100 * ((0.5 * f1_score(y_true, y_pred, average='macro'))
                           + (0.5 * accuracy_score(y_true, y_pred)))

    assert round(your_team_score, 3) == round(sklearn_score, 3)


if __name__ == "__main__":
    pytest.main()
