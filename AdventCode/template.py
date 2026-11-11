def main():
    rawData = loadData('sample.txt')

    answerP1 = solve(rawData)

    print(answerP1)


def solve(data):
    return 1


def loadData(data: str) -> list[str]:
    with open(data, 'r') as f:
        lines = f.readlines()

    linesData = lines[:-1] if lines[-1] == "" else lines
    rawData = [line_item.replace("\n", "") for line_item in linesData]

    return rawData



if __name__ == "__main__":
    main()