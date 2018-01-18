class Structure():

    ratio = 3**0.5

    def board_coord(self, n, x0, y0, a):
        Board = [['null']*n for _ in range(n)]
        for j in range(len(Board)):
            for i in range(len(Board[j])):
                p1 = x0
                p2 = y0 + j*(a*(3**0.5))
                if j <= n//2:
                    for i in range(0, n):
                        x = p1 + i*(a+a/2)
                        y = p2 - i*(a*self.ratio/2)
                        if i <= n//2+j:
                            Board[j][i] = [x, y]
                elif j > n//2:
                    for i in range(0, n):
                        x = p1 + i*(a+a/2)
                        y = p2 - i*(a*self.ratio/2)
                        if i > j-n//2-1:
                            Board[j][i] = [x, y]

        return Board
