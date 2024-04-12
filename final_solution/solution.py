import typing as tp

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

    # To support checking length and indexing of object
    messages = list(messages) if hasattr(messages, "__iter__") else [messages]

    # Prompt check for empty input and single empty string
    if not messages:
        return []

    if len(messages) == 1 and messages[0] == "":
        return [[tuple()]]

    # TODO: fix me
    COMPANIES = {"Сбер": 150, "Тинькофф": 225}
    VALUE = 3.0

    # Use a list comprehension to generate scores for all messages
    scores = [
        [
            (base_score, VALUE)
            for company, base_score in COMPANIES.items()
            if message.count(company) > 0
        ]
        for message in messages
    ]

    return scores
