from heapq import heapify, heappush
import time

def main():
    rawData = loadData('input.txt')

    answerP1 = solve1(rawData)
    start = time.perf_counter()
    answerP2 = solve2(rawData)

    end = time.perf_counter()

    print(f'Elapsed time: {end - start:.6f} seconds')
    print(answerP2)


def helperSolve2(batteryPack: list[int], packsOn: int) -> list[int]:

    # Base Case
    if packsOn == 1:
        return [max(batteryPack)]

    topVal = max(batteryPack[: -(packsOn - 1)])
    topValIndex = batteryPack.index(topVal)

    return [topVal] + helperSolve2(batteryPack[topValIndex + 1 :], packsOn - 1)

def solve2(data):
    # This part 2 solution was from the following souce.
    # https://advent-of-code.xavd.id/writeups/2025/day/3/
    topJoltage = 0
    for bank in data:
        topPacks = helperSolve2([int(i) for i in bank], 12)
        topJoltage += int("".join(map(str, topPacks)))

    
    return topJoltage


def solve1(data):
    totalJoltage = 0
    
    
    for bank in data:
        maxHeap = []
        heapify(maxHeap)


        for i in range(len(bank)):
            for j in range(i+1, len(bank)):
                battery = int(bank[i] + bank[j])
                heappush(maxHeap, -battery)

        totalJoltage += -maxHeap[0]



    return totalJoltage




def loadData(data: str) -> list[str]:
    with open(data, 'r') as f:
        lines = f.readlines()

    linesData = lines[:-1] if lines[-1] == "" else lines
    rawData = [line_item.replace("\n", "") for line_item in linesData]

    return rawData


if __name__ == "__main__":
    main()