import pygame
import sys


size = width, height = 800, 800
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


class Game:
    def __init__(self):
        self.sprites = pygame.sprite.Group()
        self.bodyes = pygame.sprite.Group()
        self.start = True
        self.snake = self.SnakeHead((390, 390), 5, self)

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
            self.rect = self.rect.move(self.x_speed, self.y_speed)


g = Game()
g.run()
pygame.quit()