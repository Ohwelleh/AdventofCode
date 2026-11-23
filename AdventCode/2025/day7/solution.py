def main():
    rawData = loadData('input.txt')

    answerP1 = solve1(rawData)
    answerP2 = solve2(rawData)

    print(answerP1)


def solve2(data):
    return 2


def solve1(data):
    rowMaxLen = len(data[0])
    prevBeams = [False for i in range(rowMaxLen)]
    splitCounter = 0

    for row in data:
        currentBeams = [False for i in range(rowMaxLen)]
        if "S" in row:
            prevBeams[row.index("S")] = True
            continue
    
        splitterInd = [i for i, s in enumerate(row) if s == "^"]
        if not splitterInd: continue


        for splitter in splitterInd:
            # Checking if beam is coming into splitter
            if prevBeams[splitter]:
                splitCounter += 1

                if splitter == 0:
                    currentBeams[splitter + 1] = True
                elif splitter == rowMaxLen:
                    currentBeams[splitter - 1] = True
                else:
                    currentBeams[splitter - 1] = True
                    currentBeams[splitter + 1] = True

                prevBeams[splitter] = False

        prevBeams = currentBeams
      

    return splitCounter


def loadData(data: str) -> list[str]:
    with open(data, 'r') as f:
        lines = f.readlines()

    linesData = lines[:-1] if lines[-1] == "" else lines
    rawData = [line_item.replace("\n", "") for line_item in linesData]

    return rawData



if __name__ == "__main__":
    main()