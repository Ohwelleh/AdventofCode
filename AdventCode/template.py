def main():
    rawData = loadData('sample.txt')

    answerP1 = solve(rawData)


def loadData(data: str) -> list[str]:
    with open(data, 'r') as f:
        lines = f.readlines()

    linesData = lines[:-1] if lines[-1] == "" else lines
    rawData = [line_item.replace("\n", "") for line_item in linesData]

    return rawData

def solve(data):
    pass


if __name__ == "__main__":
    main()