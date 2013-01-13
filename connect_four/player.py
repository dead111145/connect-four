import connectfour
from boardplayer import player


class HumanConnectFourPlayer(player.Player):
    def get_play(self):
        while True:
            move = raw_input("Please enter your move: ")
            move = self.board.parse(move)
            if move is None:
                continue
            if self.board.is_legal(self.states[-1], move):
                break
        return move


board = connectfour.Board()
player = HumanConnectFourPlayer(board)
player.run()
