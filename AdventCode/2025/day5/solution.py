def main():
    rawData = loadData('input.txt')

    
    answerP1 = solve1(rawData)
    answerP2 = solve2(rawData)

    print(answerP1)


def solve2(data):
    return 2


def solve1(data):

    gettingRanges = True
    ranges = []
    ingredientIDs = []

    isFresh = {}
    totalFresh = 0

    for item in data:
        if item == '':
            gettingRanges = False
            continue

        if gettingRanges:
            ranges.append(item)
        else:
            ingredientIDs.append(int(item))

    for rang in ranges:
        values = rang.split("-")
        for i in range(int(values[0]), int(values[1]) + 1):
            isFresh[i] = True


    for id in ingredientIDs:
        if id in isFresh:
            totalFresh += 1

    return totalFresh


def loadData(data: str) -> list[str]:
    with open(data, 'r') as f:
        lines = f.readlines()

    linesData = lines[:-1] if lines[-1] == "" else lines
    rawData = [line_item.replace("\n", "") for line_item in linesData]

    return rawData



if __name__ == "__main__":
    main()