from pathlib import Path

import pandas as pd

if __name__ == '__main__':
    example_path: Path = Path(Path.cwd().parent, "data", "example.xlsx")
    df = pd.read_excel(example_path.absolute())

    messages = df['MessageText'].tolist()

    for message in messages:
        print(message)
        break
