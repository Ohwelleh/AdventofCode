import numpy as np
import networkx as nx


def main():
    rawData = loadData('input.txt')

    #answerP1 = solve1(rawData)
    answerP2 = solve2(rawData)

    print(answerP2)


def solve2(data):
    int2Darray = []
    newLabel = 0
    for line in data:
        lineData = []
        for c in line:
            if c == '.':
                lineData.append(0)
            else:
                lineData.append(newLabel)
                newLabel += 1

        int2Darray.append(lineData)

    adj_matrix = np.zeros((newLabel, newLabel), dtype=int)
    rowLen = len(int2Darray)
    colLen = len(int2Darray[0])
    build_Adj(int2Darray, rowLen - 1, colLen - 1, adj_matrix)
    graph = nx.from_numpy_array(adj_matrix)

    return removeNodes(graph)


def removeNodes(graph: nx.Graph):
    accessedPaper = 0

    while True:
        paperToRemove = [node for node, degree in graph.degree() if degree < 4]
        accessedPaper += len(paperToRemove)

        if len(paperToRemove) == 0:
            break

        graph.remove_nodes_from(paperToRemove)


    return accessedPaper


def build_Adj(maxtrix: list[list[int]], rowSize: int, colSize: int, npArray):
    
    # Starting at 12 o'clock moving clockwise.
    directions: list[tuple[int, int]] = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    for rowIndex, r in enumerate(maxtrix):
        for colIndex, c in enumerate(r):
            if c == 0: continue

            for dx, dy in directions:
                newRow = rowIndex + dx
                newCol = colIndex + dy

                if newRow > rowSize or newRow < 0 or newCol < 0 or newCol > colSize:
                    continue

                if maxtrix[newRow][newCol] > 0:
                    newVal = maxtrix[newRow][newCol]
                    npArray[newVal][c] = 1
                    npArray[c][newVal] = 1

def solve1(data):
    int2Darray = []
    for line in data:
        lineData = []
        for c in line:
            if c == '.':
                lineData.append(0)
            else:
                lineData.append(1)

        int2Darray.append(lineData)

    rowLen = len(int2Darray)
    colLen = len(int2Darray[0])

    return check_neighbours(int2Darray, rowLen - 1, colLen - 1)
    


def check_neighbours(maxtrix: list[list[int]], rowSize: int, colSize: int):
    
    # Starting at 12 o'clock moving clockwise.
    directions: list[tuple[int, int]] = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    accessedPaper = 0

    for rowIndex, r in enumerate(maxtrix):
        for colIndex, c in enumerate(r):
            if c == 0: continue
            neighbours = 0

            for dx, dy in directions:
                newRow = rowIndex + dx
                newCol = colIndex + dy

                if newRow > rowSize or newRow < 0 or newCol < 0 or newCol > colSize:
                    continue

                if maxtrix[newRow][newCol] == 1:
                    neighbours += 1

            if neighbours < 4:
                accessedPaper += 1


    return accessedPaper
        


def loadData(data: str) -> list[str]:
    with open(data, 'r') as f:
        lines = f.readlines()

    linesData = lines[:-1] if lines[-1] == "" else lines
    rawData = [line_item.replace("\n", "") for line_item in linesData]

    return rawData



if __name__ == "__main__":
    main()