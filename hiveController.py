import hiveModel
import hiveView
import sys

class Controller():

    def __init__(self):
        self.model = hiveModel.Structure()
        self.view = hiveView.View()
        self.x0 = 100
        self.y0 = 150
        self.view.root.bind('<Button-1>', self.controlClick)
        self.view.root.bind('<Return>', self.makeHive)
        self.view.root.bind('<Escape>', self.quitGame)
        self.level = 1

    def quitGame(self, event):
        sys.exit()

    def flow(self):
        if sys.argv[0] == "hiveController.py":
            self.view.drawStartScreen()

    def makeHive(self, event):
        self.view.canvas.delete('all')
        x0 = self.x0
        y0 = self.y0
        n = self.view.level+4
        a = 35
        board = self.model.board_coord(n, x0, y0, a)
        for j in range(len(board)):
            for i in range(len(board[j])):
                if board[j][i] != 'null' :
                    x = board[j][i][0]
                    y = board[j][i][1]
                    self.view.creating_hexagon(x, y, a, j, i)
        self.view.generateBoard(n)

    def controlClick(self, event):
        self.view.click()
        self.view.checkColors()
        if self.view.checkColors():
            self.makeHive(event)


game = Controller()
game.flow()
game.view.root.mainloop()
