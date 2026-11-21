import numpy as np

def main():
    rawData = loadData('sample.txt')

    # answerP1 = solve1(rawData)
    answerP2 = solve2(rawData)

    print(answerP2)

"""
    This is not a solution for part 2. Moved onto day 7 to get ready for December 2026 calendar.
"""
def solve2(data):

    operations = dict(enumerate(data.pop().split()))
    values = np.array([x.split() for x in data]).astype(int)
    rotated = np.flip(np.rot90(values, -1), axis=1)
    total = 0

    for index, row in enumerate(rotated):

        operat = operations[index]
        rowTotal = []
        carry = 0

        # Loop while row contains any nonzero or carry has a remainder.
        while any(row) or carry:
            tempTotal = carry
            tempVals = []
            tempVal = ''
            for i, n in enumerate(row):
                if n == -10: 
                    continue
                # Getting rightmost digit and performing the operation.
                # if operat == '*':
                #     if tempTotal == 0: tempTotal = 1
                #     if n == 0: continue
                #     tempTotal *= n % 10
                # else:
                #     tempTotal += n % 10 
                tempTotal = n % 10
                tempVal += str(tempTotal)

                # Shift the value left for next iteration.
                shift = n // 10
                if shift == 0:
                    row[i] = -10
                else:
                    row[i] = n // 10

            # Dividing tempTotal by 10
            carry, digit = divmod(tempTotal, 10)
            if(row == -10).all():
                break

            rowTotal.append(tempVal)

        print(f' D: {digit}')

        for v in rowTotal:
            print(f'V: {v}')
            total += int(v)
        # total += int(''.join(map(str, rowTotal[::-1])))
        print(total)


    
    return total
    


def solve1(data):
    operations = dict(enumerate(data.pop().split()))
    values = [x.split() for x in data]
    rows = len(values)
    cols = len(values[0])
    total = 0

    for c in range(cols):
        multiply = False
        temp = 0
        if operations[c] == '*': multiply = True

        for r in range(rows):
            
            if r == 0:
                temp = int(values[r][c])
                continue

            if multiply:
                temp *= int(values[r][c])
            else:
                temp += int(values[r][c])
   
        total += temp
    
    return total


def loadData(data: str) -> list[str]:
    with open(data, 'r') as f:
        lines = f.readlines()

    linesData = lines[:-1] if lines[-1] == "" else lines
    rawData = [line_item.replace("\n", "") for line_item in linesData]

    return rawData



if __name__ == "__main__":
    main()