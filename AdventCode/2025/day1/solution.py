
def main():
    rawData = loadData('input.txt')

    # answerP1 = solve1(rawData)

    answerP2 = solve2(rawData)
    


    print(answerP2)



def solve2(data):
    currentPosition = 50
    maxVal = 99
    minVal = 0
    counter = 0

    for val in data:
        
        counterNotZero = (counter != 0)
        direction = val[0]
        directionVal = int(val[1:])

        if direction == "R":
            while directionVal > 0:
                currentPosition += 1
                directionVal -= 1
                if currentPosition > maxVal:
                    currentPosition = 0

                    if directionVal > 1 and counterNotZero:
                        counter += 1
        else:
            while directionVal > 0:
                currentPosition -= 1
                directionVal -= 1
                if currentPosition < minVal:
                    currentPosition = 99

                    if directionVal > 1 and counterNotZero:
                        counter += 1

        if currentPosition == 0:
            counter += 1

    
    return counter




def solve1(data):
    currentPosition = 50
    maxVal = 99
    minVal = 0
    counter = 0

    for val in data:
        direction = val[0]
        directionVal = int(val[1:])

        if direction == "R":
            while directionVal > 0:
                currentPosition += 1
                directionVal -= 1
                if currentPosition > maxVal:
                    currentPosition = 0
        else:
            while directionVal > 0:
                currentPosition -= 1
                directionVal -= 1
                if currentPosition < minVal:
                    currentPosition = 99

        if currentPosition == 0:
            counter += 1
    
    return counter




def loadData(data: str) -> list[str]:
    with open(data, 'r') as f:
        lines = f.readlines()

    linesData = lines[:-1] if lines[-1] == "" else lines
    rawData = [line_item.replace("\n", "") for line_item in linesData]

    return rawData


if __name__ == "__main__":
    main()