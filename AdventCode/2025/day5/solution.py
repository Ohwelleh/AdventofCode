import numpy as np

def main():
    rawData = loadData('input.txt')

    
    # answerP1 = solve1(rawData)
    answerP2 = solve2(rawData)

    print(answerP2)


def solve2Helper(ranges: list[tuple[int]]):
    
    if not ranges: return 0

    # Creating a Numpy array of the ranges.
    r = np.array(ranges, dtype=np.int64)

    # Building the ranges to sweep. The r[:, 1] + 1 is to include the end point.
    positions = np.concatenate([r[:, 0], r[:, 1] + 1])

    # Adding weights to each range number. A 1 for the range start and -1 for the range end.
    deltas = np.concatenate([np.ones(r.shape[0]), -np.ones(r.shape[0])])

    # Getting the indices that would sort the array.
    order = np.argsort(positions, kind='mergesort')

    # Reordering based on the sorted indices.
    positions = positions[order]
    deltas = deltas[order]

    # Getting a sorted array of unique values. Inverse index array mapping unique_pos back to positions.
    unique_pos, inverse = np.unique(positions, return_inverse=True)

    # Creating a Numpy arry filled with zeros and a size of unique_pos.
    delta_sum = np.zeros(len(unique_pos), dtype=np.int64)

    # Adding values from deltas into delta_sum at indexes from inverse.
    np.add.at(delta_sum, inverse, deltas)

    active = np.cumsum(delta_sum)


    segments = np.diff(unique_pos)
    return int(segments[active[:-1] > 0].sum())

def solve2(data):

    ranges = []

    for item in data:
        if item == '':
            break
            
        temp = item.split("-")
        ranges.append((int(temp[0]), int(temp[1])))

    ans = solve2Helper(ranges)

    return ans


def solve1(data):

    gettingRanges = True
    ranges = []
    ingredientIDs = []

    for item in data:
        if item == '':
            gettingRanges = False
            continue

        if gettingRanges:
            temp = item.split("-")
            ranges.append([int(temp[0]), int(temp[1])])
        else:
            ingredientIDs.append(int(item))

    ranges = np.array(ranges)
    ingredientIDs = np.array(ingredientIDs)
    in_range = np.any((ingredientIDs[:, None] >= ranges[:, 0]) & (ingredientIDs[:, None] <= ranges[:, 1]), axis=1)
    

    return np.count_nonzero(in_range == True)


def loadData(data: str) -> list[str]:
    with open(data, 'r') as f:
        lines = f.readlines()

    linesData = lines[:-1] if lines[-1] == "" else lines
    rawData = [line_item.replace("\n", "") for line_item in linesData]

    return rawData



if __name__ == "__main__":
    main()