import pickle
import typing as tp
from pathlib import Path

import pandas as pd

from final_solution.preparation_issuer import get_issuerid

EntityScoreType = tp.Tuple[int, float]  # (entity_id, entity_score)
MessageResultType = tp.List[EntityScoreType]


def score_texts(
        messages: tp.Iterable[str], *args, **kwargs
) -> tp.Iterable[MessageResultType]:
    """
    Main function (see tests for more clarifications)
    Args:
        messages (tp.Iterable[str]): any iterable of strings (utf-8 encoded text messages)

    Returns:
        tp.Iterable[tp.Tuple[int, float]]: for any messages returns MessageResultType object
    -------
    Clarifications:
    >>> assert all([len(m) < 10 ** 11 for m in messages]) # all messages are shorter than 2048 characters
    """

    messages = list(messages) if hasattr(messages, "__iter__") else [messages]  # type: ignore

    if not messages:
        return []

    if len(messages) == 1 and messages[0] == "":
        return [[tuple()]]  # type: ignore

    issuer_path: Path = Path(Path.cwd(), "data", "issuer.pickle")
    with open(issuer_path.absolute(), 'rb') as f:
        loaded_data_dict = pickle.load(f)

    # TODO: fix me
    VALUE = 3.0

    scores = []

    example_path: Path = Path(Path.cwd(), "data", "example.xlsx")
    df = pd.read_excel(example_path.absolute())

    messages = df['MessageText'].tolist()

    # for message in messages:
    #     print(message)

    for message in messages:
        message = message.lower()
        result = get_issuerid(message, loaded_data_dict)
        scores.append([(result, VALUE)])

    return scores
