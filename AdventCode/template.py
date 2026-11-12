def main():
    rawData = loadData('sample.txt')

    answerP1 = solve1(rawData)
    answerP2 = solve2(rawData)

    print(answerP1)


def solve2(data):
    return 2


def solve1(data):
    return 1


def loadData(data: str) -> list[str]:
    with open(data, 'r') as f:
        lines = f.readlines()

    linesData = lines[:-1] if lines[-1] == "" else lines
    rawData = [line_item.replace("\n", "") for line_item in linesData]

    return rawData



if __name__ == "__main__":
    main()