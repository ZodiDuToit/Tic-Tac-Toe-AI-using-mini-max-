class TicTacToeBrain:
    def __init__(self, board=["." for i in range(9)]):

        self.currentPlayer = 'x'
        self.best = None
        self.bestPosition = None

        self.board = board

    def getWinner(self, board, curentPlayer):

        if self.board[0] == curentPlayer and self.board[1
                ] == curentPlayer and self.board[2] == curentPlayer:
            return curentPlayer

        if self.board[3] == curentPlayer and self.board[4
                ] == curentPlayer and self.board[5] == curentPlayer:
            return curentPlayer
     
        if self.board[6] == curentPlayer and self.board[7
                ] == curentPlayer and self.board[8] == curentPlayer:
            return curentPlayer    

        if self.board[0] == curentPlayer and self.board[3
                ] == curentPlayer and self.board[6] == curentPlayer:
            return curentPlayer

        if self.board[1] == curentPlayer and self.board[4
                ] == curentPlayer and self.board[7] == curentPlayer:
            return curentPlayer

        if self.board[2] == curentPlayer and self.board[5
                ] == curentPlayer and self.board[8] == curentPlayer:
            return curentPlayer

        if self.board[0] == curentPlayer and self.board[4
                ] == curentPlayer and self.board[8] == curentPlayer:
            return curentPlayer            

        if self.board[2] == curentPlayer and self.board[4
                ] == curentPlayer and self.board[6] == curentPlayer:
            return curentPlayer

        for position in board:
            if position == ".":
                return None

        return "draw"

    def showBoard(self, board):
        string = ""

        for i in range(len(board)):
            string += " " + board[i]

            if len(string) == 6:
                print(string)
                string = ""      

    def getOpenSpaces(self, board):
        for i in range(len(board)):
            if board[i] == ".":
                yield i

    def getEnemyPlayer(self, currentPlayer):
        if currentPlayer == "x":
            return "o"
        return "x"

    def miniMax(self, board, currentPlayer, depth, bestPosition=None):
        winner = self.getWinner(board, self.getEnemyPlayer(currentPlayer))

        if winner == "x":
            return 1 - depth, bestPosition

        elif winner == "o":
            return -1 + depth, bestPosition

        elif winner == "draw":
           return 0

        if currentPlayer == "x":
            best = -100
        else:
            best = 100
        
        for position in self.getOpenSpaces(board):

            board[position] = currentPlayer

            self.showBoard(board)
            print(best, bestPosition, "\n") if best != 100 and best != -100 and bestPosition != None else print()

            cost, predicted = self.miniMax(

                board,
                self.getEnemyPlayer(currentPlayer),
                depth + 0.1, bestPosition
                                   
                                   )

            self.board[position] = "."

            if currentPlayer == "x" and cost - depth > best:
                best = cost
                bestPosition = position


            elif currentPlayer == "o" and cost + depth < best:
                best = cost
                bestPosition = position

        return best, bestPosition
            

Brain = TicTacToeBrain(["o", "x", "o",
                        ".", ".", "x",
                        "o", "o", "x"])

print(Brain.miniMax(Brain.board, "x", 0))
