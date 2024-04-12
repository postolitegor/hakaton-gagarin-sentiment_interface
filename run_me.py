import json
import pathlib
import time
import typing as tp

from final_solution.solution import score_texts

PATH_TO_TEST_DATA = pathlib.Path("data") / "test_texts.json"
PATH_TO_OUTPUT_DATA = pathlib.Path("results") / "output_scores.json"


def load_data(path: pathlib.PosixPath = PATH_TO_TEST_DATA) -> tp.List[str]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


def save_data(data, path: pathlib.PosixPath = PATH_TO_OUTPUT_DATA):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)


def main():
    start_time = time.time()

    texts = load_data()
    scores = score_texts(texts)
    print(scores)
    save_data(scores)

    end_time = time.time()
    print(f'Time taken: {end_time - start_time} seconds')


if __name__ == '__main__':
    main()
