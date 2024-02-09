from utils import *

def check_win(board: List[List[int]]) -> bool:
    for i in range(5):
        #Check rows
        for j in range(5):
            if board[(i * 5) + j] != 'x':
                break
            if j % 5 == 4:
                return True
            
        #Check columns
        for j in range(5):
            if board[(j * 5) + i] != 'x':
                break
            if j == 4:
                return True


def display_board(board: List[int]):
    string = ""
    for i in range(25):
        if i % 5 == 0:
            string += "\n\t"
        string += str(board[i]) + " "
    print(string)
        


def main():

    data = read_input("input.txt")

    nums = data.pop(0).split(",")
    nums = list(map(int, nums))
    boards = []

    j = 0
    #Sort data into boards and nums
    while len(data):
        if data[0] == '\n':
            data.pop(0)
            continue

        currentBoard = []
        while j < 5:
            row = data.pop(0).split(" ")
            row = [int(x) for x in row if x]
            currentBoard.extend(row)
            j += 1
        boards.append(currentBoard)
        j = 0

    i = 0
    for n in nums:
        print(f"number {i} is {n}")
        for board in boards:
            for index in range(len(board)):
                if board[index] == n:
                    board[index] = 'x'
                
            if i < 5:
                continue
            else:
                if check_win(board):
                    score = sum([x for x in board if type(x) is int])
                    index = boards.index(board)
                    print(f"\tWin! scored: {score * n}")
                    display_board(board)
                    boards.pop(index)
        i += 1


if __name__ == '__main__':
    main()
    



    