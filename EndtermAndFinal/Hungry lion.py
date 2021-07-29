import pygame
import random

pygame.init()
pygame.mixer.init()

BLACK = (0, 0, 0) #for font
WHITE = (255, 255, 255) # for screen
GREEN = (0, 255, 0) # for increase
RED = (255, 0, 0) # for decrease
BLUE = (0, 0, 255) # for lion

SCREEN_WIDTH = 700 
SCREEN_HEIGHT = 500
speed = 6 # how much pixels lion will move per sec

score_font = pygame.font.SysFont('comicsansms', 20, True, True)
game_over_font = pygame.font.SysFont("comicsansms", 20)
decrease_sound = pygame.mixer.Sound('decrease.mp3')


class Decrease(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([25, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

    def reset_pos(self):
        # by random we choose where it gonna spawn
        self.rect.y = random.randrange(-500, 0)
        self.rect.x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # move
        self.rect.y += 1
        # if it will go lower thane height we move it back
        if self.rect.y > SCREEN_HEIGHT + self.rect.height:
            self.reset_pos()


class Increase(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([25, 20])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()

    def reset_pos_eat(self):
        self.rect.y = random.randrange(20, SCREEN_HEIGHT - 40)
        self.rect.x = random.randrange(20, SCREEN_WIDTH - 20)

    def update(self):
        self.rect.y += random.randint(-2, 2)
        self.rect.x += random.randint(-2, 2)


class Lion(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()

    def update(self):
        pos = pygame.key.get_pressed()
        if pos[pygame.K_a]:
            self.rect.x -= speed
        elif pos[pygame.K_d]:
            self.rect.x += speed
        elif pos[pygame.K_w]:
            self.rect.y -= speed
        elif pos[pygame.K_s]:
            self.rect.y += speed


class Game(object):

    def __init__(self):
        self.score = 0
        self.game_over = False
        self.game_completed = False

        self.decrease_list = pygame.sprite.Group()
        self.increase_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        for i in range(30):
            decrease = Decrease()
            increase = Increase()

            decrease.rect.x = random.randrange(SCREEN_WIDTH)
            decrease.rect.y = 0

            increase.rect.x = random.randrange(20, SCREEN_WIDTH - 20)
            increase.rect.y = random.randrange(20, SCREEN_HEIGHT - 40)

            self.decrease_list.add(decrease)
            self.all_sprites_list.add(decrease)

            self.increase_list.add(increase)
            self.all_sprites_list.add(increase)

        self.lion = Lion()
        self.all_sprites_list.add(self.lion)

    def process_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                return True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                if self.game_over:
                    self.__init__()
        return False

    def logic(self):

        if not self.game_over:
            self.all_sprites_list.update()

            decrease_collision_list = pygame.sprite.spritecollide(self.lion, self.decrease_list, True)
            increase_colllision_list = pygame.sprite.spritecollide(self.lion, self.increase_list, True)

            for food in decrease_collision_list:
                decrease_sound.play()
                self.score -= 1
            for food in increase_colllision_list:
                self.score += 1
                increase_colllision_list.pop()

            if len(self.increase_list) == 0:
                self.game_completed = True
            elif self.score <= -5:
                self.game_over = True

    def display_frame(self, screen):

        screen.fill(WHITE)
        render_score = score_font.render(f'SCORE: {self.score}', True, BLACK)
        screen.blit(render_score, (10, 5))
        if self.game_over:
            text = game_over_font.render("Game Over! Press C-Play Again or Q-Quit", True, BLACK)
            screen.blit(text, [(SCREEN_WIDTH // 2) - (text.get_width() // 2), (SCREEN_HEIGHT // 2) - (text.get_height() // 2)])

        if not self.game_over:
            self.all_sprites_list.draw(screen)

        pygame.display.flip()


def main():

    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Hungry lion")

    clock = pygame.time.Clock()

    game = Game()
    done = False

    while not done:
        done = game.process_events()
        game.logic()
        game.display_frame(screen)
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()