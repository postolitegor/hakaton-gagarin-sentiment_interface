import typing as tp

EntityScoreType = tp.Tuple[int, float]  # (entity_id, entity_score)
MessageResultType = tp.List[EntityScoreType]


def score_texts(messages: tp.Iterable[str], *args, **kwargs) -> tp.Iterable[MessageResultType]:
    """
    Evaluate the score for each company in each message.

    @param messages: Iterable collection of strings (utf-8 encoded text messages)
    @return: Iterable collection of company scores (company id, score) for each message.
    @raises ValueError: If any of the message length is more than 2048 characters.
    """

    # Prompt check for empty input and single empty string
    if not messages:
        return []

    if len(messages) == 1 and messages[0] == "":
        return [[tuple()]]

    # Raise an error if any messages exceed limit of 2048 characters
    if any(len(message) > 2048 for message in messages):
        raise ValueError("Each message should be less than or equal to 2048 characters")

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
