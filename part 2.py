class Apple(Bonus):
    def __init__(self, pos, game):
        super().__init__(pos, game)
        self.add(self.game.apples)
        self.image = pygame.image.load("apple.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = pygame.Rect(pos, (16, 16))
        self.cost = 1
        self.type = 1


class SnakeBody(pygame.sprite.Sprite):
    def __init__(self, pos, spds, game, index):
        super().__init__(game.sprites)
        self.add(game.bodyes)
        self.image = pygame.image.load("body.png")
        self.rect = pygame.Rect(pos, (20, 20))
        self.x_speed = spds[0]
        self.y_speed = spds[1]
        self.pred = None
        self.game = game
        self.turn = []
        self.index = index

    def update(self):
        self.rect = self.rect.move(self.x_speed, self.y_speed)

        if self.turn:
            if distance(self.rect.x, self.turn[0][0]) < 5 and distance(self.rect.y, self.turn[0][1]) < 5:
                self.x_speed = self.turn[0][2]
                self.y_speed = self.turn[0][3]
                if self.pred is not None:
                    self.pred.turn.append(self.turn.pop(0))
                else:
                    self.turn.pop(0)


class Bonus(pygame.sprite.Sprite):
    def __init__(self, pos, game):
        super().__init__(game.sprites)
        self.add(game.apples)
        self.rect = pygame.Rect(pos, (16, 16))
        self.game = game


