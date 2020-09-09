from math import inf 

class TicTacToeBrain:
    def __init__(self, board=["." for i in range(9)]):
        self.board = board

    def createWinStatement(self, possitions, token, board):
        pos1, pos2, pos3 = possitions

        if board[pos1] == token and board[pos2] == token and board[
                pos3] == token:

            return True
        return False

    def getWinner(self, board, currentPlayer):
        for possitions in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                           [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:

            if self.createWinStatement(possitions, currentPlayer, board):
                print(currentPlayer)
                return True, currentPlayer

        for box in board:
            if box == ".":
                return False, None

        print("TIE")
        return True, "tie"

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

    def returnPosition(self, winner, depth, bestPossition):
        cost = 1 - depth if winner == "x" else -1 + depth if winner == "o" else 0 - depth if winner == "x" else 0 + depth
        print("winner: ", winner, "| cost: ", cost, "| bestPosition: ",
              bestPossition, "\n")

        return cost, bestPossition

    def miniMax(self, board, currentPlayer, depth, alpha, beta, bestPosition):
        win, winner = self.getWinner(board, currentPlayer)

        if win:
            if winner == "tie":
                return bestPosition, 0 - depth if currentPlayer == "x" else 0 + depth

            return bestPosition, 1 - depth if winner == "x" else 1 + depth  

        bestEvaluation = -inf if currentPlayer == "x" else inf

        for child in self.getOpenSpaces(board):
            board[child] = currentPlayer

            bestPosition, evaluation = self.miniMax(

                board,
                self.getEnemyPlayer(currentPlayer),
                depth + 0.1,
                alpha,beta,
                child
                    )

            self.showBoard(board)        

            board[child] = "."

            bestEva = bestEvaluation
            print("bestEvaluation: ", bestEvaluation, "evaluation: ", evaluation)

            bestEvaluation = max(bestEvaluation, evaluation) if currentPlayer == "x" else min(bestEvaluation, evaluation)

            bestPosition = child if bestEva != bestEvaluation else bestPosition

            alpha = max(alpha, bestEvaluation)


            if beta <= alpha: break
        return bestPosition, bestEvaluation    


    def validMove(self, move):
        if move != None and 0 <= move <= 8 and self.board[move] == ".":
            return True

        print("invalid move \n")
        return False


    def game(self):
        self.showBoard(self.board)

        while True:
            for player in ["x", "o"]:

                if player == "x":
                    while True:

                        try:
                            move = int(input("move: "))

                            if self.validMove(
                                    move) and self.board[move] == ".":
                                break

                            else:
                                print("invalid move \n")

                        except ValueError:
                            print("that\'s not a number \n")

                else:
                    move, _ = self.miniMax(self.board, player, 0, -inf, inf, None)
                    print("move; ", move, "\n\n\n\n")

                self.board[move] = player
                self.showBoard(self.board)

                print(player + "\'s move: ", move)

                win, winner = self.getWinner(self.board, player)             

                if win:
                    print("game over, winner: ", winner)
                    return
