import re

def main():
    rawData = loadData('input.txt')

    rawData = rawData[0].split(",")

    answerP1 = solve1(rawData)
    answerP2 = solve2(rawData)

    print(answerP2)


def solve2(data):
    sumInvalid = 0
    
    for val in data:
        rangeVal = val.split("-") 
        startRange = int(rangeVal[0])
        endRange = int(rangeVal[1])

        while startRange < (endRange + 1):

            # This commented out code was my attempt at solving part 2. This code worked for most cases, but struggled
            #   on numbers like 2121212121.
            # currentLen = len(str(startRange))
            # startPoint = 0
            # valuesEqual = True


            # if (int(currentLen) % 2) != 0:
            #     tempDict = {}
            #     for x in range(currentLen):
            #         if currentVal[x] in tempDict:
            #             tempDict[currentVal[x]] = tempDict[currentVal[x]] + 1
            #         else:
            #             tempDict[currentVal[x]] = 1

            #     lastKeyVal = -1

            #     for key in tempDict:
            #         currKeyVal = tempDict[key]
            #         if lastKeyVal < 0:
            #             lastKeyVal = currKeyVal
            #             continue
            #         elif lastKeyVal != currKeyVal or currKeyVal < 2:
            #             valuesEqual = False
            #             break

            #         lastKeyVal = currKeyVal
            # else:
            #     midPoint = int(currentLen // 2)

            #     while midPoint < currentLen:
            #         print(f'Before; Midpoint: {midPoint}, startP: {startPoint}, Current: {currentVal}, Length: {currentLen - 1}')
            #         if int(currentVal[startPoint]) != int(currentVal[midPoint]):
            #             if int(currentVal[startPoint]) != int(currentVal[midPoint - 1]):
            #                 valuesEqual = False
            #                 break
            #             else:
            #                 midPoint -= 1
            #         print(f'After; Midpoint: {midPoint}, startP: {startPoint}, Current: {currentVal}, Length: {currentLen - 1}')
            #         startPoint += 1
            #         midPoint += 1


            # Had to look at solution from someone else to get the regex.
            currentVal = str(startRange)

            if re.match(r"^(\d+)\1+$", currentVal):
                sumInvalid += startRange
                

            startRange += 1

    return sumInvalid

def solve1(data):

    sumInvalid = 0

    for val in data:
        rangeVal = val.split("-") 
        startRange = int(rangeVal[0])
        endRange = int(rangeVal[1])

        while startRange < (endRange + 1):
            currentLen = len(str(startRange))
            if (int(currentLen) % 2) != 0:
                startRange += 1
                continue

            currentVal = str(startRange)
            midPoint = int(currentLen // 2)
            startPoint = 0
            valuesEqual = True

            while startPoint < (currentLen / 2):
                if int(currentVal[startPoint]) != int(currentVal[midPoint]):
                    valuesEqual = False

                if not valuesEqual:
                    break

                startPoint += 1
                midPoint += 1

            if valuesEqual:
                sumInvalid += startRange

            startRange += 1



    return sumInvalid


def loadData(data: str) -> list[str]:
    with open(data, 'r') as f:
        lines = f.readlines()

    linesData = lines[:-1] if lines[-1] == "" else lines
    rawData = [line_item.replace("\n", "") for line_item in linesData]

    return rawData



if __name__ == "__main__":
    main()