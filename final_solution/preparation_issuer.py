import pickle
from pathlib import Path

import pandas as pd


def read_data(file_path: Path) -> pd.DataFrame:
    """
    Читает excel-файл, заполняет значения NaN пустыми строками и создает новую колонку 'titles'.

    :param file_path: Путь к excel-файлу.
    :return: DataFrame после выполнения операций.
    """
    df = pd.read_excel(file_path)
    df.fillna('', inplace=True)

    df['titles'] = df[df.columns[3:]].values.tolist()

    return df


def extend_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Итерирует по индексу DataFrame, чтобы расширить список 'titles' с помощью
    'EMITENT_FULL_NAME' и 'BGTicker'.

    :param df: DataFrame полученный из функции read_data.
    :return: DataFrame после расширения 'titles'.
    """
    df['titles'] = df.apply(lambda row: row['titles'] + [row['EMITENT_FULL_NAME'], row['BGTicker']], axis=1)

    return df


def process_titles(df: pd.DataFrame) -> pd.DataFrame:
    """
    Обрабатывает колонку 'titles', удаляя дубликаты и пустые значения.

    :param df: DataFrame полученный из функции extend_data.
    :return: DataFrame с обработанными 'titles'.
    """
    df['titles'] = df['titles'].apply(lambda x: list(filter(None, set(item.lower() for item in x))))

    return df


def prep_data(df: pd.DataFrame) -> list:
    """
    Подготавливает итоговый список данных в виде словарей с ключами 'issuerid', 'EMITENT_FULL_NAME',
    'BGTicker' и 'titles'.

    :param df: DataFrame полученный из функции process_titles.
    :return: Список всех записей.
    """
    data = df[['issuerid', 'EMITENT_FULL_NAME', 'BGTicker', 'titles']].to_dict('records')

    return data


def get_issuerid(string: str, data_dict: dict) -> int:
    """
    Ищет соответствие 'titles' в данной строке и возвращает соответствующий 'issuerid'

    :param string: Строка, в которой ищем соответствие
    :param data_dict: Подготовленный словарь данных с 'titles' и 'issuerid'
    :return: 'issuerid', если найдено соответствие, в противном случае `-1`
    """
    return next((record['issuerid'] for record in data_dict if any(title in string for title in record['titles'])), -1)


if __name__ == "__main__":
    path: Path = Path(Path.cwd().parent, "data", "ready_issuer.xlsx")
    df = read_data(path.absolute())
    df = extend_data(df)
    df = process_titles(df)
    data_dict = prep_data(df)

    issuer_pickle_path: Path = Path(Path.cwd().parent, "data", "issuer.pickle")
    with open(issuer_pickle_path.absolute(), 'wb') as f:
        pickle.dump(data_dict, f)

    ### Example ###
    # test_string = "Роснефть увеличила добычу на 3% в 2022 году".lower()
    # result = get_issuerid(test_string, data_dict)
    # print(result)
