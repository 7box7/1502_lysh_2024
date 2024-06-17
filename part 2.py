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

def distance(coord1, coord2):
    return abs(coord1 - coord2)

self.snake.turn.append([self.snake.rect.x, self.snake.rect.y, self.snake.x_speed, self.snake.y_speed])


check = pygame.sprite.spritecollideany(self, self.game.apples)
if check:
if check.type == 1 or check.type == 2:
    for i in range(self.game.apple.cost):
        body = Game.SnakeBody((self.last.rect.x - 20 * get_sign(self.last.x_speed)
                               - 5 * get_sign(self.last.x_speed) * (i > 0),
                               self.last.rect.y - 20 * get_sign(self.last.y_speed)
                               - 5 * get_sign(self.last.y_speed) * (i > 0)),
                              (self.last.x_speed, self.last.y_speed), self.game,
                              self.game.count + i + 1)

        self.game.all_bodyies.append(body)
        if self.pred is None:
            self.game.bodyes.remove(body)

        self.last.pred = body
        self.last = body

    check.kill()
    self.game.apple = Game.Apple(get_random_pos(self.game.all_board.copy(), self.game.all_bodyies), self.game)

