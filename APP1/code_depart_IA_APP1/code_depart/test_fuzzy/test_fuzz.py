class test_fuzz:
    def __init__(self, Games2D_obj):
        self.G2D = Games2D_obj


    def move(self):
        for i in range(400):
            self.G2D.deplacement((60, 60), 'DOWN')
            if self.G2D.on_coin_collision():
                self.G2D.score += 1
            if self.G2D.on_treasure_collision():
                self.G2D.score += 10
        for i in range(330):
            self.G2D.deplacement((60, 60), 'UP')
            if self.G2D.on_coin_collision():
                self.G2D.score += 1
            if self.G2D.on_treasure_collision():
                self.G2D.score += 10
        for i in range(400):
            self.G2D.deplacement((60, 60), 'RIGHT')
            if self.G2D.on_coin_collision():
                self.G2D.score += 1
            if self.G2D.on_treasure_collision():
                self.G2D.score += 10
        for i in range(400):
            self.G2D.deplacement((60, 60), 'LEFT')
            if self.G2D.on_coin_collision():
                self.G2D.score += 1
            if self.G2D.on_treasure_collision():
                self.G2D.score += 10
