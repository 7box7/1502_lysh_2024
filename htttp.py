import pygame
import random
import sys


size = width, height = 800, 800
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


class Game:
    def __init__(self):
        self.sprites = pygame.sprite.Group()
        self.bodyes = pygame.sprite.Group()
        self.apples = pygame.sprite.Group()
        self.start = True
        self.snake = self.SnakeHead((390, 390), 5, self)
        self.count = 0

        self.apple = Game.Apple(get_random_pos(), self)

    def run(self):
        screen.fill(pygame.Color(0, 0, 0))
        tick = 60

        self.sprites.draw(screen)
        self.sprites.update()
        pygame.display.flip()
        clock.tick(tick)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    ys = self.snake.y_speed != 0
                    xs = self.snake.x_speed != 0
                    turns = [
                        (event.key == pygame.K_a or event.key == pygame.K_LEFT) and ys,
                        (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and ys,
                        (event.key == pygame.K_w or event.key == pygame.K_UP) and xs,
                        (event.key == pygame.K_s or event.key == pygame.K_DOWN) and xs
                    ]
                    if any(turns):
                        spd = 5
                        self.snake.x_speed = turns[0] * -spd + turns[1] * spd
                        self.snake.y_speed = turns[2] * -spd + turns[3] * spd

                        self.snake.turn.append([self.snake.rect.x, self.snake.rect.y, self.snake.x_speed, self.snake.y_speed])

            screen.fill(pygame.Color(0, 0, 0))
            self.sprites.draw(screen)
            self.sprites.update()
            pygame.display.flip()
            clock.tick(tick)

    class SnakeHead(pygame.sprite.Sprite):
        def __init__(self, pos, spd, game):
            super().__init__(game.sprites)
            self.image = pygame.image.load("body.png")
            self.rect = pygame.Rect(pos, (20, 20))
            self.x_speed = 0
            self.y_speed = spd
            self.turn = []
            self.pred = None
            self.last = self
            self.screen = screen
            self.game = game

        def update(self):
            check = pygame.sprite.spritecollideany(self, self.game.apples)
            if check:
                if check.type == 1:
                    for i in range(self.game.apple.cost):
                        body = Game.SnakeBody((self.last.rect.x - 20 * get_sign(self.last.x_speed)
                                               - 5 * get_sign(self.last.x_speed) * (i > 0),
                                               self.last.rect.y - 20 * get_sign(self.last.y_speed)
                                               - 5 * get_sign(self.last.y_speed) * (i > 0)),
                                              (self.last.x_speed, self.last.y_speed), self.game,
                                              self.game.count + i + 1)

                        if self.pred is None:
                            self.game.bodyes.remove(body)

                        self.last.pred = body
                        self.last = body

                    check.kill()
                    self.game.apple = Game.Apple(get_random_pos(), self.game)
            self.rect = self.rect.move(self.x_speed, self.y_speed)

            if self.turn:
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


def distance(coord1, coord2):
    return abs(coord1 - coord2)


def get_random_pos():
    pos = random.randint(50, 750), random.randint(50, 750)
    return pos


def get_sign(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    return 1


g = Game()
g.run()
pygame.quit()
